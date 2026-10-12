from fastapi import FastAPI
from inference import load_model
from api.models.iris import PredictRequest, PredictResponse

app = FastAPI()
model = load_model("iris_classifier.joblib")


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    prediction = model.predict(request.model_dump())
    return PredictResponse(prediction=prediction)
