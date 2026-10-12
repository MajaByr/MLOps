import joblib
import pandas as pd
from sklearn.datasets import load_iris


def load_model(filename="iris_classifier.joblib"):
    return joblib.load(filename)


def predict(model, data: dict) -> str:
    df = pd.DataFrame([data])
    prediction_idx = model.predict(df)[0]

    iris = load_iris()
    return iris.target_names[prediction_idx]
