import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import mlflow
import mlflow.sklearn

# ------------ COMPONENT 1: DATA LOADING ------------
def load_data(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    # Rename target column for consistency
    if "medv" in df.columns:
        df = df.rename(columns={"medv": "TARGET"})
    df.to_csv(output_path, index=False)
    print("Data loaded and copied to:", output_path)
    return df

# ------------ COMPONENT 2: PREPROCESSING ------------
def preprocess_data(df: pd.DataFrame):
    X = df.drop("TARGET", axis=1)
    y = df["TARGET"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Save scaled data
    pd.DataFrame(X_train_scaled, columns=X.columns).to_csv("data/X_train.csv", index=False)
    pd.DataFrame(X_test_scaled, columns=X.columns).to_csv("data/X_test.csv", index=False)
    pd.DataFrame(y_train).to_csv("data/y_train.csv", index=False)
    pd.DataFrame(y_test).to_csv("data/y_test.csv", index=False)

    joblib.dump(scaler, "scaler.pkl")
    print("Preprocessing completed.")
    return X_train_scaled, X_test_scaled, y_train, y_test

# ------------ COMPONENT 3: MODEL TRAINING ------------
def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train.values.ravel())

    joblib.dump(model, "data/model.pkl")
    print("Model trained and saved to data/model.pkl")
    return model

# ------------ COMPONENT 4: EVALUATION ------------
def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    with open("data/metrics.txt", "w") as f:
        f.write(f"Mean Squared Error: {mse}\n")

    print("Evaluation completed. MSE:", mse)
    return mse

# ------------ FULL PIPELINE WITH MLflow ------------
def run_pipeline(input_csv="data/raw_data.csv"):
    # Start MLflow experiment
    mlflow.set_experiment("Boston_Housing_Experiment")
    with mlflow.start_run():
        # Load data
        df = load_data(input_csv, "data/loaded_data.csv")

        # Preprocess
        X_train, X_test, y_train, y_test = preprocess_data(df)

        # Train model
        model = train_model(X_train, y_train)

        # Evaluate
        mse = evaluate_model(model, X_test, y_test)

        # Log model and metrics
        mlflow.sklearn.log_model(model, "random_forest_model")
        mlflow.log_metric("mse", mse)
        mlflow.log_artifact("data/metrics.txt")
        print("MLflow run completed. Model and metrics logged.")

# ------------ MAIN ------------
if __name__ == "__main__":
    run_pipeline()
