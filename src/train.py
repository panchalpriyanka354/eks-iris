import pandas as pd
import pickle
import os
import git
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("data/iris_train.csv")

# Preprocessing
X = data.drop(columns=['species'])
y = data['species']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
os.makedirs("models", exist_ok=True)
model_path = "models/model.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

# Evaluate model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# Upload to GitHub
repo = git.Repo(".")
repo.index.add([model_path])
repo.index.commit("Updated model.pkl with latest trained model")
repo.remote(name="origin").push()
print("Model uploaded to GitHub successfully.")
