from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model (ensure the model is saved in the same directory or provide the correct path)
model = joblib.load('model.pkl')  # Update the path if needed

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """
    Prediction endpoint: accepts JSON input, processes it, and returns predictions.
    Expected input format: 
    {
        "data": [
            {6.1,2.8,4.7,1.2},
            {5.7,3.8,1.7,0.3}
             ]
    }
    """
    try:
        # Get JSON data from the request
        input_data = request.get_json()

        # Convert JSON data to pandas DataFrame
        data = pd.DataFrame(input_data["data"])

        # Make predictions
        predictions = model.predict(data)

        # Return the predictions as a JSON response
        return jsonify({"predictions": predictions.tolist()}), 200

    except Exception as e:
        # Handle errors and return an error response
        return jsonify({"error": str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
