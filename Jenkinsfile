pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
			url: 'https://github.com/Sclra/python-app-CICD-test.git'
            }
        }

        stage('Install') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t cicd-app .'
            }
        }
    }
}
