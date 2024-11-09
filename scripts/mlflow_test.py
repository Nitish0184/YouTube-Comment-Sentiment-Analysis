import mlflow
from mlflow.tracking import MlflowClient
mlflow.set_tracking_uri("http://13.233.122.146:5000/")
client = MlflowClient()
print("MLflow client initialized successfully.")
