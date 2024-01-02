import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

# Importamos el dataset como un dataframe
madrid = pd.read_csv("../Data/Raw/buy_houses_Madrid.csv",
                     sep=';')


# Convertimos el Zipcode a str y separamos sus ultimos 3 numeros
madrid['Zipcode'] = madrid['Zipcode'].astype(str).str[2:5]

# Convertimos el zipcode a int
madrid["Zipcode"] = madrid["Zipcode"].astype(int)

# Separamos el año y eliminamos la columna date
madrid['Year']=madrid['Date'].str.split('-').str[0]
madrid.drop(['Date'],axis=1,inplace=True)

# Eliminamos las viviendas duplicadas
madrid.drop_duplicates(subset=["Zipcode", "Address", 
                               "Latitude", "Longitude",
                               "Price", "Surface"],
                               inplace=True)

# Renombrar las columnas del DataFrame con nombres en español
nombres_espanyol = ['Direccion', 'Codigo_Postal', 'Latitud', 'Longitud', 'Precio', 'Habitaciones',
       'Baños', 'Superficie_m2', 'Piso', 'Ascensor', 'Aire_Acondicionado',
       'Calefaccion', 'Parking', 'Balcon', 'Terraza', 'Piscina', 'Año']
# Utilizamos rename para renombrarlas y Zip para que recorra las columnas de df
madrid = madrid.rename(columns=dict(zip(madrid.columns, nombres_espanyol)))
madrid.columns

# Borramos las casas que estén fuera de madrid ciudad
filtro_cp = madrid["Codigo_Postal"] > 99
madrid = madrid[~filtro_cp]

# Eliminamos los valores que tienen una superficie menor a 15 m2 interpretando que son errores
filtro_15 = madrid["Superficie_m2"] < 15
madrid = madrid[~filtro_15]

# Eliminamos las casas que no tienen baños
filtro_banyo = madrid["Baños"]==0
madrid = madrid[~filtro_banyo]

# Eliminamos los valores de casas que sean muy baratas para su tamaño
filtro = (madrid["Precio"] < 75000) & (madrid["Superficie_m2"] > 60)
madrid = madrid[~filtro] 

# Eliminamos las casas con precio 0
# Despues vemos si podemos buscar los valores
filtro_cero = madrid['Precio'] == 0
madrid = madrid[~filtro_cero] 

# Eliminamos las casas que no tienen habitaciones y cuentan con una superficie grande como para que sea un estudio
filtro2 = (madrid["Habitaciones"] == 0) & (madrid["Superficie_m2"] > 55)
madrid = madrid[~filtro2]

# Nos parece que si una casa tiene 9 habitaciones en menos de 300 metros cuadrados puede haber un error
filtro3 = (madrid["Habitaciones"] > 8) & (madrid["Superficie_m2"] < 300)
madrid[filtro3] 
madrid = madrid[~filtro3]

estudios_varios_baños = (madrid['Habitaciones'] == 0) & (madrid['Baños'] > 1)
estudios_varios_baños
madrid = madrid[~estudios_varios_baños]

pocos_banyos = (madrid['Habitaciones'] > 5) & (madrid['Baños'] < 2)
madrid[pocos_banyos].sort_values(by='Precio')
madrid = madrid[~pocos_banyos]

pocos_banyos2 = (madrid['Habitaciones'] > 6) & (madrid['Baños'] < 3)
madrid[pocos_banyos2].sort_values(by='Precio')
madrid = madrid[~pocos_banyos2]

madrid = madrid.drop(madrid[madrid['Longitud'] == 0].index)

# Sacamos el precio medio por codigo postal
cp_med = madrid.groupby("Codigo_Postal")["Precio"].mean().reset_index()
# Lo convertimos en un diccionario para poder mapearlo
precio_medio_dict = cp_med.set_index('Codigo_Postal')['Precio'].to_dict()
# Creamos una nueva columna con el precio medio por coidgo postal
madrid['Precio_Medio_cp'] = madrid['Codigo_Postal'].map(precio_medio_dict)
madrid['Precio_Medio_cp'] = madrid['Precio_Medio_cp'].astype(int)

Luxury = madrid["Precio"] > 10000000
madrid = madrid[~Luxury]

# Eliminamos la columna Dirección y Año que no tiene datos que sean relevantes
madrid = madrid.drop(columns=["Direccion","Año"],axis=1)

# Dicconario cp y media cp

# Sacamos el precio medio por codigo postal
cp_med = madrid.groupby("Codigo_Postal")["Precio"].mean().reset_index()
# Lo convertimos en un diccionario para poder mapearlo
precio_medio_dict = cp_med.set_index('Codigo_Postal')['Precio'].to_dict()

# Funcion para guardar CSV 
def csv(nombre_archivo, archivo_guardar):
    ruta_archivo = '../Data/Processed/' + nombre_archivo + '.csv'
    archivo_guardar.to_csv(ruta_archivo, index=False)
# Guardamos el CSV Madrid para crear, entrenar y validar los modelos
csv("madrid", madrid)

