import streamlit as st
from recommend import recommend_songs
import pandas as pd
import random

st.set_page_config(page_title="EchoMood: Find Your Sound", page_icon="🎧", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #1DB954;
            text-align: center;
            margin-bottom: 30px;
        }
        .footer {
            text-align: center;
            font-size: 12px;
            color: gray;
            margin-top: 50px;
        }
        .song-title {
            font-size: 18px;
            font-weight: bold;
            color: #1DB954;
            text-decoration: none;
        }
        .song-title:hover {
            text-decoration: underline;
        }
        .artist-name {
            font-size: 14px;
            color: #555;
        }
        .stSelectbox > div {
            font-size: 14px !important;
            padding: 6px 10px !important;
        }
        .center-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
            margin-bottom: 30px;
        }
        .stButton > button {
            font-size: 14px !important;
            padding: 8px 16px !important;
            border-radius: 8px;
            background-color: #1DB954;
            color: white;
            border: none;
        }
        .stButton > button:hover {
            background-color: #169c43;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown('<div class="title">🎧 EchoMood: Find Your Sound </div>', unsafe_allow_html=True)

# Mood selection
mood_list = ['happy', 'sad', 'angry', 'relaxed', 'neutral']
selected_mood = st.selectbox("😊 Select your current mood", mood_list)

# Centered buttons
st.markdown('<div class="center-buttons">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    recommend_click = st.button("🎶 Recommend Songs for My Mood")
with col2:
    if st.button("🎵 Tap for Spotify"):
        st.markdown("<meta http-equiv='refresh' content='0; url=https://open.spotify.com'>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Recommend songs
if 'recommend_click' in locals() and recommend_click:
    all_recommended = recommend_songs(selected_mood, top_n=50) 
    # Filter out songs with invalid cover_url
    valid_songs = all_recommended[
        ~(all_recommended['cover_url'].str.lower().isin(["not found", "none", ""])) &
        (~all_recommended['cover_url'].isna())
    ]

    # Randomly sample 5 from valid ones
    if len(valid_songs) >= 5:
        final_songs = valid_songs.sample(5, replace=False, random_state=random.randint(1, 9999)).reset_index(drop=True)
    else:
        final_songs = valid_songs.head(5)

    st.subheader("🔥 Recommended Songs:")

    # Create 5 columns for side-by-side display
    cols = st.columns(5)

    for idx, row in final_songs.iterrows():
        with cols[idx]:
            st.image(row['cover_url'], width=200)
            st.markdown(f"""
                <a href="{row['cover_url']}" target="_blank" class="song-title">{row['track_name']}</a><br>
                <span class="artist-name">{row['artist_name']}</span>
            """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit & Spotify Data</div>', unsafe_allow_html=True)
