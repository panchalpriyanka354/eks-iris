import pandas as pd
import pickle
import os
import subprocess
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("data/iris_train.csv")

# Preprocessing
X = data.drop(columns=['species'])
y = data['species']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model inside models folder
model_path = "models/model.pkl"
os.makedirs(os.path.dirname(model_path), exist_ok=True)
with open(model_path, "wb") as f:
    pickle.dump(model, f)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# Push model to GitHub
try:
    subprocess.run(["git", "config", "--global", "user.email", "your-email@example.com"], check=True)
    subprocess.run(["git", "config", "--global", "user.name", "CodeBuild Bot"], check=True)
    subprocess.run(["git", "add", "app/models/model.pkl"], check=True)
    subprocess.run(["git", "commit", "-m", "Updated model.pkl with latest training"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Model pushed to GitHub successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error pushing model to GitHub: {e}")
