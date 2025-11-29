MLOps Pipeline Project

Course: Cloud MLOps (BS AI)
Student Name: Hira Binte Zahid
Student ID: 22i-0616
About the Project
This project demonstrates an end-to-end MLOps pipeline for the Boston Housing dataset. The pipeline handles data versioning, preprocessing, model training, evaluation, and experiment tracking. Tools used include Python, DVC, MLflow, and Jenkins/GitHub Actions to make the workflow reproducible and automated.

Project Layout
mlops-mlflow-assignment/

data/ (Raw and processed datasets)

src/ (Python scripts for pipeline steps)

pipeline_components.py

model_training.py

components/ (Saved MLflow components)

pipeline.py (Pipeline orchestration)

requirements.txt (Python dependencies)

Dockerfile (Custom Docker image if used)

Jenkinsfile (CI/CD pipeline automation)

.dvc/ (DVC configuration)

README.md (Project documentation)

Getting Started

Clone the repository:
git clone <repository-url>
cd mlops-mlflow-assignment

Install dependencies:
pip install -r requirements.txt

Setup DVC:

Initialize DVC and configure remote storage

Pull the dataset using DVC

Run MLflow UI to track experiments, metrics, and artifacts

Running the Pipeline

Execute the main pipeline using Python

Pipeline stages tracked in MLflow include:

Data extraction from DVC

Data preprocessing and cleaning

Model training

Model evaluation

Use MLflow UI to view experiment metrics, model versions, and artifacts

Continuous Integration

Jenkins or GitHub Actions automatically:

Sets up environment and installs dependencies

Validates and runs the pipeline

Logs experiments to MLflow

Notes

Dataset: Boston Housing

Model: Random Forest Regressor

Metrics tracked: RMSE, R², MAE

Pipeline tracking: MLflow
