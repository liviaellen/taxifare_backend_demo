from fastapi import FastAPI
import pandas as pd
from calculate import *


app=FastAPI()
app.state.model=load_model()

@app.get("/")
def home():
    return {"message":"This is for testing, please go to docs for more info"}

@app.get("/prep_predict")
def predict(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count):
    X_new = pd.DataFrame(dict(
    pickup_datetime=[pd.Timestamp(pickup_datetime, tz='UTC')],
    pickup_longitude=[pickup_latitude],
    pickup_latitude=[dropoff_longitude],
    dropoff_longitude=[dropoff_longitude],
    dropoff_latitude=[dropoff_latitude],
    passenger_count=[passenger_count],
    ))
    X_new_clean=prep_data(X_new)
    model=app.state.model
    pred=model.predict(X_new_clean)[0]
    print(pred)



    pred=0
    return {"prediction":pred}
