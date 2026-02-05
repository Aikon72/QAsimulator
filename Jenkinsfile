pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Aikon72/QAsimulator.git'
            }
        }

        stage('Test') {
            steps {
                sh 'ls -la'
                sh 'find . -type f -name "*.py" | head -10'
            }
        }
    }
}