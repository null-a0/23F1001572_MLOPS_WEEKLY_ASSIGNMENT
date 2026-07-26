---
# Week 6 - Deploying an Iris Classification API on Google Kubernetes Engine (GKE)

## Assignment Tasks

Repository: **23F1001572_MLOPS_WEEKLY_ASSIGNMENT**  
Branch: **week_6**

## Task 1 – Explain Pod vs Container ✅

A **Docker Container** is the smallest runnable unit that packages an application together with its dependencies and runtime environment.

A **Kubernetes Pod** is the smallest deployable unit in Kubernetes. A Pod can contain one or more containers that share the same network namespace, storage volumes, and lifecycle.

### Difference

| Docker Container | Kubernetes Pod |
|------------------|----------------|
| Runs a single application process | Groups one or more containers |
| Managed by Docker | Managed by Kubernetes |
| Has its own filesystem | Containers inside a Pod share networking and storage |
| Cannot scale itself | Pods are replicated and managed by Deployments |

### Why Kubernetes Uses Pods

Kubernetes schedules Pods instead of individual containers because multiple tightly coupled containers (for example, an application container and a logging sidecar) often need to communicate using localhost, share storage, and be managed as a single unit.

---

## Task 2 – Dockerize the IRIS API ✅

A Dockerfile was created to package the IRIS FastAPI application.

The Docker image includes:

- FastAPI application
- Trained model (`model.joblib`)
- Python dependencies
- Uvicorn server

The application listens on **port 8000** inside the container.

---

## Task 3 – Setup GCP Service Account ✅

A Google Cloud Service Account was configured with the required permissions to:

- Push Docker images to Google Artifact Registry
- Deploy workloads to Google Kubernetes Engine (GKE)

The service account credentials were configured for deployment.

---

## Task 4 – Build & Push Docker Image ✅

The Docker image was:

- Built from the Dockerfile
- Tagged appropriately
- Pushed to Google Artifact Registry

Artifact Registry stores the versioned container image used during deployment.

---

## Task 5 – Deploy to Google Kubernetes Engine ✅

The application was deployed using Kubernetes.

Deployment included:

- Kubernetes Deployment
- Kubernetes Service
- LoadBalancer Service
- Public External IP

The deployed API successfully serves predictions through the public endpoint.

Example:

```
GET /
```

Response

```json
{
  "message": "Welcome to the Iris Classifier API!"
}
```

Prediction

```
POST /predict/
```

```json
{
    "predicted_class": 0
}
```

---

## Task 6 – MLflow Model in Container (Optional)

**Not Implemented**

The optional task required fetching the best model from the MLflow Model Registry during Docker image creation and packaging it inside the container.

This assignment was completed without implementing the optional MLflow integration.
