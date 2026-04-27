import pandas as pd
import numpy as np
from functions_housing import obtener_codigo_postal, csv

# ── Carga ────────────────────────────────────────────────────────────────────
madrid = pd.read_csv("../Data/Raw/buy_houses_Madrid.csv", sep=';')

# ── Códigos postales ─────────────────────────────────────────────────────────
# Completamos los CP nulos o que no pertenecen a Madrid usando geocodificación inversa
madrid['Zipcode'] = madrid.apply(obtener_codigo_postal, axis=1)

# Extraemos solo los últimos 3 dígitos (28007 → 7) y convertimos a int
madrid['Zipcode'] = madrid['Zipcode'].astype(str).str[2:5].astype(int)

# ── Fecha ────────────────────────────────────────────────────────────────────
madrid['Year'] = madrid['Date'].str.split('-').str[0]
madrid.drop(columns=['Date'], inplace=True)

# ── Duplicados ───────────────────────────────────────────────────────────────
madrid.drop_duplicates(
    subset=["Zipcode", "Address", "Latitude", "Longitude", "Price", "Surface"],
    inplace=True
)

# ── Renombrar columnas ───────────────────────────────────────────────────────
nombres = ['Direccion', 'Codigo_Postal', 'Latitud', 'Longitud', 'Precio',
           'Habitaciones', 'Baños', 'Superficie_m2', 'Piso', 'Ascensor',
           'Aire_Acondicionado', 'Calefaccion', 'Parking', 'Balcon',
           'Terraza', 'Piscina', 'Año']
madrid = madrid.rename(columns=dict(zip(madrid.columns, nombres)))

# ── Filtros de limpieza ───────────────────────────────────────────────────────
# Fuera de Madrid ciudad
madrid = madrid[madrid["Codigo_Postal"] <= 99]

# Superficie mínima (< 20 m² se considera error)
madrid = madrid[madrid["Superficie_m2"] >= 20]

# Sin baños
madrid = madrid[madrid["Baños"] > 0]

# Muy baratas para su tamaño
madrid = madrid[~((madrid["Precio"] < 75000) & (madrid["Superficie_m2"] > 60))]

# Precio cero
madrid = madrid[madrid["Precio"] > 0]

# Estudios con superficie grande (probablemente error en habitaciones)
madrid = madrid[~((madrid["Habitaciones"] == 0) & (madrid["Superficie_m2"] > 55))]

# Demasiadas habitaciones para la superficie
madrid = madrid[~((madrid["Habitaciones"] > 8) & (madrid["Superficie_m2"] < 300))]

# Estudios con varios baños
madrid = madrid[~((madrid["Habitaciones"] == 0) & (madrid["Baños"] > 1))]

# Pocas habitaciones para los baños que tiene
madrid = madrid[~((madrid["Habitaciones"] > 5) & (madrid["Baños"] < 2))]
madrid = madrid[~((madrid["Habitaciones"] > 6) & (madrid["Baños"] < 3))]

# Sin coordenadas
madrid = madrid[madrid["Longitud"] != 0]

# ── Feature engineering ───────────────────────────────────────────────────────
# Precio medio por código postal
precio_medio_dict = madrid.groupby("Codigo_Postal")["Precio"].mean().to_dict()
madrid["Precio_Medio_cp"] = madrid["Codigo_Postal"].map(precio_medio_dict).astype(int)

# ── Outliers de precio ────────────────────────────────────────────────────────
# Eliminamos propiedades de lujo extremo (> 5M€) para no desbalancear el modelo
madrid = madrid[madrid["Precio"] <= 5_000_000]

# ── Selección final de columnas ───────────────────────────────────────────────
madrid = madrid.drop(columns=["Direccion", "Año", "Codigo_Postal", "Longitud", "Piso"])

# ── Guardamos ────────────────────────────────────────────────────────────────
csv("madrid", madrid)
print(f"CSV guardado: {madrid.shape[0]} filas, {madrid.shape[1]} columnas")
