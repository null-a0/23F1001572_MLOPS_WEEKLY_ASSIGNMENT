# Week 7 – MLOps Deployment, Stress Testing & Autoscaling on GKE

This repository contains the Week 7 MLOps assignment demonstrating deployment of a FastAPI-based ML inference service on **Google Kubernetes Engine (GKE)** with Docker, Kubernetes, Horizontal Pod Autoscaler (HPA), Cloud Monitoring, Cloud Logging, and GitHub Actions CI/CD.

---

## Features

- FastAPI ML Inference API
- Docker Containerization
- Google Kubernetes Engine (GKE)
- Kubernetes Deployment & LoadBalancer Service
- Liveness & Readiness Probes
- Horizontal Pod Autoscaler (HPA)
- Google Cloud Monitoring
- Google Cloud Logging
- GitHub Actions CI/CD
- Stress Testing using `wrk`

---

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   ├── test_data.py
│   └── test_model.py
├── Dockerfile
├── .dockerignore
├── demo_log.py
├── deployment.yaml
├── service.yaml
├── hpa.yaml
├── post.lua
├── requirements.txt
└── README.md
```

---

# Assignment Tasks

## Task 1 – CI/CD Workflow with Stress Testing

The GitHub Actions workflow performs:

- Checkout repository
- Authenticate to Google Cloud using Workload Identity Federation (OIDC)
- Configure Google Cloud SDK
- Build Docker image
- Push image to Artifact Registry
- Update Kubernetes deployment
- Wait for rollout completion
- Install `wrk`
- Execute stress test
- Display HPA status
- Display Pod status

Workflow file:

```
.github/workflows/ci.yml
```

---

## Task 2 – Stress Testing

Install `wrk`

```bash
sudo apt update
sudo apt install wrk
```

Run stress test:

```bash
wrk -t4 -c1000 -d30s --latency \
-s post.lua \
http://<EXTERNAL_IP>/predict
```

This generates more than **1000 concurrent connections** and reports:

- Requests/sec
- Average latency
- Latency percentiles
- Error count

---

## Task 3 – Horizontal Pod Autoscaler

Deploy the application:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

Check deployment:

```bash
kubectl get pods
kubectl get svc
kubectl get hpa
```

HPA Configuration:

- Minimum Replicas: **1**
- Maximum Replicas: **3**
- CPU Target: **60%**

Monitor autoscaling while running `wrk`:

```bash
kubectl get pods -w
```

```bash
kubectl get hpa
```

```bash
kubectl top pods
```

---

## Task 4 – Cloud Monitoring & Cloud Logging

### Cloud Monitoring

Open:

```
Google Cloud Console
→ Monitoring
→ Dashboards
→ Kubernetes
→ Workloads
```

Monitor:

- CPU Usage
- Memory Usage
- Pod Replicas

### Cloud Logging

Open:

```
Google Cloud Console
→ Logging
→ Logs Explorer
```

Query:

```
resource.type="k8s_container"
resource.labels.container_name="fastapi-container"
```

The application logs include:

- Trace ID
- Prediction
- Confidence
- Latency
- Request Status

---

## Task 5 – Bottleneck Analysis

Restrict autoscaling:

```yaml
maxReplicas: 1
```

Run stress test with higher concurrency:

```bash
wrk -t4 -c2000 -d30s --latency \
-s post.lua \
http://<EXTERNAL_IP>/predict
```

Compare the following scenarios:

| Scenario | Configuration |
|----------|---------------|
| Scenario 1 | maxReplicas = 3, 1000 concurrent connections |
| Scenario 2 | maxReplicas = 1, 2000 concurrent connections |

Observe:

- Requests/sec
- Latency
- Error Rate
- CPU Utilization
- Pod Scaling

---

# Deployment Steps

### Build Docker Image

```bash
docker build -t demo-log:v3 .
```

### Push Image

```bash
docker tag demo-log:v3 \
us-central1-docker.pkg.dev/<PROJECT_ID>/week6-repo/demo-log:v3

docker push \
us-central1-docker.pkg.dev/<PROJECT_ID>/week6-repo/demo-log:v3
```

### Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

Verify:

```bash
kubectl get deployments
kubectl get pods
kubectl get svc
kubectl get hpa
```

---

# API Endpoints

### Liveness Probe

```http
GET /live_check
```

```bash
curl http://<EXTERNAL_IP>/live_check
```

---

### Readiness Probe

```http
GET /ready_check
```

```bash
curl http://<EXTERNAL_IP>/ready_check
```

---

### Prediction

```http
POST /predict
```

Example:

```bash
curl -X POST http://<EXTERNAL_IP>/predict \
-H "Content-Type: application/json" \
-d '{"feature1":10,"feature2":20}'
```

---

# Technologies Used

- Python
- FastAPI
- Docker
- Kubernetes
- Google Kubernetes Engine (GKE)
- Google Artifact Registry
- Google Cloud Monitoring
- Google Cloud Logging
- GitHub Actions
- Workload Identity Federation (OIDC)
- Horizontal Pod Autoscaler (HPA)
- wrk

---

# Outcome

This project demonstrates:

- Containerization of a FastAPI application
- Deployment on Google Kubernetes Engine
- Health monitoring using Liveness and Readiness Probes
- Automatic scaling using Horizontal Pod Autoscaler
- Stress testing with `wrk`
- Monitoring using Google Cloud Monitoring
- Structured logging using Google Cloud Logging
- Automated deployment through GitHub Actions CI/CD
