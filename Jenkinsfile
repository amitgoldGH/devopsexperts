pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // store username+password in Jenkins
        DOCKER_IMAGE = "amitgoldgh/python-flask-part2:latest"
				HELM_CHART_DIR = 'D:\\DevopsExperts\\gitfolder\\devopsexperts\\part3\\helm\\amitdevopsprojectchart'
        HELM_CHART_OUTPUT = 'D:\\DevopsExperts\\gitfolder\\devopsexperts\\part3\\helm\\charts'
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
                helm upgrade --install amitdevopsprojectchart %HELM_CHART_DIR% --namespace default --set image.repository=amitgoldgh/python-flask-part2 --set image.tag=latest
                """
            }
        }
				
				stage('Port-forward Flask service') {
						when {
              changeset "part3/docker/**"
            }
						steps {
								bat '''
								start /b kubectl port-forward service/amitdevopsprojectchart 5000:5000
								REM wait a few seconds for port-forward to be ready
								ping -n 5 127.0.0.1 > nul
								'''
						}
				}

				stage('Test Flask Webpage') {
						when {
              changeset "part3/docker/**"
            }
						steps {
								bat 'curl -s -o nul -w "HTTP CODE: %{http_code}\\n" http://localhost:5000'
						}
				}

				stage('Cleanup Port-forward') {
						when {
              changeset "part3/docker/**"
            }
						steps {
								bat '''
								for /f "tokens=5" %%p in ('netstat -ano ^| find ":5000" ^| find "LISTENING"') do taskkill /PID %%p /F
								'''
						}
				}

        stage('Package Helm Chart') {
					when {
									changeset "part3/helm/amitdevopsprojectchart/**"
							}
					steps {
							script {
									def timestamp = bat(
											script: 'powershell -command "Get-Date -Format \\"yyyy-MM-dd-HH-mm\\""',
											returnStdout: true
									).trim()

									bat """
											helm package %HELM_CHART_DIR% ^
													--version ${timestamp} ^
													-d %HELM_CHART_DIR%
									"""
							}
					}
			}
    }
}