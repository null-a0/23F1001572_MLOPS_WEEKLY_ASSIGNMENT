from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load Iris dataset
iris = load_iris(as_frame=True)
X = iris.data
y = iris.target

# Train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X, y)

# Save the model
joblib.dump(model, "model.joblib")

print("✅ model.joblib created successfully!")
