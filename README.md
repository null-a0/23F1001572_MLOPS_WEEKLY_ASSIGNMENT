
# Week 9 — Explainability, Fairness, and Drift in the IRIS Pipeline

## Overview

This assignment extends the IRIS classification pipeline with responsible machine learning practices. The main focus is on:

- Fairness evaluation using Fairlearn
- Model explainability using SHAP
- Data drift detection
- ML governance and model documentation

The implementation follows the Week 9 starter notebook methodology and adds the fairness and governance requirements specified in the assignment.

---

## Dataset

The standard Iris dataset from `scikit-learn` is used.

- **Samples:** 150
- **Features:** 4
- **Classes:** 3

### Features

- Sepal length
- Sepal width
- Petal length
- Petal width

### Classes

- Setosa
- Versicolor
- Virginica

---

## Model

A `DecisionTreeClassifier` is used as the classification model.

```python
DecisionTreeClassifier(
    max_depth=4,
    random_state=1
)
````

The model is trained using only the four original Iris features.

---

# Task 1 — Introduce the Location Attribute

A synthetic `location` attribute is randomly assigned to every Iris sample with values `0` or `1`.

The `location` attribute is **not used as a training feature**. It is used exclusively as a sensitive attribute for fairness evaluation.

### Training Features

```text
sepal length (cm)
sepal width (cm)
petal length (cm)
petal width (cm)
```

### Sensitive Attribute

```text
location
```

This separation ensures that the sensitive attribute does not directly influence model training.

---

# Task 2 — Fairness Evaluation with Fairlearn

Fairlearn's `MetricFrame` is used to evaluate model performance separately for the two location groups.

The following metrics are evaluated:

* Accuracy
* Precision
* Recall

## Overall Model Performance

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 0.9333 |
| Precision | 0.9333 |
| Recall    | 0.9333 |
| F1 Score  | 0.9333 |

## Performance by Location

| Location | Accuracy | Precision | Recall |
| -------- | -------: | --------: | -----: |
| 0        |   0.9286 |    0.9429 | 0.9286 |
| 1        |   0.9375 |    0.9531 | 0.9375 |

The differences between the two groups are small:

* Accuracy difference: approximately 0.9 percentage points
* Precision difference: approximately 1.0 percentage point
* Recall difference: approximately 0.9 percentage points

Since the location attribute was randomly assigned and excluded from model training, these small differences are interpreted as sampling variation rather than evidence of systematic discrimination.

---

# Task 3 — SHAP Explainability

SHAP is used to explain the Decision Tree classifier.

A full-dataset SHAP explainer is used to generate explanations for:

* All 150 Iris samples
* All 4 features
* All 3 classes

The resulting SHAP value structure is:

```text
(150, 4, 3)
```

Summary plots are generated for:

1. Setosa
2. Versicolor
3. Virginica

## Virginica Interpretation

The Virginica SHAP summary plot is used for detailed interpretation.

* A positive SHAP value pushes the prediction toward Virginica.
* A negative SHAP value pushes the prediction away from Virginica.
* Red points represent high feature values.
* Blue points represent low feature values.
* Points further to the right have stronger positive contributions.
* Points further to the left have stronger negative contributions.

The SHAP features are ranked according to their overall contribution to the model's predictions.

---

# Task 4 — Data Drift Detection

A simulated production dataset is created from the training/reference data.

The distributions of:

* `petal length (cm)`
* `petal width (cm)`

are deliberately shifted to simulate production data drift.

The reference and production distributions are compared using distribution plots and the Kolmogorov-Smirnov (KS) statistical test.

A p-value below `0.05` is considered evidence of statistically significant drift.

## Drift Results

| Feature      |  p-value | Result               |
| ------------ | -------: | -------------------- |
| Sepal length | 1.000000 | No significant drift |
| Sepal width  | 1.000000 | No significant drift |
| Petal length | 0.000003 | Drift detected       |
| Petal width  | 0.000212 | Drift detected       |

### Interpretation

Significant drift was detected in petal length and petal width.

This means that the simulated production input distribution differs from the reference training distribution for these features.

In a real production environment, this would be an early warning signal that the model is receiving data different from the data on which it was trained. Further investigation and model-performance monitoring would therefore be required.

This experiment demonstrates **data drift**, not concept drift.

* **Data drift:** the distribution of input features changes.
* **Concept drift:** the relationship between the input features and target changes.

---

# Task 5 — Model Card

A Model Card is included in the notebook to document:

* Model details
* Intended use
* Training data
* Overall performance
* Fairness results
* SHAP explainability
* Drift monitoring
* Limitations
* Governance considerations

The model is intended for educational demonstration of responsible ML practices and is not intended for high-stakes or safety-critical decisions.

---

## Responsible ML Pipeline

```text
Iris Dataset
     |
     v
Add Synthetic Location
     |
     +--------------------+
     |                    |
     v                    v
Model Training       Fairness Audit
     |                (Fairlearn)
     |
     +--------------------+
     |                    |
     v                    v
Model Predictions      SHAP
     |               Explainability
     |
     v
Production Simulation
     |
     v
Drift Detection
     |
     v
Model Card / Governance
```

---

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Fairlearn
* SHAP
* SciPy
* Matplotlib
* Jupyter Notebook

---

## Project Files

```text
.
├── Iris detection with governance.ipynb
├── README.md
└── requirements.txt
```

The main implementation and experiment results are contained in:

```text
Iris detection with governance.ipynb
```

---

## Conclusion

This assignment demonstrates that model quality should not be evaluated only through overall accuracy.

The completed pipeline combines:

* **Fairness** — evaluating performance across sensitive groups
* **Explainability** — understanding feature contributions using SHAP
* **Monitoring** — detecting changes in production data
* **Governance** — documenting intended use, limitations, and model behavior

Together, these practices provide a foundation for building more trustworthy and responsible machine learning systems.

