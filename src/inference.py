from flask import Flask, request, jsonify
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load model from GitHub models folder
model_path = "../models/model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data['features']], columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    prediction = model.predict(df)[0]
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
