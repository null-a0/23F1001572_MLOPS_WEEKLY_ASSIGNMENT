# Week 10 — From MLOps to LLMOps: Fine-Tuning Gemini on the IRIS Pipeline

**Course:** MLOps  
**Platform:** Google Cloud Platform (GCP)  
**Model Platform:** Vertex AI  
**Task:** Supervised Fine-Tuning and Evaluation of Gemini  
**Dataset:** IRIS Classification  
**Branch:** `week_10`

---

# 1. Assignment Overview

This project implements **Week 10 — From MLOps to LLMOps: Fine-Tuning Gemini on the IRIS Pipeline**.

The objective is to apply LLMOps principles using **Google Cloud Platform (GCP), Google Cloud Storage (GCS), and Vertex AI**.

The experiment compares two representations of the same IRIS dataset:

- **V1 — Raw Feature Representation:** IRIS measurements provided directly as text.
- **V2 — Natural Language Representation:** The same measurements expressed as natural-language descriptions.

Both datasets are used to fine-tune Gemini models with the same training configuration. The resulting models are evaluated on held-out test data using accuracy, per-class precision and recall, and format compliance.

The project demonstrates how **data representation, supervised fine-tuning, model versioning, and LLM-specific evaluation** fit into an LLMOps workflow.

# 2. Learning Objectives

- Understand the transition from **MLOps to LLMOps**.
- Convert structured IRIS data into **LLM-compatible JSONL datasets**.
- Create and compare **raw-feature and natural-language representations**.
- Perform **supervised Gemini fine-tuning using Vertex AI**.
- Evaluate fine-tuned models using **accuracy, precision, and recall**.
- Measure **LLM output-format compliance**.
- Compare model versions and analyze the impact of data representation.
- Understand the role of **versioning, evaluation, and CI/CD** in LLMOps.

## 3. Assignment Tasks

### Task 1 — V1 Raw Feature Format
Completed. Created and uploaded the raw-feature JSONL dataset to GCS.

### Task 2 — V2 Natural Language Format
Completed. Created and uploaded the natural-language JSONL dataset to GCS.

### Task 3 — Gemini Fine-Tuning
Completed. Successfully fine-tuned two Gemini model versions using the V1 and V2 datasets.

### Task 4 — Evaluation & Comparison
Completed. Evaluated both models using accuracy, per-class precision/recall, and format compliance.

### Task 5 — Automated Evaluation in CI
**Optional.** Not implemented, as this is an optional extension of the assignment.
