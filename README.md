# Week 3 - Feature Store with Feast

## Overview

This project demonstrates how to use **Feast**, an open-source Feature Store, to manage machine learning features for both training and online inference.

The IRIS dataset is used to build an end-to-end MLOps pipeline that includes:

- Data preparation
- Feature Store creation
- Historical feature retrieval
- Model training
- Online feature serving
- Real-time prediction

---

## Project Structure

```
.
├── data/
│   ├── iris.csv
│   ├── iris_feast.csv
│   └── iris_feast.parquet
│
├── feature_repo/
│   └── feature_repo/
│       ├── feature_definitions.py
│       └── feature_store.yaml
│
├── models/
│   └── iris_model.pkl
│
├── week_3.ipynb
├── train.py
└── README.md
```

---

## Technologies Used

- Python
- Feast 0.64
- Pandas
- PyArrow
- Scikit-learn
- DVC
- Git & GitHub

---

## Workflow

1. Load the IRIS dataset.
2. Prepare the dataset for Feast.
3. Save the dataset as CSV and Parquet.
4. Create a Feast Feature Repository.
5. Register Feature Views using `feast apply`.
6. Materialize features into the online store.
7. Retrieve historical features for model training.
8. Train a Random Forest classifier.
9. Save the trained model.
10. Retrieve online features from Feast.
11. Perform real-time prediction.

---

## Model Performance

| Metric | Value |
|---------|-------|
| Model | Random Forest Classifier |
| Accuracy | **100%** |

---

## Running the Project

### Apply Feast Configuration

```bash
cd feature_repo/feature_repo
feast apply
```

### Materialize Features

```bash
feast materialize 2026-07-01T00:00:00 2026-12-31T00:00:00
```

### Run the Notebook

Open:

```
week_3.ipynb
```

and execute all cells sequentially.

---

## Sample Output

```
Model Accuracy: 1.0000

Predicted Species: setosa
```

---

## Learning Outcomes

This project demonstrates:

- Feature Store concepts
- Offline and Online Feature Stores
- Historical Feature Retrieval
- Online Feature Retrieval
- Training-Serving Consistency
- End-to-End MLOps Workflow using Feast

---

## Author

**Abhishek Saha**

BS in Data Science and Applications  
Indian Institute of Technology Madras
