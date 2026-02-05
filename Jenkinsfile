pipeline {
    agent any

    stages {
        stage('Checkout via SSH') {
            steps {
                git branch: 'main', url: 'git@github.com:Aikon72/QAsimulator.git'
            }
        }

        stage('Test') {
            steps {
                sh 'ls -la'
            }
        }
    }
}