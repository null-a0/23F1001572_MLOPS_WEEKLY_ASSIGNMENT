# 23F1001572_MLOPS_WEEKLY_ASSIGNMENT

# MLOps Graded Assignment – Week 4

## Overview

This assignment extends the Iris MLOps pipeline by integrating **Continuous Integration (CI)** using **GitHub Actions**. The pipeline automatically validates data quality, evaluates the trained model, and executes tests on every push and pull request. DVC configuration is included for version-controlled data and model management, providing the foundation for reproducible machine learning workflows.

---

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dvc/
├── data/
│   └── iris_data_adapted_for_feast.csv
├── feature_repo/
├── models/
│   └── iris_model.pkl
├── tests/
│   ├── test_data.py
│   └── test_model.py
├── requirements.txt
├── week3.ipynb
└── README.md
```

---

## Tasks Completed

### ✅ Task 1 – Data Validation Tests

Implemented automated data validation using **pytest**.

Validation checks include:

- Dataset availability
- Expected schema
- Missing values
- Feature data types
- Valid feature value ranges
- Valid target classes

---

### ✅ Task 2 – Model Evaluation Tests

Implemented automated model evaluation tests.

The workflow:

- Loads the trained Random Forest model
- Performs inference on the evaluation dataset
- Computes evaluation metrics
- Verifies that model quality meets the required threshold

---

### ✅ Task 3 – GitHub Actions CI Pipeline

Configured GitHub Actions to automatically:

- Checkout repository
- Setup Python
- Install project dependencies
- Execute automated test suite

---

### ✅ Task 4 – Continuous Integration

Configured workflow triggers for:

- Push
- Pull Request
- Manual execution (`workflow_dispatch`)

This ensures every code change is automatically validated before merging.

---

### ✅ Task 5 – Continuous Machine Learning (CML)

Integrated CML into the GitHub Actions workflow to generate automated CI reports and publish test results on Pull Requests.

---

### ✅ Task 6 – Pull Request Workflow

Created a Pull Request from the **week_4** branch into **main**.

GitHub Actions automatically executed the CI pipeline before merge, ensuring only validated code is merged.

---

## Technologies Used

- Python
- Git
- GitHub Actions
- Pytest
- DVC
- Feast
- Scikit-learn
- Pandas
- Joblib

---

## Branch

```
week_4
```

---

## Conclusion

This assignment demonstrates how Continuous Integration can be integrated into an MLOps workflow. Automated testing ensures data quality and model performance are continuously validated, while GitHub Actions provides reproducible execution of the CI pipeline for every code change.
