# API_model_tryout

Esta API proporciona una predicción de ventas basada en los gastos de marketing en televisión, radio y periódicos de una empresa. Además, permite agregar datos a la base de datos y reentrenar el modelo.

## Estructura 

* /data: carpeta que contiene los siguientes archivos de datos. ➝ Advertising.csv ➝ advertising_model.pkl

* /imgs_readme: carpeta con el banner

* Adv_data.db: base de datos SQLite donde se almacenan los datos de gastos y ventas.

* README.md: este archivo, que proporciona una descripción general del proyecto.

* app_model.py: código principal de la API FastAPI que define los endpoints.

## Aplicaciones 

1. Predicción

- Endpoint: /predict

- Método: GET

- Descripción: hace una predicción de ventas utilizando el modelo entrenado. Se deben proporcionar valores de gastos en "TV", "radio" y "newspaper" como parámetros de consulta.

2. Ingesta de Datos

- Endpoint: /add_data

- Método: POST

- Descripción: permite agregar nuevos datos de gastos en TV, radio, periódicos y ventas a la base de datos SQLite. Los datos ingresados se utilizan para reentrenar el modelo.

3. Reentrenamiento del Modelo

- Endpoint: /retrain

- Método: POST

- Descripción: realiza el reentrenamiento del modelo utilizando todos los datos almacenados en la base de datos. Después del reentrenamiento, el modelo actualizado se guarda en el sistema de archivos para su uso futuro en predicciones.

4. Herramientas

* FastAPI: construir la API.

* Pandas: librería para la manipulación de datos.

* SQLite: sistema de gestión de bases de datos.

* Pickle: para guardar y cargar el modelo entrenado.
