pipeline {
    agent any
    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/yuvraj-singh009/Flask-Application-on-AWS-using-Terraform-Jenkins.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }
        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d --build'
            }
        }
        stage('Health Check') {
            steps {
                sh 'sleep 15 && curl -f http://localhost:5000/health'
            }
        }
    }
}