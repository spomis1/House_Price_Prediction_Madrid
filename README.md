# Predicción Precios de Viviendas en Madrid

![portada](Data/portada.jpg)


<h2> 📝 Introducción</h2>

Este proyecto se abordará la aplicación del machine learning para predecir los precios de venta de las viviendas en madrid, brindando una descripción detallada del trabajo realizado. Identificaremos tendencias, correlaciones y patrones que ofrezcan una visión clara sobre la dinámica de precios en el sector inmobiliario madrileño. <br> 
Estos descubrimientos pueden ser de gran utilidad para las agencias inmobiliarias, que pueden afinar sus estrategias de valoración y marketing, y para los compradores, que obtendrán una visión más informada sobre el valor real de una propiedad.


<h2>👾Aplicación</h2>

Haz clic en el icono de Streamlit para ejecutar la aplicación.<br>


<a href="https://house-price-predictor-spomi.streamlit.app/">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png" title="Streamlit" alt="Streamlit" width="100" height="100"/>
</a>


<h2> 💾 Estructura Repositorio</h2>

En la estructura de carpetas, se han incluido las siguientes secciones:

- Carpeta "data": Contiene los archivos relacionados con los datos. La subcarpeta "raw" almacena el archivo original del dataframe. La carpeta "Processed" contiene el dataframe procesado y listo para su uso.

- Carpeta "models": Contiene el modelo entrenado en formato pickle.

- Carpeta "notebooks": Contiene los cuadernos Jupyter utilizados durante el desarrollo del proyecto. El cuaderno "01_EDA_&_Preprocesamiento.ipynb" se utiliza para realizar el análisis exploratorio y para el procesamiento de los datos. El cuaderno "02_Entrenamiento_y_validacion_modelos.ipynb" se utiliza para la creación, entrenamiento y evaluación los modelos y realizar comparaciones.

- Carpeta "src": Contiene los archivos Python que contienen el código fuente para el procesamiento de datos y la creación del modelo. El archivo "data_processing.py" contiene el código para procesar los datos y generar el archivo "madird.csv". El archivo "model.py" contiene el código para crear, entrenar y guardar el modelo en la carpeta "models".

- Carpeta "docs": Contiene la Memoria del proyecto con la información de todo el proyecto.

- "README.md": Este es el archivo principal que proporciona información general sobre el proyecto, incluyendo la descripción de la estructura de carpetas y otras instrucciones o notas relevantes.

<h2> 📁 Estructura Carpetas </h2>

    HOUSE_PRICE_PREDICTION_MADRID
    ├── App
    │   ├── app.py
    │   └── requirements.txt
    │
    ├── Data
    │   ├── Processed
    │   │   ├── __init_py__.py
    │   │   └── madrid.csv
    │   ├── Raw
    │   │   ├── __init_py__.py
    │   │   └── buy_houses_Madrid.csv
    │   ├── logo.png
    │   └─── portada.jpg
    │  
    ├── Docs 
    │   └── Memoria.pdf
    ├── Models
    │   ├── __init__.py
    │   └── Rf.joblib
    │
    ├── Notebooks
    │   ├── 01_EDA_&_Preprocesamiento.ipynb
    │   └── 02_Entrenamiento_y_validacion_modelo.ipynb  
    │ 
    ├── scr
    │   ├── __init__.py
    │   ├── data_processing.py
    │   ├── functions_housing.py
    │   ├── main.py
    │   └── model.py
    │ 
    └── README.md


<h2> 🏷️ Variables</h2>

En este proyecto hemos trabajado con las siguientes variables:


1. **Address->** Dirección de la vivienda
2. **Zipcode->** Código Postal
3. **Latitude ->** Latitud
4. **Longitude->** Longitud
5. **Price ->** Precio de la casa
6. **Date ->** Fecha de publicación del aviso de venta
7. **Rooms ->** Número de habitaciones
8. **Bathrooms ->** Número de baños
9. **Surface->** Superficie de la vivienda en metros cuadrados
10. **Floor->** Numero de piso
11. **Elevator->** Si tiene ascensor
12. **Air_Conditioner->** Si tiene aire acondicionado
13. **Heater ->** Si tiene calefacción
14. **Parking ->** Si tiene parking
15. **Balcony ->** Si tiene balcón
16. **Terrace ->** Si tiene terraza
17. **Swimming_Pool ->** Si tiene piscina

<h2>📚 Librerías Utilizadas</h2>
<div>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" title="Numpy" **alt="Numpy" width="180" height="180"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" title="Pandas" **alt="Pandas" width="180" height="180"/>
<img src="https://matplotlib.org/stable/_static/logo_dark.svg" title="matplotlib" **alt="Matplotlib" width="220" height="180"/>
<img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" title="Seaborn" **alt="Seaborn" width="180" height="180"/>
<img src="https://www.statsmodels.org/stable/_images/statsmodels-logo-v2-horizontal.svg" title="statsmodels" **alt="statsmodels" width="180" height="180"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/b/b2/SCIPY_2.svg" title="scipy" **alt="scipy" width="100" height="100"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" title="Scikit_learn" **alt="Scikit_learn" width="180" height="180"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png" title="Streamlit" **alt="Streamlit" width="180" height="180"/>
<img src="https://joblib.readthedocs.io/en/stable/_static/joblib_logo.svg" title="Joblib" **alt="Joblib" width="180" height="180"/>
<img src="https://geopy.readthedocs.io/en/stable/_images/logo-wide.png" title="Geopy" **alt="Geopy" width="180" height="180"/>

</div>



<h2> 📥 Fuentes</h2> 
<a href="https://www.idealista.com/"> <img src="https://st3.idealista.com/static/common/img/idealista.svg" title="idealista" **alt="idealista" width="180" height="180"/> </a>
<a href="https://www.kaggle.com/datasets"> <img src="https://www.kaggle.com/static/images/site-logo.svg" title="Kaggle" **alt="Kaggle" width="180" height="180"/> </a>

<br></br>
<p>Espero que este proyecto haya sido de tu interés.<br>
No dudes en consultarme cualquier duda que te haya surgido y siéntete libre de compartirlo! Estoy abierto a recibir tus comentarios y sugerencias.

//

I hope this project has been of interest to you. Feel free to ask me any questions that may have arisen, and feel free to share it! I am open to receiving your comments and suggestions.

</p></br>

<h2>👨‍💻 Autor</h2>
<a href="https://www.linkedin.com/in/sebastianpomi/" target="_blank">Sebastian Pomi</a>
