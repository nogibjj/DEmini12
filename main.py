import os
import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


os.environ["MLFLOW_TRACKING_URI"] = "file:./mlruns"
os.environ["MLFLOW_ARTIFACT_URI"] = "file:./mlruns"
print(f"MLFLOW_TRACKING_URI: {os.getenv('MLFLOW_TRACKING_URI')}")
print(f"MLFLOW_ARTIFACT_URI: {os.getenv('MLFLOW_ARTIFACT_URI')}")
os.makedirs("./mlruns", exist_ok=True)
os.chmod("./mlruns", 0o777)


def main():
    # Set up MLflow tracking URI
    # mlflow.set_tracking_uri("file:///workspaces/DEmini12/mlruns")
    # print(f"MLflow Tracking URI: {mlflow.get_tracking_uri()}")

    # Load data
    df = pd.read_csv("data/instagram_Data.csv", delimiter=",")
    df = df.dropna()
    features = df[["Engagement avg"]]
    target = df["Rank"]

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))

    # Log the model and metrics
    with mlflow.start_run():
        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("data_path", "data/instagram_Data.csv")
        mlflow.log_metric("accuracy", accuracy)

        # Use relative path for artifact_path
        mlflow.sklearn.log_model(model, artifact_path="models")
        print("Model logged successfully.")


if __name__ == "__main__":
    main()
