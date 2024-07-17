from fastapi import FastAPI, HTTPException
import uvicorn
import os
import pickle
import pandas as pd
import sqlite3

# Cargamos el modelo

model_path = './data/advertising_model.pkl'
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

advertising_df = pd.read_csv('./data/advertising_clean.csv')
conn = sqlite3.connect('adv_data_clean.db')
advertising_df.to_sql('advertising_clean', conn, if_exists='replace', index=False)

app = FastAPI()

conec = sqlite3.connect('adv_data_clean.db')
cursor = conec.cursor()

# Saludo de entrada

@app.get("/")
async def saludo():
    return "Bienvenido, esta es una API para probar un modelo de machine learning"

# Endpoint de predicción

@app.get("/predict")
async def prediccion(TV: float, radio: float, newspaper: float):
   try:
        data_inversion = {'TV': TV, 'radio': radio, 'newspaper': newspaper}

        input = pd.DataFrame([data_inversion])
        prediction = model.predict(input)
        return {"Prediction": prediction[0]}

   except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint de ingesta de datos

@app.post("/add_data")
async def add_data(TV,radio, newspaper, sales):
    try:
        cursor.execute('''INSERT INTO advertising_clean (TV, radio, newspaper, sales) 
                        VALUES (?,?,?,?)''', (TV,radio,newspaper,sales))
        conn.commit()
        return "Datos ingresados"
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint de reentramiento del modelo

@app.post("/retrain")
async def retrain():
    try:
        df = pd.read_sql_query("SELECT * FROM advertising_clean", conn)

    
        X = df[['TV', 'radio', 'newspaper']]  
        y = df['sales']  
        model.fit(X, y)
        with open(model_path, 'wb') as model_file:
            pickle.dump(model, model_file)
        return "Modelo reentrenado!"

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Fin

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)