import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("dataset/crop_data.csv")

# Remove missing values
df = df.dropna()

# Create Yield column
df["Yield"] = df["Production"] / df["Area"]

# Remove invalid values
df = df[df["Area"] > 0]

# Encode categorical columns
encoders = {}

for col in ["State_Name", "District_Name", "Season", "Crop"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Features
X = df[
    [
        "State_Name",
        "District_Name",
        "Crop_Year",
        "Season",
        "Crop",
        "Area"
    ]
]

# Target
y = df["Yield"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=20,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, pred))

# Save model
joblib.dump(model, "models/yield_model.pkl")
joblib.dump(encoders, "models/yield_encoders.pkl")

print("Yield model saved successfully.")