pipeline {
    agent any

    options {
        // Adds a timestamp to every line in the Jenkins console.log
        timestamps()

        // Jenkins will keep only last 20 builds and discareded older ones
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }


    environment {
        GIT_BRANCH = 'main'
        REGISTRY = 'iamridoydey'
        BACKEND_IMAGE = "${REGISTRY}/notebook-api"
        FRONTEND_IMAGE = "${REGISTRY}/notebook-ui"

    }

    stages {
        stage('Checkout') {
            steps {
                git branch: env.GIT_BRANCH,
                    url: 'https://github.com/iamridoydey/flask-notebook-app.git',
                    credentialsId: 'flask-notebook-app-id'
            }
        }

        stage('Backend build (Python/Flask)'){
            steps {
                dir('backend'){
                    sh'''
                    python3 --version

                    # Create virtual environment for this build
                    python3 -m venv venv
                    . venv/bin/activate

                    # Install project dependencies
                    venv/bin/python -m pip install -r requirements.txt

                    # Run a qucik syntax check
                    python -m py_compile app.py
                '''
                }
            }
        }


        stage('Frontend Build (React vite)') {
            agent {
                docker {
                    image 'node:22' 
                    args '-u root:root'
                }
            }
            steps {
                dir('frontend'){
                    sh'''
                    node --version
                    npm --version
                    npm ci || npm install
                    npm run build
                '''
                }  
            }
        }

        stage('Docker build images'){
            steps {
                sh'''
                    docker --version
                    docker compose version

                    # Build the image
                    docker build -t ${BACKEND_IMAGE}:$BUILD_NUMBER ./backend
                    docker build -t ${FRONTEND_IMAGE}:$BUILD_NUMBER ./frontend

                    # Tag the image as latest
                    docker tag ${BACKEND_IMAGE}:$BUILD_NUMBER ${BACKEND_IMAGE}:latest
                    docker tag ${FRONTEND_IMAGE}:$BUILD_NUMBER ${FRONTEND_IMAGE}:latest
                '''
            }
        }


        stage('push images'){
            when {
                branch 'main'
            }

            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub_creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]){
                    sh'''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push ${BACKEND_IMAGE}:$BUILD_NUMBER
                    docker push ${FRONTEND_IMAGE}:$BUILD_NUMBER
                    docker push ${BACKEND_IMAGE}:latest
                    docker push ${FRONTEND_IMAGE}:latest
                    docker logout
                '''
                }
            }
        }  
    }


    post {
        success {
            echo "Build ${env.BUILD_NUMBER} succeeded"
        }

        failure {
            echo "Build ${env.BUILD_NUMBER} failed"
        }

        always {
            echo "Pipeline finished"
        }
    }
}