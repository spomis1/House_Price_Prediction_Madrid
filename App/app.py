import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler,MinMaxScaler
import pickle
from sklearn.preprocessing import OrdinalEncoder
import os
import joblib

# Obtén la ruta del directorio actual del script
script_directory = os.path.dirname(__file__)

try:
    modelo = joblib.load(os.path.join(script_directory, '../Models/Rf.joblib'))
    print(f"Modelo cargado exitosamente. Tipo: {type(modelo)}, Forma: {modelo.shape}")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")


# Obtener la ruta al directorio actual del script
script_directory_logo = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta a la imagen
ruta_logo = os.path.join(script_directory_logo, '..', 'Data', 'logo.png')



# Diccionario de códigos postales
codigos_postales = {28000: 942338.7096774194,
 28001: 1709528.2558139535,
 28002: 700100.0,
 28003: 898889.1936758893,
 28004: 745917.0051282052,
 28005: 421413.22340425535,
 28006: 1207212.7969348659,
 28007: 529747.4950495049,
 28008: 766309.9516129033,
 28009: 941621.881147541,
 28010: 1018679.0,
 28011: 259011.09722222222,
 28012: 439992.61352657,
 28013: 760050.7389162561,
 28014: 856046.2035928144,
 28015: 669236.22265625,
 28016: 923762.2047244095,
 28017: 238758.1822222222,
 28018: 166500.23076923078,
 28019: 226302.790625,
 28020: 597620.078313253,
 28021: 156772.0170940171,
 28022: 280852.7788461539,
 28023: 1274253.9473684211,
 28024: 199225.49019607843,
 28025: 197312.21474358975,
 28026: 202513.95977011495,
 28027: 379788.88940092165,
 28028: 603234.0625,
 28029: 347317.4657534247,
 28030: 247271.43023255814,
 28031: 234693.22093023255,
 28032: 260153.3309859155,
 28033: 471372.82608695654,
 28034: 718994.5789473684,
 28035: 733699.8554913295,
 28036: 1197915.3047619048,
 28037: 260568.84,
 28038: 164928.84375,
 28039: 301371.1179245283,
 28040: 645360.0,
 28041: 212177.72661870503,
 28042: 457692.8321167883,
 28043: 911651.9774011299,
 28044: 192864.3,
 28045: 357857.48703170026,
 28046: 1134196.1240310078,
 28047: 219078.36036036036,
 28048: 764000.0,
 28049: 561631.5789473684,
 28050: 480497.57692307694,
 28051: 314346.0256410256,
 28052: 382726.42,
 28053: 152717.6043956044,
 28054: 255165.5172413793,
 28055: 761064.5161290322}



distritos = { 
'Centro': [28004, 28005, 28012, 28013, 28014],
'Argenzuela':[28045],
'Retiro': [28007, 28008, 28009],
'Salamanca': [28001, 28006, 28028],
'Chamartín': [28002, 28016, 28036, 28046],
'Tetuán': [28020, 28035, 28039],
'Chamberí': [28003, 28010, 28015],
'Fuencarral-El Pardo': [28029,28034,28048,28049],
'Moncloa-Aravaca': [28011, 28023,28040],
'Latina': [28019, 28024, 28044, 28047,28054],
'Carabanchel': [28025],
'Usera': [28026],
'Puente de Vallecas': [28018, 28038, 28053],
'Moratalaz': [28030],
'Ciudad Lineal': [28017, 28027, 28037],
'Hortaleza': [28033, 28043, 28050],
'Villaverde': [28021],
'Villa de Vallecas':[ 28031],
'Vicálvaro': [28032],
'San Blas-Canillejas': [28022],
'Barajas': [28042, 28055]
}



# Función principal de la app
def main():


    st.set_page_config(page_title="Predicción de Precios", page_icon=":house:",layout="wide",
        initial_sidebar_state="expanded")


    c1, c2 = st.columns([.85, .20])
    c1.title('PREDICTOR DE PRECIOS DE VIVIENDAS :crystal_ball:')
    c1.subheader('¿Cuánto pagarás por tu nuevo hogar? :european_castle:')
    c2.image(ruta_logo, width=200)
    

    Zonas = {
        'Norte': ['Chamartín','Tetuán','Fuencarral-El Pardo','Hortaleza','Barajas'],
        'Centro': ['Centro','Argenzuela','Retiro','Salamanca','Chamberí','Moncloa-Aravaca','Ciudad Lineal','Latina','San Blas-Canillejas'],
        'Sur': ['Carabanchel','Usera','Puente de Vallecas','Moratalaz','Villaverde','Villa de Vallecas','Vicálvaro']
    }

    # Selector para elegir la Zona
    zona_seleccionada = st.selectbox("Elige la zona de Madrid:", list(Zonas.keys()))
    if zona_seleccionada == "Norte":
        latitud = np.random.uniform(40.530510, 40.442550)
    elif zona_seleccionada == "Centro":
        latitud = np.random.uniform(40.442550, 40.398802)
    else:
        latitud = np.random.uniform(40.398802, 40.331640)
     # Selector para elegir el Distrito en función de la Zona
    distrito_seleccionado = st.selectbox("Elige el distrito:", Zonas[zona_seleccionada])

    #  Selector de código postal basado en el distrito seleccionado
    codigo_seleccionado = st.selectbox("Elige el código postal:", distritos[distrito_seleccionado])

    # Obtener el valor correspondiente del diccionario
    valor_codigo = codigos_postales[codigo_seleccionado]
    # Creando los casilleros para que el usuario introduzca los datos
    
    superficie_m2 = st.number_input("Introduce la Superficie (m2)", min_value=17.0)
    baños = st.number_input("Introduce la Cantidad de Baños", min_value=1)
    habitaciones = st.number_input("Introduce la Cantidad de Habitaciones", min_value=1)
    ascensor = st.checkbox("¿Ascensor?")
    parking = st.checkbox("¿Parking?")
    balcon = st.checkbox("¿Balcon?")
    piscina = st.checkbox("¿Piscina?")
    terraza = st.checkbox("¿Terraza?")
    aire_acondicionado = st.checkbox("¿Aire Acondicionado?")
    calefaccion = st.checkbox("¿Calefacción?")



    # Cuando se presione el botón de predicción
    if st.button("Predecir Precio"):

        # Verificar si el modelo se cargó correctamente
        if modelo is None:
            st.error("Error: El modelo no se cargó correctamente.")
            st.stop()

        # Crear un DataFrame con los datos ingresados
        datos_entrada = pd.DataFrame({
            'Latitud': [latitud],
            'Precio_Medio_cp': [valor_codigo],
            'Superficie_m2': [superficie_m2],
            'Habitaciones': [habitaciones],
            'Baños': [baños],
            'Ascensor': [ascensor],
            'Parking':[parking],
            'Balcon': [balcon],
            'Aire_Acondicionado': [aire_acondicionado],
            'Calefaccion': [calefaccion],
            'Piscina': [piscina],
            'Terraza': [terraza],
        })

    

        # Realizar la predicción con el modelo
        precio_predicho = modelo.predict(datos_entrada)[0]

        # Mostrar el resultado
        st.success(f"El precio estimado de la vivienda es: €{precio_predicho:,.2f}")


if __name__ == '__main__':
    main()
