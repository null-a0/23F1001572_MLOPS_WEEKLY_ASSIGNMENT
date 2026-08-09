import mlflow
import mlflow.sklearn
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

np.random.seed(42)


def poison_dataset(X, y, poison_percent):
    X_poison = X.copy()
    y_poison = y.copy()

    n_samples = len(X)
    n_poison = int(n_samples * poison_percent)

    indices = np.random.choice(
        n_samples,
        n_poison,
        replace=False
    )

    for idx in indices:
        X_poison[idx] = np.random.uniform(
            low=X.min(axis=0),
            high=X.max(axis=0),
            size=4
        )

        y_poison[idx] = np.random.randint(0, 3)

    return X_poison, y_poison


iris = load_iris()

X = iris.data
y = iris.target

poison_levels = [0, 5, 10, 50]

mlflow.set_experiment("IRIS_MLSecOps")

for level in poison_levels:

    X_poison, y_poison = poison_dataset(
        X,
        y,
        level / 100
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X_poison,
        y_poison,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    accuracy = accuracy_score(y_test, preds)
    precision = precision_score(
        y_test,
        preds,
        average="weighted"
    )
    recall = recall_score(
        y_test,
        preds,
        average="weighted"
    )
    f1 = f1_score(
        y_test,
        preds,
        average="weighted"
    )

    with mlflow.start_run(
        run_name=f"poison_{level}"
    ):

        mlflow.log_param(
            "poisoning_level",
            level
        )

        mlflow.log_metric(
            "accuracy",
            accuracy
        )

        mlflow.log_metric(
            "precision",
            precision
        )

        mlflow.log_metric(
            "recall",
            recall
        )

        mlflow.log_metric(
            "f1_score",
            f1
        )

        mlflow.sklearn.log_model(
            model,
            f"model_{level}"
        )

        print(
            f"Poison={level}% | "
            f"Accuracy={accuracy:.4f} | "
            f"Precision={precision:.4f} | "
            f"Recall={recall:.4f} | "
            f"F1={f1:.4f}"
        )