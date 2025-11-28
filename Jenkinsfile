pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Preprocessing') {
            steps {
                sh 'python src/preprocess.py'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python src/train.py'
            }
        }
    }
}
