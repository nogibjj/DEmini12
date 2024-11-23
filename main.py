"""Runs a simple machine learning experiment"""

import os
import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from mlflow.models.signature import ModelSignature
from mlflow.types.schema import Schema, ColSpec
from mlflow.models.utils import _enforce_schema


def main():
    """Runs a basic logistic regression model and logs it with MLflow"""

    # Step 1: Load data
    data_path = os.getenv("DATA_PATH", "data/instagram_Data.csv")
    df = pd.read_csv(data_path, delimiter=",")

    # Step 2: Data preprocessing
    df = df.dropna()  # Remove NaN values
    features = df[["Engagement avg"]]
    target = df["Rank"]

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Convert back to DataFrame with column names
    X_train = pd.DataFrame(X_train, columns=["Engagement avg"])
    X_test = pd.DataFrame(X_test, columns=["Engagement avg"])

    # Step 3: Train the logistic regression model
    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)

    # Step 4: Make predictions and calculate accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Step 5: Define input_example and schema
    input_example = X_test.iloc[0:1]  # Correct format
    input_schema = Schema([ColSpec("double", "Engagement avg")])
    output_schema = Schema([ColSpec("integer", "Rank")])
    signature = ModelSignature(inputs=input_schema, outputs=output_schema)

    # Step 6: Log experiment with MLflow
    with mlflow.start_run() as run:
        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("data_path", data_path)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(
            model,
            "model",
            input_example=input_example,
            signature=signature
        )

        # Generate the model URI within the MLflow run context
        logged_model_uri = f"runs:/{run.info.run_id}/model"

        # Step 7: Validate input example
        try:
            # Validate input example format
            _enforce_schema(input_example, signature.inputs)
            print("Input example validated successfully.")
        except Exception as e:
            print(f"Input example validation failed: {e}")


if __name__ == "__main__":
    main()
