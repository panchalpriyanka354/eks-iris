# src/model.py
import boto3
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data_from_s3(bucket_name, file_name):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    return pd.read_csv(obj['Body'])

def train_model(train_data):
    X = train_data.drop(columns=['species'])
    y = train_data['species']

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, 'model.pkl')

if __name__ == "__main__":
    train_data = load_data_from_s3('ml-iris-demo-project-data', 'data/iris_train.csv')  
    train_model(train_data)
