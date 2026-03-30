#  VibeCheck: Dual-Language Song Recommender 🎧

Welcome to **VibeCheck**, a Python-based music recommendation engine designed to bridge the gap between **Hindi (Bollywood)** and **English** hits. This project uses data science principles to suggest the perfect tracks based on musical "vibes" like energy and danceability.

---

##  Features
* **Dual-Language Support:** Curated database of 50 Hindi and 50 English famous tracks.
* **Modern UI:** A clean, minimalist dark-mode interface built with `CustomTkinter`.
* **Hybrid Logic:** * **CLI Mode:** Fast, terminal-based searching for developers.
    * **GUI Mode:** Interactive window-based searching for users.
* **Vibe-Based Ranking:** Recommends songs by calculating a "Vibe Score" using **Normalization (MinMaxScaler)**.

---

##  Tech Stack
* **Language:** Python 3.x 
* **Data Analysis:** `pandas` 
* **Machine Learning:** `scikit-learn` 
* **GUI Library:** `CustomTkinter` 

---

## 📂 Project Structure
```text
Song_Recommender/
├── venv/                # Virtual Environment
├── my_songs.csv         # The generated song database
├── data_gen.py          # Script to create/reset the 100-song dataset
├── main.py              # CLI version of the recommender
└── gui_app.py           # The modern GUI application (Main Entry)
