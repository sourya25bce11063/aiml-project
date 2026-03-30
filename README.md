# 🎵 Song Recommendation System

A Python-based CLI tool that recommends songs from your personal music library based on language or genre, ranked by danceability and energy.

---

## Features

- Filter songs by **language** (e.g., Hindi, English) or **genre** (e.g., Pop, Rock, Romantic)
- Ranks results using a **Popularity Score** derived from danceability and energy
- Returns the **Top 5** best-matching tracks

---

## Prerequisites

- Python 3.7+
- `pandas`
- `scikit-learn`

Install dependencies:

```bash
pip install pandas scikit-learn
```

---

## Setup

1. **Generate the dataset** — Run the data generation script first to create `my_songs.csv`:

   ```bash
   python data_gen.py
   ```

2. **Run the recommender:**

   ```bash
   python recommendation.py
   ```

---

## Usage

When prompted, enter a language or genre keyword:

```
--- Song Recommendation System ---
Available: Hindi, English, Romantic, Pop, Rock, etc.
Enter a Language or Genre: Hindi
```

**Example output:**

```
Top Recommendations for you:
      track_name       track_artist         genre
  Tum Hi Ho           Arijit Singh    Hindi Romantic
  Kesariya            Arijit Singh    Hindi Pop
  ...
```

---

## How It Works

1. Loads song data from `my_songs.csv`
2. Filters rows where the `genre` column contains the user's keyword (case-insensitive)
3. Computes a `rank_score` by summing `danceability` and `energy` values for each track
4. Returns the top 5 songs sorted by highest score

---

## Project Structure

```
├── data_gen.py           # Generates my_songs.csv with song data
├── recommendation.py     # Main recommendation script
├── my_songs.csv          # Auto-generated song dataset
└── README.md
```

---

## Expected CSV Format

The `my_songs.csv` file should contain at least these columns:

| Column        | Description                        |
|---------------|------------------------------------|
| `track_name`  | Name of the song                   |
| `track_artist`| Artist name                        |
| `genre`       | Genre/language tag (e.g., Hindi Pop)|
| `danceability`| Numeric score (0.0 – 1.0)         |
| `energy`      | Numeric score (0.0 – 1.0)         |

---

## Notes

- The keyword search is **partial and case-insensitive** — searching `"pop"` will match `"Hindi Pop"`, `"K-Pop"`, etc.
- If no matches are found, the system will prompt you to try a different keyword.
- Make sure to run `data_gen.py` before `recommendation.py`, otherwise the program will exit with an error.
