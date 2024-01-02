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
from sklearn.model_selection import cross_val_score
import pickle
import shap
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from geopy.geocoders import Nominatim
from sklearn.decomposition import PCA

# Cargamos el archivo
df_mad = pd.read_csv("../Data/Processed/madrid.csv")

# Creamos X e Y

X = df_mad.drop(columns=["Precio"], axis=1)
y = df_mad["Precio"]

# Creamos los train y test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Escalamos los datos del train con StandardScaler()
scal = StandardScaler() # Declaramos el modelo
scal.fit(X_train) # Entrenamos el modelo
X_train_scal = scal.transform(X_train) # Aplicamos el scaler en los datos de Train 
X_test_scal = scal.transform(X_test) # Aplicamos el scaler en los datos del test

# Model

# Definimos los pasos del Pipeline
steps = [ ('n_estimators',None),
    ('model', None)  # Modelo a evaluar (se especificará posteriormente)
]

# Crear el pipeline
pipeline = Pipeline(steps)

# Definir los hiperparámetros a ajustar para cada modelo
parameters = [
    {
        'model': [LinearRegression()]  # Regresión lineal
    },
    {
        'model': [RandomForestRegressor()],  # RandomForestRegressor
        'model__n_estimators': [10, 50, 100],  # Número de árboles en el bosque
        'model__max_depth': [None, 5, 10],  # Profundidad máxima de los árboles
    }
]

# Realizar la búsqueda de hiperparámetros y seleccionar el mejor modelo
grid_search = GridSearchCV(pipeline, parameters, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)  # X_train y y_train son tus datos de entrenamiento

# Obtener el mejor modelo y sus hiperparámetros
best_model = grid_search.best_estimator_
best_model
# Pipeline(steps=[('n_estimators', None), ('model', RandomForestRegressor())])

# Importamos el modelo y lo entrenamos

rf = RandomForestRegressor()
rf.fit(X_train,y_train)
import pickle
# Exportamos el RandomForestRegresor del Pipeline
with open('../models/Rf.pkl', 'wb') as salida:
    pickle.dump(rf,salida)

