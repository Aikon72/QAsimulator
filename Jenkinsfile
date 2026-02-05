pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Aikon72/qa_simulator.git'
            }
        }

        stage('Test') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                python -m pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                ssh -i /var/jenkins_home/.ssh/id_rsa aikon@192.168.1.100 '
                    cd /var/www/qa_simulator
                    git pull
                    source venv/bin/activate
                    pip install -r requirements.txt
                    sudo systemctl restart qa_simulator.service
                '
                '''
            }
        }
    }
}