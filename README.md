# 🎧 EchoMood: Mood-Based Music Recommender

EchoMood is a personalized music recommendation web app that suggests songs based on your selected mood. It leverages cosine similarity to match moods with song features—without using any pre-trained models or deep learning. Built using **Streamlit**, this project focuses on clean user interaction, simple logic, and beautiful UI.

---

## 🚀 Demo  
📦 [https://github.com/SUMANTH1543/music_recommendation.git](https://github.com/SUMANTH1543/music_recommendation.git)  
🟢 Built entirely with Python and Streamlit.

---

## 📌 Features

- 🎵 Recommends 5 songs based on the mood you choose
- 🎲 Randomizes recommendations on every click
- 🖼️ Displays album art and artist details
- ✅ Filters out songs with missing or invalid URLs
- 💚 Includes quick access to [Spotify](https://www.spotify.com)

---

## 💻 Tech Stack

| Tool          | Purpose                       |
|---------------|-------------------------------|
| Python        | Core programming language     |
| Streamlit     | Web app UI framework          |
| Pandas, NumPy | Data manipulation & similarity|
| HTML/CSS      | Custom styling in Streamlit   |

---

## 🧠 Recommendation Logic

- The app uses **cosine similarity** to find songs with feature vectors that best match the selected mood.
- A simple mood embedding system maps moods to vectors.
- No machine learning or pre-trained models are used — the logic is **lightweight, fast, and interpretable**.

---

## ⚙️ Installation & Running Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SUMANTH1543/music_recommendation
2. **Install Dependencies**
   pip install -r requirements.txt
3. **Run the app**
   streamlit run app.py
## 🌐 Future Improvements

1.Add audio previews or Spotify embeds

2.Integrate user input text and use NLP for mood detection

3.Store user preferences for personalized recommendations

4.Deploy to Streamlit Cloud or Hugging Face Spaces

## 📬 Connect with Me
Feel free to reach out if you liked this project or want to collaborate:

📧 Email:godarisumanth1543@gmail.com
💼 LinkedIn:[https://www.linkedin.com/in/sumanthgodari](https://www.linkedin.com/in/sumanthgodari/)
