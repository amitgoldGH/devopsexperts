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
- Jenkins
- Helm

## 🚀 Getting Started

### Clone the Repository
Clone the repository, open a terminal/powershell, cd to the directory of part3/helm/amitdevopsprojectchart, enter "helm install amitdevopsprojectchart ." to install the helm chart

If using minikube, type minikube service amitdevopsprojectchart, afterwards the webpage should load

you can then access the home node (as default) or the readiness / liveness nodes with /health/ready and /health/live

## Jenkins CICD Pipeline
The pipeline works in stages as following:

First stage - Check for changes in the docker folder (part3/docker/**)
If there are any changes in the app.py file, it will initiate a docker image build, then upload it to my docker hub repo - amitgoldgh, with the "latest" tag

Second stage (follow up for first stage) - Reinstall helm chart in order to pull the new image we just built from dockerhub (this will run the chart on the same machine that jenkins runs on)

Third stage - if there's a chart in the helm chart it self (any files in the chart, such as values.yaml or chart.yaml) it will package the chart again and store the tgz file in the part3/helm/charts/ folder
