import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError


# Geocodificador para completar códigos postales nulos o inválidos
geolocator = Nominatim(user_agent="Madrid_Housing_Predict_Price")

def obtener_codigo_postal(row):
    """Completa el código postal usando coordenadas cuando es nulo o no empieza por 28."""
    try:
        if pd.isna(row['Zipcode']) or not str(row['Zipcode']).startswith("28"):
            location = geolocator.reverse((row['Latitude'], row['Longitude']), exactly_one=True)
            if location:
                zipcode = location.raw.get('address', {}).get('postcode', None)
                if zipcode:
                    return zipcode
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Error geocodificando: {e}")
    return row['Zipcode']


def csv(nombre_archivo, archivo_guardar):
    """Guarda un DataFrame como CSV en la carpeta Data/Processed."""
    ruta_archivo = '../Data/Processed/' + nombre_archivo + '.csv'
    archivo_guardar.to_csv(ruta_archivo, index=False)


def valoracion_modelos(tipo, modelo, X_test, y_test):
    """Imprime las métricas de evaluación de un modelo."""
    y_pred = modelo.predict(X_test)
    print(f"R²:   {tipo} → {r2_score(y_test, y_pred):.4f}")
    print(f"MAE:  {tipo} → {mean_absolute_error(y_test, y_pred):,.0f}")
    print(f"MSE:  {tipo} → {mean_squared_error(y_test, y_pred):,.0f}")
    print(f"MAPE: {tipo} → {np.mean(np.abs((y_test - y_pred) / y_test)) * 100:.2f}%")
