from sentence_transformers import SentenceTransformer
import joblib
from pathlib import Path


def test_model_paths():
    assert Path("model/sentence_transformer.model").exists()
    assert Path("model/classifier.joblib").exists()


def test_model_loading():
    transformer = SentenceTransformer("model/sentence_transformer.model")
    classifier = joblib.load("model/classifier.joblib")

    assert transformer is not None
    assert classifier is not None


def test_inference():
    transformer = SentenceTransformer("model/sentence_transformer.model")
    classifier = joblib.load("model/classifier.joblib")

    texts = [
        "Tuna loops are awful!",
        "Lorem ipsum",
        "What a great MLOps lecture, I am very satisfied",
    ]

    for sentiment, text in enumerate(texts):
        embedding = transformer.encode([text])
        prediction = classifier.predict(embedding)[0]
        assert str(prediction) == str(sentiment)
