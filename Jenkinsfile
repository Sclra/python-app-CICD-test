pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                sh 'echo "=========== Checkout Stage ==========="'

                git branch: 'main',
                    url: 'https://github.com/Sclra/python-app-CICD-test.git'
            }
        }

        stage('Install') {
            steps {
                sh 'echo "============ Install Stage ============"'

                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "============ Test Stage ============"'

                sh 'pytest'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'echo "========== Docker Build Stage =========="'

                sh 'docker build -t cicd-app .'
            }
        }
    }
}
