# MLOps Weekly Assignment - Week 1

## Repository Details

* **Roll Number:** 23F1001572
* **Repository:** 23F1001572_MLOPS_WEEKLY_ASSIGNMENT
* **Branch:** week_1

---

## Objective

The objective of this assignment is to build an end-to-end IRIS classification pipeline on Google Cloud Platform (GCP) using Vertex AI Workbench and Google Cloud Storage (GCS).

The pipeline includes:

1. Setting up Vertex AI Workbench.
2. Storing training and evaluation data in GCS.
3. Training an IRIS classifier by fetching data from GCS.
4. Saving model artifacts in timestamped folders.
5. Running inference using a separate notebook.
6. Executing the pipeline multiple times and comparing results.

---

## Files in Repository

### 1. iris_training.ipynb

This notebook performs:

* Downloading training and evaluation data from GCS.
* Training a Random Forest classifier.
* Evaluating the model.
* Saving:

  * model.joblib
  * metrics.json
  * logs.txt
* Uploading artifacts to GCS in timestamped folders.

---

### 2. inference.ipynb

This notebook performs:

* Downloading trained models from GCS.
* Downloading evaluation data.
* Running inference.
* Computing:

  * Accuracy
  * Confusion Matrix
  * Classification Report

It also evaluates the model on:

* data/v1/data.csv
* data/v2/data.csv

and compares the results.

---

## GCS Bucket Structure

```text
gs://mlops-course-project-0a6400db-0297-4323-a8f/

data/

    raw/iris.csv

    train.csv

    eval.csv

    v1/data.csv

    v2/data.csv


artifacts/

    2026-06-23_15-08-49/

        eval.csv

        logs.txt

        metrics.json

        model.joblib


    2026-06-23_15-26-49/

        eval.csv

        logs.txt

        metrics.json

        model.joblib
```

---

## Results

### Evaluation Dataset

* Accuracy: **0.90**

### Optional Task 6

Comparison across different data versions:

| Dataset | Accuracy |
| ------- | -------- |
| V1      | 0.9703   |
| V2      | 1.0000   |

---

## Learnings

Through this assignment, I learned:

* Setting up and using Vertex AI Workbench.
* Managing datasets and artifacts using Google Cloud Storage.
* Building a reproducible ML pipeline.
* Separating training and inference workflows.
* Organizing artifacts using timestamped folders for experiment tracking.
