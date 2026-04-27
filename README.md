# Predicción Precios de Viviendas en Madrid

![portada](Data/portada.jpg)


<h2>📝 Introducción</h2>

En este proyecto, nos enfocamos en la aplicación de machine learning para predecir los precios de venta de viviendas en Madrid, proporcionando una descripción detallada del trabajo realizado. Identificamos tendencias, correlaciones y patrones que ofrecen una visión clara de la dinámica de precios en el sector inmobiliario madrileño.

Estos hallazgos pueden resultar de gran utilidad tanto para las agencias inmobiliarias, que pueden ajustar sus estrategias de valoración y marketing, como para los compradores, quienes obtendrán una visión más informada sobre el valor real de una propiedad.

//

In this project, we focus on the application of machine learning to predict home sale prices in Madrid, providing a detailed description of the work performed. We identify trends, correlations and patterns that provide a clear picture of the price dynamics in the Madrid real estate sector.

These insights can be of great use both to real estate agencies, who can adjust their valuation and marketing strategies, and to buyers, who will gain a more informed view of the real value of a property.


<h2>👾 Aplicación</h2>

Haz clic en el icono de Streamlit para ejecutar la aplicación.

//

Click on the Streamlit icon to run the application.


<a href="https://house-price-predictor-spomi.streamlit.app/">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png" title="Streamlit" alt="Streamlit" width="100" height="100"/>
</a>


<h2>💾 Estructura Repositorio</h2>

En la estructura de carpetas, se han incluido las siguientes secciones:

- **`App/`**: Contiene la aplicación Streamlit. `app.py` es el archivo principal y `requirements.txt` lista las dependencias necesarias.

- **`Data/`**: Contiene los archivos de datos. La subcarpeta `Raw/` almacena el dataset original. La carpeta `Processed/` contiene el dataframe procesado y listo para su uso.

- **`Models/`**: Contiene el modelo entrenado en formato joblib (`Rf.joblib`).

- **`Notebooks/`**: Contiene los cuadernos Jupyter del proyecto. `01_EDA_&_Preprocesamiento.ipynb` realiza el análisis exploratorio y el procesamiento de datos. `02_Entrenamiento_y_validacion_modelos.ipynb` crea, entrena y evalúa los modelos.

- **`src/`**: Contiene los scripts Python del proyecto. `data_processing.py` procesa el dataset raw y genera `madrid.csv`. `model.py` entrena y guarda el modelo. `functions_housing.py` contiene funciones auxiliares compartidas.

- **`Docs/`**: Contiene la Memoria del proyecto con la documentación completa.

- **`README.md`**: Archivo principal con información general del proyecto.


<h2>📁 Estructura Carpetas</h2>

    HOUSE_PRICE_PREDICTION_MADRID
    ├── App
    │   ├── app.py
    │   └── requirements.txt
    │
    ├── Data
    │   ├── Processed
    │   │   └── madrid.csv
    │   └── Raw
    │       └── buy_houses_Madrid.csv
    │
    ├── Docs
    │   └── Memoria.pdf
    │
    ├── Models
    │   └── Rf.joblib
    │
    ├── Notebooks
    │   ├── 01_EDA_&_Preprocesamiento.ipynb
    │   └── 02_Entrenamiento_y_validacion_modelos.ipynb
    │
    ├── src
    │   ├── data_processing.py
    │   ├── functions_housing.py
    │   └── model.py
    │
    └── README.md


<h2>🏷️ Variables</h2>

En este proyecto hemos trabajado con las siguientes variables:

1. **Address** → Dirección de la vivienda
2. **Zipcode** → Código Postal
3. **Latitude** → Latitud
4. **Longitude** → Longitud
5. **Price** → Precio de la casa
6. **Date** → Fecha de publicación del aviso de venta
7. **Rooms** → Número de habitaciones
8. **Bathrooms** → Número de baños
9. **Surface** → Superficie de la vivienda en metros cuadrados
10. **Floor** → Numero de piso
11. **Elevator** → Si tiene ascensor
12. **Air_Conditioner** → Si tiene aire acondicionado
13. **Heater** → Si tiene calefacción
14. **Parking** → Si tiene parking
15. **Balcony** → Si tiene balcón
16. **Terrace** → Si tiene terraza
17. **Swimming_Pool** → Si tiene piscina


<h2>📚 Librerías Utilizadas</h2>
<div>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" title="Numpy" alt="Numpy" width="180" height="180"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" title="Pandas" alt="Pandas" width="180" height="180"/>
<img src="https://matplotlib.org/stable/_static/logo_dark.svg" title="Matplotlib" alt="Matplotlib" width="220" height="180"/>
<img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" title="Seaborn" alt="Seaborn" width="180" height="180"/>
<img src="https://www.statsmodels.org/stable/_images/statsmodels-logo-v2-horizontal.svg" title="Statsmodels" alt="Statsmodels" width="180" height="180"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/b/b2/SCIPY_2.svg" title="Scipy" alt="Scipy" width="100" height="100"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" title="Scikit-learn" alt="Scikit-learn" width="180" height="180"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png" title="Streamlit" alt="Streamlit" width="180" height="180"/>
<img src="https://joblib.readthedocs.io/en/stable/_static/joblib_logo.svg" title="Joblib" alt="Joblib" width="180" height="180"/>
<img src="https://geopy.readthedocs.io/en/stable/_images/logo-wide.png" title="Geopy" alt="Geopy" width="180" height="180"/>
</div>


<h2>📥 Fuentes</h2>
<a href="https://www.idealista.com/">
  <img src="https://st3.idealista.com/static/common/img/idealista.svg" title="Idealista" alt="Idealista" width="180" height="180"/>
</a>
<a href="https://www.kaggle.com/datasets">
  <img src="https://www.kaggle.com/static/images/site-logo.svg" title="Kaggle" alt="Kaggle" width="180" height="180"/>
</a>

<br></br>
<p>Espero que este proyecto haya sido de tu interés.<br>
No dudes en consultarme cualquier duda que te haya surgido y siéntete libre de compartirlo. Estoy abierto a recibir tus comentarios y sugerencias.

//

I hope this project has been of interest to you. Feel free to ask me any questions that may have arisen, and feel free to share it. I am open to receiving your comments and suggestions.

</p></br>

<h2>👨‍💻 Autor</h2>
<a href="https://www.linkedin.com/in/sebastianpomi/" target="_blank">Sebastian Pomi</a>
