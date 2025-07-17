
import numpy as np
import pandas as pd  
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from tensorflow.keras.models import load_model
app=FastAPI()
model=load_model('model.h5')
with open('stander.pkl','rb') as f:
    stand=pickle.load(f)

class model_select(BaseModel):
    MedInc:float
    HouseAge:float
    AveRooms:float    
    AveBedrms:float  
    Population:float  
    AveOccup:float     
    Latitude:float     
    Longitude:float     

@app.get('/')
def welcome():
    return {'meassage':'welcome to House price Prediction'}

@app.post('/price')
def predict_model(data:model_select):
    arr=np.array([[data.MedInc,data.HouseAge,data.AveRooms,data.AveBedrms,data.Population,data.AveOccup,data.Latitude,data.Longitude]])
    stander=stand.transform(arr)
    model_price=model.predict(stander)
    USD_PRICE=float(model_price[0][0])*1_00_00 #this us ruppes
    INR_PRICE=round(USD_PRICE*83) #this is INR
    return {'House price':f"₹{INR_PRICE:,}"}
    