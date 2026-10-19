import pytest
from fastapi.testclient import TestClient
from api.models.text_model import PredictRequest, PredictResponse
from sentence_transformers import SentenceTransformer
import joblib
from app import app

client = TestClient(app)

transformer = SentenceTransformer("./model/sentence_transformer.model")
classifier = joblib.load("./model/classifier.joblib")


def test_input_validation():
    with pytest.raises(ValueError):
        PredictRequest(text="")


def test_inference():
    response = client.post("/predict", json={"text": "Lorem ipsum"})

    assert response.status_code == 200
    assert response.json()["prediction"] == str(1)


def test_response_validation():
    response = client.post(
        "/predict",
        json={"text": "This is a test."},
    )

    assert response.status_code == 200
    assert PredictResponse.model_validate(response.json())


def test_invalid_input_returns_json_error():
    response = client.post("/predict", json={"text": ""})

    assert response.status_code == 422
    data = response.json()
    assert "detail" in data
    assert isinstance(data["detail"], list)
