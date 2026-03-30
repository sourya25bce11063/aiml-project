import pandas as pd
import random

# 1. Real Hindi Songs (50 Total)
hindi_songs = [
    ("Kesariya", "Arijit Singh", "Hindi-Romantic"), ("Tum Hi Ho", "Arijit Singh", "Hindi-Romantic"),
    ("Raataan Lambiyan", "Jubin Nautiyal", "Hindi-Romantic"), ("Chaiyya Chaiyya", "Sukhwinder Singh", "Hindi-Classic"),
    ("Kal Ho Naa Ho", "Sonu Nigam", "Hindi-Sad"), ("Badtameez Dil", "Benny Dayal", "Hindi-Dance"),
    ("Pasoori", "Ali Sethi", "Hindi-Indie"), ("Apna Bana Le", "Arijit Singh", "Hindi-Romantic"),
    ("Zinda Banda", "Anirudh Ravichander", "Hindi-Action"), ("Jai Ho", "A.R. Rahman", "Hindi-Global"),
    ("Dil Se Re", "A.R. Rahman", "Hindi-Classic"), ("Tera Ban Jaunga", "Akhil Sachdeva", "Hindi-Romantic"),
    ("Ghooghat", "Arijit Singh", "Hindi-Romantic"), ("Kabira", "Tochi Raina", "Hindi-Indie"),
    ("Namo Namo", "Amit Trivedi", "Hindi-Devotional"), ("Ghungroo", "Arijit Singh", "Hindi-Dance"),
    ("Garmi", "Badshah", "Hindi-Dance"), ("Lut Gaye", "Jubin Nautiyal", "Hindi-Romantic"),
    ("Ranjha", "B Praak", "Hindi-Sad"), ("Mast Magan", "Arijit Singh", "Hindi-Romantic"),
    ("Channa Mereya", "Arijit Singh", "Hindi-Sad"), ("Kun Faya Kun", "A.R. Rahman", "Hindi-Sufi"),
    ("Aankhey Khuli", "Lata Mangeshkar", "Hindi-Classic"), ("Lag Jaa Gale", "Lata Mangeshkar", "Hindi-Classic"),
    ("Tujhe Kitna Chahne Lage", "Arijit Singh", "Hindi-Romantic"), ("Shrivalli", "Javed Ali", "Hindi-Pop"),
    ("O Maahi", "Arijit Singh", "Hindi-Romantic"), ("Heeriye", "Arijit Singh", "Hindi-Indie"),
    ("Malhari", "Vishal Dadlani", "Hindi-Dance"), ("First Class", "Arijit Singh", "Hindi-Dance"),
    ("Gully Boy", "Ranveer Singh", "Hindi-Rap"), ("Brown Munde", "AP Dhillon", "Hindi-Indie"),
    ("Excuses", "AP Dhillon", "Hindi-Indie"), ("Proper Patola", "Diljit Dosanjh", "Hindi-Pop"),
    ("Lemonade", "Diljit Dosanjh", "Hindi-Pop"), ("Born to Shine", "Diljit Dosanjh", "Hindi-Pop"),
    ("Saami Saami", "Sunidhi Chauhan", "Hindi-Dance"), ("Manike", "Yohani", "Hindi-Pop"),
    ("Dilbar", "Neha Kakkar", "Hindi-Dance"), ("Kala Chashma", "Badshah", "Hindi-Dance"),
    ("Gerua", "Arijit Singh", "Hindi-Romantic"), ("Dil Diyan Gallan", "Atif Aslam", "Hindi-Romantic"),
    ("Zaalima", "Arijit Singh", "Hindi-Romantic"), ("Bom Diggy Diggy", "Zack Knight", "Hindi-Dance"),
    ("Galti Se Mistake", "Arijit Singh", "Hindi-Fun"), ("Dangal", "Daler Mehndi", "Hindi-Inspiring"),
    ("Kar Gayi Chull", "Badshah", "Hindi-Dance"), ("Nashe Si Chadh Gayi", "Arijit Singh", "Hindi-Dance"),
    ("Galliyan", "Ankit Tiwari", "Hindi-Romantic"), ("Sun Saathiya", "Priya Saraiya", "Hindi-Dance")
]

# 2. Real English Songs (50 Total)
english_songs = [
    ("Blinding Lights", "The Weeknd", "English-Pop"), ("Shape of You", "Ed Sheeran", "English-Pop"),
    ("Stay", "Justin Bieber", "English-Pop"), ("Levitating", "Dua Lipa", "English-Dance"),
    ("Humble", "Kendrick Lamar", "English-HipHop"), ("Flowers", "Miley Cyrus", "English-Pop"),
    ("As It Was", "Harry Styles", "English-Indie"), ("Believer", "Imagine Dragons", "English-Rock"),
    ("Bohemian Rhapsody", "Queen", "English-Rock"), ("Rolling in the Deep", "Adele", "English-Soul"),
    ("Cruel Summer", "Taylor Swift", "English-Pop"), ("Anti-Hero", "Taylor Swift", "English-Pop"),
    ("Bad Guy", "Billie Eilish", "English-Alt"), ("Lovely", "Billie Eilish", "English-Sad"),
    ("God's Plan", "Drake", "English-HipHop"), ("Starboy", "The Weeknd", "English-R&B"),
    ("Uptown Funk", "Bruno Mars", "English-Funk"), ("Perfect", "Ed Sheeran", "English-Romantic"),
    ("Someone Like You", "Adele", "English-Soul"), ("Sunflower", "Post Malone", "English-Pop"),
    ("Seven", "Jungkook", "English-Pop"), ("Die For You", "The Weeknd", "English-R&B"),
    ("Creepin", "Metro Boomin", "English-HipHop"), ("Escapism", "RAYE", "English-R&B"),
    ("Vampire", "Olivia Rodrigo", "English-Pop"), ("Driver's License", "Olivia Rodrigo", "English-Pop"),
    ("Kill Bill", "SZA", "English-R&B"), ("Snooze", "SZA", "English-R&B"),
    ("Peaches", "Justin Bieber", "English-Pop"), ("Watermelon Sugar", "Harry Styles", "English-Pop"),
    ("Heat Waves", "Glass Animals", "English-Indie"), ("Cold Heart", "Elton John", "English-Dance"),
    ("Bad Habits", "Ed Sheeran", "English-Pop"), ("Shivers", "Ed Sheeran", "English-Pop"),
    ("Thunder", "Imagine Dragons", "English-Rock"), ("Radioactive", "Imagine Dragons", "English-Rock"),
    ("Counting Stars", "OneRepublic", "English-Pop"), ("Good 4 U", "Olivia Rodrigo", "English-Pop"),
    ("Industry Baby", "Lil Nas X", "English-HipHop"), ("Montero", "Lil Nas X", "English-Pop"),
    ("About Damn Time", "Lizzo", "English-Pop"), ("Save Your Tears", "The Weeknd", "English-Pop"),
    ("One Dance", "Drake", "English-HipHop"), ("Thinking Out Loud", "Ed Sheeran", "English-Romantic"),
    ("All of Me", "John Legend", "English-Romantic"), ("Hello", "Adele", "English-Soul"),
    ("Sweet Child O' Mine", "Guns N' Roses", "English-Rock"), ("Lose Yourself", "Eminem", "English-HipHop"),
    ("Mockingbird", "Eminem", "English-HipHop"), ("Without Me", "Eminem", "English-HipHop")
]

# 3. Create Dataset
all_songs = []

# Merge both lists
for song in (hindi
