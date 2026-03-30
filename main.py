import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def get_recommendations():
    # Load the data
    try:
        df = pd.read_csv('my_songs.csv')
    except FileNotFoundError:
        return "Please run data_gen.py first!"

    print("\n--- Song Recommendation System ---")
    print("Available: Hindi, English, Romantic, Pop, Rock, etc.")
    query = input("Enter a Language or Genre: ").strip().lower()

    # Filter by searching for the keyword in the 'genre' column
    results = df[df['genre'].str.lower().str.contains(query)].copy()

    if results.empty:
        return "No matches found. Try keywords like 'Hindi' or 'Pop'."

    # Ranking logic: Calculate a 'Popularity Score'
    # We use Danceability and Energy to rank the "vibe"
    scaler = MinMaxScaler()
    results['rank_score'] = results[['danceability', 'energy']].sum(axis=1)
    
    # Sort by highest score
    top_5 = results.sort_values(by='rank_score', ascending=False).head(5)
    
    return top_5[['track_name', 'track_artist', 'genre']]

if __name__ == "__main__":
    output = get_recommendations()
    if isinstance(output, str):
        print(output)
    else:
        print("\nTop Recommendations for you:")
        print(output.to_string(index=False))
