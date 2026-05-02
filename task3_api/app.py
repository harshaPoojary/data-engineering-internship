import pandas as pd
from fastapi import FastAPI
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

# ---------------------------
# Load and train model once
# ---------------------------
df = pd.read_csv("data/processed/processed_netflix.csv")

df = df.dropna(subset=['type'])

X = df[['duration', 'genre_count', 'release_year']].fillna(0)
y = df['type']

model = RandomForestClassifier()
model.fit(X, y)

# ---------------------------
# API Routes
# ---------------------------
@app.get("/")
def home():
    return {"message": "Netflix Prediction API is running 🚀"}

@app.get("/predict")
def predict(duration: float, genre_count: int, release_year: int):
    input_data = [[duration, genre_count, release_year]]
    prediction = model.predict(input_data)[0]

    result = "Movie" if prediction == 0 else "TV Show"

    return {
        "prediction": result
    }