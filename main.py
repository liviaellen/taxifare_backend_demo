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
    pickup_longitude=[float(pickup_longitude)],
    pickup_latitude=[float(pickup_latitude)],
    dropoff_longitude=[float(dropoff_longitude)],
    dropoff_latitude=[float(dropoff_latitude)],
    passenger_count=[int(passenger_count)],
    ))
    print("shape size ", X_new.shape)

    X_new_clean=prep_data(X_new)
    if X_new_clean=="error input":
        return {"error":"input error"}
    else:
        model=app.state.model
        pred=model.predict(X_new_clean)[0][0]
        print(pred)
        return {"prediction":float(pred)}


# fast api can only return python built in data type
