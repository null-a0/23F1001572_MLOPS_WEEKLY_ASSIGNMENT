# MLOps Week 5 Assignment – MLflow Integration

## Student Details

- **Name:** Abhishek Saha
- **Roll Number:** 23F1001572

---

# Objective

This assignment integrates **MLflow** into the Iris machine learning pipeline for experiment tracking, model logging, model registration, and model retrieval.

---

# Task 1: Hyperparameter Tuning

Implemented hyperparameter tuning for the Random Forest classifier.

Hyperparameters explored:

| n_estimators | max_depth |
|--------------|-----------|
| 50 | 3 |
| 50 | 5 |
| 100 | 3 |
| 100 | 5 |

Each combination is trained as a separate MLflow run.

---

# Task 2: MLflow Experiment Tracking

Integrated MLflow into the training pipeline.

For every run, the following information is logged:

### Parameters
- n_estimators
- max_depth

### Metrics
- Accuracy
- Precision
- Recall
- F1 Score

### Artifacts
- Trained Random Forest model

The trained model is also registered in the MLflow Model Registry as:

```
iris_random_forest
```

---

# Task 3: Experiment Comparison

Multiple training runs were executed with different hyperparameter combinations.

The MLflow Tracking UI can be used to compare:

- Hyperparameters
- Accuracy
- Precision
- Recall
- F1 Score

---

# Task 4: Remove Model Dependency from DVC

Model artifact tracking through DVC has been removed.

Instead,

- Models are stored in the MLflow Model Registry.
- DVC is no longer used for model versioning.

---

# Task 5: Load Model from MLflow Registry

The evaluation pipeline loads the latest registered model directly from the MLflow Model Registry.

Instead of loading a local model file, the model is loaded using:

```python
mlflow.sklearn.load_model(
    f"models:/iris_random_forest/latest"
)
```

---

# Task 6 (Optional)

Not implemented.

---

# Results

Best evaluation metrics obtained:

| Metric | Value |
|---------|---------|
| Accuracy | 0.9583 |
| Precision | 0.9630 |
| Recall | 0.9583 |
| F1 Score | 0.9582 |

---

# Repository Structure

```
.
├── week5.ipynb
├── README.md
├── requirements.txt
├── .gitignore
└── .github/
```

---

# Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Assignment

Run the notebook:

```
week5.ipynb
```

To launch the MLflow UI:

```bash
mlflow ui
```

---
