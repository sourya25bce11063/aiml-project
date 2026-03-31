import customtkinter as ctk
import pandas as pd

# Set the appearance to Dark Mode and Blue theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SongRecommender(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("VibeCheck: Song Recommender")
        self.geometry("600x500")

        # Load Data
        try:
            self.df = pd.read_csv('my_songs.csv')
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=['track_name', 'track_artist', 'genre'])

        # --- UI ELEMENTS ---
        
        # Header
        self.label = ctk.CTkLabel(self, text="Music Recommender", font=("Helvetica", 24, "bold"))
        self.label.pack(pady=20)

        # Search Box
        self.search_entry = ctk.CTkEntry(self, placeholder_text="Try 'Hindi', 'English', or 'Pop'...", width=400)
        self.search_entry.pack(pady=10)

        # Search Button
        self.btn = ctk.CTkButton(self, text="Get Recommendations", command=self.recommend)
        self.btn.pack(pady=10)

        # Results Area (Scrollable)
        self.result_box = ctk.CTkTextbox(self, width=500, height=250, font=("Consolas", 14))
        self.result_box.pack(pady=20)
        self.result_box.insert("0.0", "Your recommendations will appear here...")

    def recommend(self):
        query = self.search_entry.get().strip().lower()
        
        # Filter Logic
        results = self.df[self.df['genre'].str.lower().str.contains(query)].copy()
        
        # Clear previous results
        self.result_box.delete("0.0", "end")

        if results.empty:
            self.result_box.insert("0.0", "No matches found! Try 'Hindi' or 'Rock'.")
        else:
            # Ranking (Simple Energy + Danceability score)
            results['rank'] = results['energy'] + results['danceability']
            top_5 = results.sort_values(by='rank', ascending=False).head(5)
            
            output_text = f"Top 5 Recommendations for '{query.title()}':\n"
            output_text += "-" * 50 + "\n\n"
            
            for i, row in top_5.iterrows():
                output_text += f"🎵 {row['track_name']}\n   👤 {row['track_artist']} | {row['genre']}\n\n"
            
            self.result_box.insert("0.0", output_text)

if __name__ == "__main__":
    app = SongRecommender()
    app.mainloop()
