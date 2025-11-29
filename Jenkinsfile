pipeline {
    agent any

    environment {
        PYTHON = "python3"  // Adjust if your Python is named differently
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Checking out repository..."
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo "Installing dependencies..."
                sh "${env.PYTHON} -m pip install --upgrade pip"
                sh "${env.PYTHON} -m pip install -r requirements.txt"
                sh "${env.PYTHON} -m pip install mlflow dvc"
            }
        }

        stage('Run Pipeline') {
            steps {
                echo "Running MLflow pipeline..."
                sh "${env.PYTHON} src/pipeline_components.py"
            }
        }

        stage('Verify Artifacts') {
            steps {
                echo "Checking generated artifacts..."
                sh "ls -l data/"
                sh "cat data/metrics.txt"
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs!"
        }
    }
}
