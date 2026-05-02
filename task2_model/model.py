import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ---------------------------
# Load Processed Data
# ---------------------------
df = pd.read_csv("data/processed/processed_netflix.csv")

print("Data Loaded:", df.shape)

# ---------------------------
# Drop rows with missing target
# ---------------------------
df = df.dropna(subset=['type'])

# ---------------------------
# Select Features
# ---------------------------
X = df[['duration', 'genre_count', 'release_year']]
y = df['type']

# Fill missing values
X = X.fillna(0)

# ---------------------------
# Train Test Split
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------
# Train Model
# ---------------------------
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ---------------------------
# Predictions
# ---------------------------
y_pred = model.predict(X_test)

# ---------------------------
# Evaluation
# ---------------------------
accuracy = accuracy_score(y_test, y_pred)

print("✅ Model Trained Successfully")
print("Accuracy:", accuracy)