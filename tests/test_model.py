import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score

MODEL_PATH = "models/iris_model.pkl"
DATA_PATH = "data/iris_data_adapted_for_feast.csv"


def test_model_performance():
    # Load model
    model = joblib.load(MODEL_PATH)

    # Load evaluation data
    df = pd.read_csv(DATA_PATH)

    # Features
    X = df[
        [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
        ]
    ]

    # Target
    y = df["species"]

    # Prediction
    predictions = model.predict(X)

    # Metrics
    accuracy = accuracy_score(y, predictions)

    precision = precision_score(
        y,
        predictions,
        average="weighted",
        zero_division=0,
    )

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")

    # Quality gates
    assert accuracy >= 0.90, f"Accuracy too low: {accuracy:.4f}"
    assert precision >= 0.90, f"Precision too low: {precision:.4f}"