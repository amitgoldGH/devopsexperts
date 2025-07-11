# Flask App with Docker & Kubernetes (Part 2 of the course project)

This is a simple Flask web application that demonstrates how to use environment variables through Kubernetes ConfigMaps and Secrets. It includes health endpoints for liveness and readiness probes.

## 🧰 Features

- Returns a welcome message and API key from environment variables
- Health endpoints for Kubernetes:
  - `/health/live`
  - `/health/ready`
- Dockerized and ready to deploy in Kubernetes
- Uses ConfigMap and Secret for configuration

## 🐍 Requirements

- Python 3.9+
- Docker
- Kubernetes cluster (e.g., Minikube)

## 🚀 Getting Started

### Clone the Repository
Clone the repository, open a terminal/powershell, cd to the directory of part2, enter "kubectl apply -f ." to apply all the yaml files

If using minikube, type minikube service cm-pod-service, afterwards the webpage should load

you can then access the home node (as default) or the readiness / liveness nodes with /health/ready and /health/live
