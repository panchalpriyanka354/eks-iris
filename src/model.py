import boto3
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data_from_s3(bucket_name, file_name):
    """
    Load data from an S3 bucket.
    """
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    return pd.read_csv(obj['Body'])

def train_model(train_data):
    """
    Train the RandomForest model and save it as model.pkl.
    """
    X = train_data.drop(columns=['species'])
    y = train_data['species']

    model = RandomForestClassifier()
    model.fit(X, y)

    # Save the trained model to a file
    joblib.dump(model, 'model.pkl')
    print("Model training completed and saved as model.pkl.")

    # Upload the saved model to S3
    upload_model_to_s3('model.pkl', 'ml-iris-demo-project-new-bucket', 'src/model.pkl')

def upload_model_to_s3(file_name, bucket_name, object_name):
    """
    Upload a file to an S3 bucket.
    """
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"Successfully uploaded {file_name} to s3://{bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading {file_name} to S3: {e}")

if __name__ == "__main__":
    # Replace with your actual bucket name and file path
    train_data = load_data_from_s3('ml-iris-demo-project-new-bucket', 'data/iris_train.csv')  
    train_model(train_data)
[ec2-user@ip-172-31-23-139 ~]
