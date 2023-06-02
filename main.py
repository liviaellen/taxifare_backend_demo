from fastapi import FastAPI


app=FastAPI()


@app.get("/")
def home():
    return {"message":"This is for testing, please go to docs for more info"}

@app.get("/prep_predict")
def predict():
    pred=0
    return {"prediction":pred}
