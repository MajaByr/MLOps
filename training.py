from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib


def load_data():
    return load_iris(return_X_y=True)


def train_model(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model


def save_model(model, filename="iris_classifier.joblib"):
    joblib.dump(model, filename)


if __name__ == "__main__":
    X, y = load_data()
    model = train_model(X, y)
    save_model(model)
