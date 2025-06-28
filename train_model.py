import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import json
import random
import numpy as np

random.seed(42)
np.random.seed(42)


# Load config
with open('config.json') as f:
    config = json.load(f)

# Load dataset
df = pd.read_csv("training_data.csv")

# Split features and label
X = df[config["features"]]
y = df["label"]

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = RandomForestRegressor(n_estimators=300, max_depth=10, min_samples_split=3, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, config["model_path"])
print("Model trained and saved.")

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Evaluation:")
print(f" - Mean Squared Error (MSE): {mse:.2f}")
print(f" - R² Score: {r2:.2f}")
