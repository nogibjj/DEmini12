import os
import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler



tracking_uri = "file:" + os.path.join(os.getcwd(), "mlruns")
os.environ["MLFLOW_TRACKING_URI"] = tracking_uri
mlflow.set_tracking_uri(tracking_uri)

print(f"MLFLOW_TRACKING_URI: {mlflow.get_tracking_uri()}")

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
        artifact_path = "./mlruns/models"
        os.makedirs(artifact_path, exist_ok=True)
        mlflow.sklearn.log_model(model, artifact_path="models")

if __name__ == "__main__":
    main()
