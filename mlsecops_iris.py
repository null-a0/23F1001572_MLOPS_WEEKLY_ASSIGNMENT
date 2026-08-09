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
    f1_score,
)

# =====================================
# MLflow Configuration
# =====================================

mlflow.set_tracking_uri("sqlite:///mlflow.db")

experiment_name = "IRIS_MLSecOps"

try:
    experiment_id = mlflow.create_experiment(experiment_name)
except Exception:
    experiment = mlflow.get_experiment_by_name(experiment_name)
    experiment_id = experiment.experiment_id

mlflow.set_experiment(experiment_name)

np.random.seed(42)

# =====================================
# Data Poisoning Function
# =====================================

def poison_dataset(X, y, poison_percent):

    X_poison = X.copy()
    y_poison = y.copy()

    n_samples = len(X)
    n_poison = int(n_samples * poison_percent)

    poison_indices = np.random.choice(
        n_samples,
        n_poison,
        replace=False
    )

    for idx in poison_indices:

        X_poison[idx] = np.random.uniform(
            low=X.min(axis=0),
            high=X.max(axis=0),
            size=X.shape[1]
        )

        y_poison[idx] = np.random.randint(
            0,
            len(np.unique(y))
        )

    return X_poison, y_poison


# =====================================
# Load Dataset
# =====================================

iris = load_iris()

X = iris.data
y = iris.target

poison_levels = [0, 5, 10, 50]

print("\n========== MLSecOps Experiment ==========\n")

# =====================================
# Training Loop
# =====================================

for level in poison_levels:

    print(f"\nRunning Experiment: {level}% Poisoning")

    X_poison, y_poison = poison_dataset(
        X,
        y,
        level / 100
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X_poison,
        y_poison,
        test_size=0.2,
        random_state=42,
        stratify=y_poison
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    precision = precision_score(
        y_test,
        predictions,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    with mlflow.start_run(
        run_name=f"poison_{level}"
    ):

        # Parameters
        mlflow.log_param(
            "poisoning_level",
            level
        )

        # Metrics
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

        # Model Artifact
        mlflow.sklearn.log_model(
            sk_model=model,
            name=f"iris_model_{level}"
        )

        print(
            f"Poison={level}% | "
            f"Accuracy={accuracy:.4f} | "
            f"Precision={precision:.4f} | "
            f"Recall={recall:.4f} | "
            f"F1={f1:.4f}"
        )

print("\n========== Experiment Complete ==========")
print("Results logged to MLflow successfully.")