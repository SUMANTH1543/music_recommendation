import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the original dataset
df = pd.read_csv('Spotify Most Streamed Songs.csv')

# Keep relevant columns
df = df[[
    'track_name', 'artist(s)_name', 'valence_%', 'energy_%', 'danceability_%',
    'acousticness_%', 'instrumentalness_%', 'cover_url'
]].copy()

# Rename for consistency
df.rename(columns={'artist(s)_name': 'artist_name'}, inplace=True)

# Normalize percentage-based features
feature_cols = ['valence_%', 'energy_%', 'danceability_%', 'acousticness_%', 'instrumentalness_%']
df[feature_cols] = df[feature_cols] / 100.0

# Remove rows with missing or invalid cover URLs
invalid_cover = ['Not Found', 'not found', 'none', 'None', '']
df = df[~df['cover_url'].isin(invalid_cover)]
df = df[~df['cover_url'].isna()]
df.reset_index(drop=True, inplace=True)

# Mood classification function
def classify_mood(row):
    valence = row['valence_%']
    energy = row['energy_%']
    if valence > 0.7 and energy > 0.7:
        return 'happy'
    elif valence < 0.4 and energy < 0.4:
        return 'sad'
    elif valence < 0.5 and energy > 0.7:
        return 'angry'
    elif valence > 0.6 and energy < 0.5:
        return 'relaxed'
    else:
        return 'neutral'

# Apply mood classification
df['mood'] = df.apply(classify_mood, axis=1)

# Predefined mood vectors
mood_vectors = {
    'happy': [0.9, 0.9, 0.8, 0.2, 0.1],
    'sad': [0.2, 0.2, 0.4, 0.8, 0.6],
    'angry': [0.3, 0.8, 0.5, 0.1, 0.1],
    'relaxed': [0.8, 0.3, 0.6, 0.7, 0.3],
    'neutral': [0.5, 0.5, 0.5, 0.5, 0.5]
}

# Mood-based recommendation function
def recommend_songs(user_mood, top_n=5):
    if user_mood not in mood_vectors:
        return pd.DataFrame()
    
    mood_vector = mood_vectors[user_mood]
    song_features = df[feature_cols].values

    # Compute cosine similarity
    df['similarity'] = cosine_similarity([mood_vector], song_features)[0]

    # Sort and return top N
    top = df.sort_values(by='similarity', ascending=False).head(top_n)
    return top[['track_name', 'artist_name', 'cover_url', 'similarity']]
