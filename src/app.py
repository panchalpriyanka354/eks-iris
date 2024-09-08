from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import boto3

# Initialize the Flask app
app = Flask(__name__)

# S3 bucket details
S3_BUCKET = 'ml-iris-demo-project-new-bucket'
S3_MODEL_PATH = 'src/model.pkl'
LOCAL_MODEL_PATH = 'model.pkl'

def download_model_from_s3(bucket, s3_path, local_path):
    """Downloads the model file from the specified S3 bucket."""
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket, s3_path, local_path)
        print(f"Successfully downloaded {s3_path} from bucket {bucket} to {local_path}.")
    except Exception as e:
        print(f"Error downloading {s3_path} from bucket {bucket}: {e}")
        raise

# Load the model from S3 at startup
try:
    download_model_from_s3(S3_BUCKET, S3_MODEL_PATH, LOCAL_MODEL_PATH)
    model = joblib.load(LOCAL_MODEL_PATH)
    print(f"Model loaded successfully from {LOCAL_MODEL_PATH}.")
except Exception as e:
    print(f"Failed to load model: {e}")
    model = None

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Handles GET requests to render the index page and POST requests for predictions."""
    if request.method == 'GET':
        # Render index.html on GET request
        return render_template('index.html')

    # Handle prediction logic for POST requests
    if request.method == 'POST':
        if model is None:
            return jsonify({"error": "Model not loaded. Please check the logs for errors."}), 500

        try:
            input_data = request.get_json()
            if 'data' not in input_data:
                return jsonify({"error": "Invalid input format. 'data' key is missing."}), 400

            data = pd.DataFrame(input_data['data'])
            predictions = model.predict(data)
            return jsonify({"predictions": predictions.tolist()}), 200

        except Exception as e:
            return jsonify({"error": f"Prediction error: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
