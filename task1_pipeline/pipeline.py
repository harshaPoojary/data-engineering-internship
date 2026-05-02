import pandas as pd

# ---------------------------
# Load Data
# ---------------------------
df = pd.read_csv("data/raw/netflix_titles.csv")

print("Initial Shape:", df.shape)

# ---------------------------
# Remove Duplicates
# ---------------------------
df.drop_duplicates(inplace=True)

# ---------------------------
# Handle Missing Values
# ---------------------------
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')

# ---------------------------
# Date Processing
# ---------------------------
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

# ---------------------------
# Feature Engineering
# ---------------------------
df['genre_count'] = df['listed_in'].apply(lambda x: len(str(x).split(',')))
df['type'] = df['type'].map({'Movie': 0, 'TV Show': 1})

# ---------------------------
# Duration Cleaning
# ---------------------------
df['duration'] = df['duration'].str.extract('(\d+)').astype(float)

# ---------------------------
# Drop unnecessary columns
# ---------------------------
df.drop(['show_id', 'title', 'date_added'], axis=1, inplace=True)

# ---------------------------
# Save Processed Data
# ---------------------------
df.to_csv("data/processed/processed_netflix.csv", index=False)

print("✅ Pipeline completed!")
print("Final Shape:", df.shape)
