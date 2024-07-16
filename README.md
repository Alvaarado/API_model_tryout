# API_model_tryout

Esta API proporciona una predicción de ventas basada en los gastos de marketing en televisión, radio y periódicos de una empresa. Además, permite agregar datos a la base de datos y reentrenar el modelo.

## Estructura 

* /data: Carpeta que contiene los siguientes archivos de datos. ➝ Advertising.csv ➝ advertising_model.pkl

* /imgs_readme: Carpeta con el banner

* Adv_data.db: Base de datos SQLite donde se almacenan los datos de gastos y ventas.

* README.md: Este archivo, que proporciona una descripción general del proyecto.

* app_model.py: Código principal de la API FastAPI que define los endpoints.

## Aplicaciones 

1. Predicción

- Endpoint: /predict

- Método: GET

- Descripción: Hace una predicción de ventas utilizando el modelo entrenado. Se deben proporcionar valores de gastos en "TV", "radio" y "newspaper" como parámetros de consulta.

2. Ingesta de Datos

- Endpoint: /add_data

- Método: POST

- Descripción: Permite agregar nuevos datos de gastos en TV, radio, periódicos y ventas a la base de datos SQLite. Los datos ingresados se utilizan para reentrenar el modelo.

3. Reentrenamiento del Modelo

- Endpoint: /retrain

- Método: POST

- Descripción: Realiza el reentrenamiento del modelo utilizando todos los datos almacenados en la base de datos. Después del reentrenamiento, el modelo actualizado se guarda en el sistema de archivos para su uso futuro en predicciones.

4. Herramientas

* FastAPI: Construir la API.

* Pandas: Librería para la manipulación de datos.

* SQLite: Sistema de gestión de bases de datos.

* Pickle: Para guardar y cargar el modelo entrenado.
