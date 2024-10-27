import mlflow
from mlflow.tracking import MlflowClient
mlflow.set_tracking_uri("http://ec2-43-204-229-37.ap-south-1.compute.amazonaws.com:5000/")
client = MlflowClient()
print("MLflow client initialized successfully.")
