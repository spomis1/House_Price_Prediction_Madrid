import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import normaltest
from scipy.stats import anderson
import statsmodels.api as sm
import streamlit as st
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler,MinMaxScaler
import xgboost as xgb
from sklearn.model_selection import cross_val_score
import pickle
import shap
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from geopy.geocoders import Nominatim

# Importamos el dataset como un dataframe
madrid = pd.read_csv("../Data/Raw/buy_houses_Madrid.csv",sep=';')

# Crear un geocodificador Nominatim
geolocator = Nominatim(user_agent="myGeocoder",timeout=10)
# Funcion para completar los Zipcode nulos o los que no comienzan con 28
def obtener_codigo_postal(madrid):
    if pd.isna(madrid['Zipcode']) or not str(madrid['Zipcode']).startswith("28"):
        location = geolocator.reverse((madrid['Latitude'], madrid['Longitude']), exactly_one=True)
        if location:
            zipcode = location.raw.get('address', {}).get('postcode', None)
            if zipcode:
                return zipcode
    return madrid['Zipcode']

# Aplicamos la función para completar los códigos postales
madrid['Zipcode'] = madrid.apply(obtener_codigo_postal, axis=1)


# Guardar CSV

def csv(nombre_archivo, archivo_guardar):

    ruta_archivo = '../Data/Processed' + nombre_archivo + '.csv'
    archivo_guardar.to_csv(ruta_archivo, index=False)

# Funcion de Valoración de los modelos
def valoracion_modelos(tipo, modelo, Xtest, ytest):
    y_pred = modelo.predict(Xtest)
    print("R2_score",tipo, r2_score(ytest , y_pred))
    print("MAE", tipo, mean_absolute_error(ytest, y_pred))
    print("MSE",tipo, mean_squared_error(ytest, y_pred))
    print("MAPE",tipo,np.mean(np.abs((ytest-y_pred)/ytest)) * 100)