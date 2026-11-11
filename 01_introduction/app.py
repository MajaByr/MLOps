from fastapi import FastAPI
from api.models.text_model import PredictRequest, PredictResponse
from sentence_transformers import SentenceTransformer
import joblib


app = FastAPI()

transformer = SentenceTransformer("./model/sentence_transformer.model")
classifier = joblib.load("./model/classifier.joblib")


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API (H)"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    embedding = transformer.encode([request.text])
    prediction = classifier.predict(embedding)[0]
    return PredictResponse(prediction=str(prediction))
