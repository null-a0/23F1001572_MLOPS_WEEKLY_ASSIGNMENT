import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create models directory
os.makedirs("models", exist_ok=True)

# Load dataset
df = pd.read_csv("data/iris.csv")

# Features and target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print(f"Accuracy: {accuracy:.4f}")

# Save model
joblib.dump(model, "models/model.joblib")

print("Model saved to models/model.joblib")
