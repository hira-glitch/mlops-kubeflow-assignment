********** MLOps Pipeline Project **********

Course: Cloud MLOps (BS AI)
Student Name:Hira Binte Zahid
Student ID: 22i-0508

********** Project Overview **********
This project demonstrates an end-to-end MLOps pipeline for the Boston Housing dataset. The pipeline handles:

Data versioning using DVC

Data preprocessing and cleaning

Model training and evaluation

Experiment tracking using MLflow

Continuous Integration with Jenkins/GitHub Actions

The goal is to create a reproducible and automated workflow for machine learning experiments.

********** Project Structure **********

mlops-mlflow-assignment/
├─ data/                  # Raw and processed datasets
├─ src/                   # Python scripts for pipeline steps
│   ├─ pipeline_components.py
│   ├─ model_training.py
├─ components/            # Saved MLflow components
├─ pipeline.py            # Pipeline orchestration
├─ requirements.txt       # Python dependencies
├─ Dockerfile             # Custom Docker image (optional)
├─ Jenkinsfile            # CI/CD automation
├─ .dvc/                  # DVC configuration
└─ README.md              # Project documentation


********** Getting Started **********

Clone the Repository

git clone <repository-url>
cd mlops-mlflow-assignment


Install Dependencies

pip install -r requirements.txt


Setup DVC

Initialize DVC and configure remote storage

Pull the dataset using DVC

Run MLflow UI

Start MLflow to track experiments, metrics, and artifacts

********** Running the Pipeline **********

Execute the pipeline using Python

MLflow tracks the following stages:

Data extraction from DVC

Data preprocessing

Model training

Model evaluation

Check MLflow UI for metrics, model versions, and artifacts

********** Continuous Integration **********

The pipeline is automated using Jenkins or GitHub Actions:

Sets up the environment and installs dependencies

Compiles and runs the pipeline

Logs experiments automatically to MLflow

********** Notes **********

Dataset: Boston Housing

Model: Random Forest Regressor

Metrics Tracked: RMSE, R², MAE

Pipeline Tracking: MLflow


