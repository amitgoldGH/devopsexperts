pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // store username+password in Jenkins
        DOCKER_IMAGE = "amitgoldgh/python-flask-part2:latest"
        HELM_CHART_DIR = "part3/helm/amitdevopsprojectchart"
        HELM_CHART_OUTPUT = "part3/helm/charts"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Push Docker Image') {
            when {
                changeset "part3/docker/**"
            }
            steps {
                bat """
                docker build -t %DOCKER_IMAGE% part3/docker
                docker login -u %DOCKERHUB_CREDENTIALS_USR% -p %DOCKERHUB_CREDENTIALS_PSW%
                docker push %DOCKER_IMAGE%
                """
            }
        }

        stage('Reinstall Helm Chart') {
            when {
                changeset "part3/docker/**"
            }
            steps {
                bat """
                helm upgrade --install myapp %HELM_CHART_DIR% --namespace default --set image.repository=amitgoldgh/python-flask-part2 --set image.tag=latest
                """
            }
        }

        stage('Package Helm Chart') {
            when {
                changeset "part3/helm/**"
            }
            steps {
                bat """
                helm package %HELM_CHART_DIR% -d %HELM_CHART_OUTPUT%
                """
            }
        }
    }
}