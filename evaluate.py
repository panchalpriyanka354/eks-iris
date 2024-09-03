import joblib
import boto3
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# S3 bucket details
S3_BUCKET = 'ml-iris-demo-project-bucket'
S3_TEST_DATA_PATH = 'data/iris_test.csv'  # Ensure the test data file name is correct
LOCAL_TEST_DATA_PATH = 'iris_test.csv'

def download_data_from_s3(bucket, s3_path, local_path):
    """Downloads the test data file from the specified S3 bucket."""
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket, s3_path, local_path)
        print(f"Successfully downloaded {s3_path} from bucket {bucket} to {local_path}.")
    except Exception as e:
        print(f"Error downloading {s3_path} from bucket {bucket}: {e}")
        raise

# Load the test data from S3
try:
    download_data_from_s3(S3_BUCKET, S3_TEST_DATA_PATH, LOCAL_TEST_DATA_PATH)
    print(f"Test data loaded successfully from {LOCAL_TEST_DATA_PATH}.")
except Exception as e:
    print(f"Failed to load test data: {e}")
    exit(1)

# Load the trained model
try:
    model = joblib.load('model.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Failed to load model: {e}")
    exit(1)

# Load the test dataset
try:
    test_data = pd.read_csv(LOCAL_TEST_DATA_PATH)
    X_test = test_data.drop('target', axis=1)  # Adjust the 'target' column name as needed
    y_test = test_data['target']
    print("Test data prepared for evaluation.")
except Exception as e:
    print(f"Error preparing test data: {e}")
    exit(1)

# Make predictions and evaluate the model
try:
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    # Output evaluation results
    print(f"Accuracy: {accuracy}")
    print(f"Classification Report:\n{report}")

    # Save evaluation results to a file (optional)
    with open('evaluation_report.txt', 'w') as f:
        f.write(f"Accuracy: {accuracy}\n")
        f.write(f"Classification Report:\n{report}\n")

    # Exit with an error if accuracy is below threshold to fail the build
    if accuracy < 0.80:  # Replace with your acceptable accuracy threshold
        print("Model performance is below the acceptable threshold.")
        exit(1)

except Exception as e:
    print(f"Error during evaluation: {e}")
    exit(1)
