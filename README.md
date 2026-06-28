# 23F1001572_MLOPS_WEEKELY_ASSIGNMENT
# IRIS Classification with DVC (Week 2 – MLOps Assignment)

## Project Overview

This project demonstrates how **Data Version Control (DVC)** can be integrated into a machine learning workflow to version datasets and model artifacts separately from Git.

The project uses the **IRIS dataset** and a **Random Forest Classifier**. Dataset versions and trained models are tracked using DVC, while the actual files are stored in a **Google Cloud Storage (GCS)** remote.

---

## Repository Structure

```
.
├── train.py
├── README.md
├── data/
│   ├── iris.csv.dvc
│   └── .gitignore
├── models/
│   ├── model.joblib.dvc
│   └── .gitignore
├── .dvc/
├── .dvcignore
└── .gitignore
```

---

## Files Description

### train.py

Python script used to:

* Load the IRIS dataset
* Train a Random Forest Classifier
* Save the trained model as `models/model.joblib`

### data/

Contains the DVC pointer file for the dataset.

* `iris.csv.dvc` – DVC metadata pointing to the versioned dataset stored in the configured GCS remote.

### models/

Contains the DVC pointer file for the trained model.

* `model.joblib.dvc` – DVC metadata pointing to the trained model stored in the configured GCS remote.

### .dvc/

Contains DVC configuration and remote storage configuration.

---

## DVC Workflow

### Train the model

```bash
python train.py
```

### Track dataset and model

```bash
dvc add data/iris.csv
dvc add models/model.joblib
```

### Upload tracked files to GCS

```bash
dvc push
```

### Restore files from DVC

```bash
dvc pull
```

### Switch between versions

```bash
git checkout <tag_or_commit>
dvc checkout
```

---

## Version History

Three versions were created during this assignment:

* **v1.0** – Initial dataset and trained model
* **v2.0** – Augmented dataset and retrained model
* **v3.0** – Further augmented dataset and retrained model

---

## Remote Storage

DVC Remote: **Google Cloud Storage (GCS)**

All datasets and trained model artifacts are stored in the configured GCS bucket, while Git stores only lightweight DVC pointer files.

---

## Technologies Used

* Python
* Scikit-learn
* Pandas
* Joblib
* Git
* DVC
* Google Cloud Storage (GCS)
