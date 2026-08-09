# Week 8 – MLSecOps: Data Poisoning on IRIS Dataset

## Objective

This assignment explores MLSecOps concepts by simulating data poisoning attacks on the IRIS dataset and measuring their impact on model performance using MLflow.

---

## Tasks Completed

### Task 1: ML Threat Vectors
Studied and explained:

- Data Poisoning
- Adversarial Examples
- Model Extraction
- Prompt Injection

### Task 2: Data Poisoning
Created poisoned versions of the IRIS dataset with:

- 0% (Clean Dataset)
- 5% Poisoning
- 10% Poisoning
- 50% Poisoning

Poisoned samples were replaced with:
- Random feature values
- Random class labels

### Task 3: MLflow Experiment Tracking
For each poisoning level:

- Trained a Random Forest Classifier
- Logged experiments in MLflow
- Recorded:
  - Accuracy
  - Precision
  - Recall
  - F1 Score

### Task 4: Analysis

| Poisoning Level | Accuracy | F1 Score |
|----------------|----------|----------|
| 0% | 1.0000 | 1.0000 |
| 5% | 0.9667 | 0.9665 |
| 10% | 0.9667 | 0.9668 |
| 50% | 0.7000 | 0.6930 |

Observations:

- Model performance starts degrading at 5–10% poisoning.
- Significant degradation occurs at 50% poisoning.
- The model still learns some patterns at 50% corruption but performance drops substantially.

### Task 5: Mitigation Strategies

Recommended defenses:

- Data validation and schema checks
- Statistical anomaly detection
- Data provenance tracking
- Quality gates before training
- Dataset versioning and auditing

Key Insight:

Increasing data quantity does not solve poisoning issues if data quality is compromised. Maintaining a high ratio of clean data is critical for reliable model training.

---

## Project Structure

```
week_8/
├── mlsecops_iris.py
└── README.md
```

---

## Execution

Run the experiment:

```bash
python mlsecops_iris.py
```

Start MLflow UI:

```bash
export MLFLOW_TRACKING_URI=sqlite:///mlflow.db

mlflow ui \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./mlruns \
--host 0.0.0.0 \
--port 5000 \
--allowed-hosts "*"
```

Open:

```text
http://<VM_EXTERNAL_IP>:5000
```

---

## Technologies Used

- Python
- Scikit-Learn
- MLflow
- SQLite
- Google Cloud Platform (GCP)

---

## Author

**Abhishek Saha**  
Roll No: **23F1001572**
