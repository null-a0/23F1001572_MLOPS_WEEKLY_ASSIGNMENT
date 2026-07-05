# MLOps Graded Assignment – Week 3


## Overview

This assignment demonstrates the integration of the **Feast Feature Store** into an existing Iris machine learning pipeline. The objective is to use Feast for both offline feature retrieval during training and online feature retrieval during inference, ensuring consistency between training and serving.

---

## Project Structure

```
.
├── data/
│   ├── iris_data_adapted_for_feast.csv
│   └── iris_data_adapted_for_feast.parquet
│
├── feature_repo/
│   ├── README.md
│   └── feature_repo/
│       ├── feature_definitions.py
│       ├── feature_store.yaml
│       └── data/
│           ├── registry.db
│           └── online_store.db
│
├── models/
│   └── iris_model.pkl
│
├── week3.ipynb
├── README.md
└── .gitignore
```

---

## Tasks Completed

### ✅ Task 1 – Initialize Feast Feature Repository

- Created a Feast Feature Repository.
- Configured Feast with the Local Provider.
- Configured SQLite as the Online Store.

---

### ✅ Task 2 – Define Entity, Data Source and Feature View

Defined:

- **Entity:** `iris`
- **Entity Key:** `iris_id`
- **Data Source:** Time-aware Iris Dataset
- **Feature View:** `iris_features`

Features stored:

- sepal_length
- sepal_width
- petal_length
- petal_width

---

### ✅ Task 3 – Apply Definitions and Materialize Features

Successfully executed:

```bash
feast apply
```

and

```bash
feast materialize 2025-09-01T00:00:00 2025-12-31T00:00:00
```

to register feature definitions and populate the online store.

---

### ✅ Task 4 – Offline Feature Retrieval & Model Training

- Retrieved historical features using the Feast Offline Store.
- Built the training dataset using Feast instead of directly reading the feature columns.
- Trained a Random Forest classifier.
- Saved the trained model as:

```
models/iris_model.pkl
```

---

### ✅ Task 5 – Online Feature Retrieval & Inference

Retrieved real-time features from the Feast Online Store using `iris_id` and performed inference with the trained model.

The prediction obtained using Feast matched the prediction obtained using the raw dataset, demonstrating consistency between training and serving.

Example output:

```
Prediction using Feast : setosa
Prediction using Raw Data : setosa

Predictions are consistent.
```

---

## Technologies Used

- Python
- Feast 0.64
- Pandas
- Scikit-learn
- SQLite
- PyArrow
- Jupyter Notebook

---

## Repository

Branch used for this assignment:

```
week_3
```

---

## Conclusion

This project demonstrates the complete workflow of integrating a Feature Store into a machine learning pipeline. Feast was successfully used for feature management, offline training, and online inference, ensuring consistent feature access across different stages of the ML lifecycle.
