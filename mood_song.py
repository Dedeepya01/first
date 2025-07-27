import random

# Define moods and their song vibes
songs = {
    "happy": [
        " 'Levitating' - Dua Lipa",
        " 'Can’t Stop the Feeling' - Justin Timberlake",
        " 'Happy' - Pharrell Williams"
    ],
    "sad": [
        " 'Someone Like You' - Adele",
        " 'Let Her Go' - Passenger",
        " 'Heather' - Conan Gray"
    ],
    "angry": [
        " 'Smells Like Teen Spirit' - Nirvana",
        " 'Bad Guy' - Billie Eilish",
        " 'Lose Yourself' - Eminem"
    ],
    "inspirational": [
        " 'Believer' - Imagine Dragons",
        " 'Unstoppable' - Sia",
        " 'Hall Of Fame' - The Script"
    ],
    "chill": [
        " 'Sunflower' - Post Malone",
        " 'Yellow' - Coldplay",
        " 'Ocean Eyes' - Billie Eilish"
    ],
    "love": [
        " 'Perfect' - Ed Sheeran",
        " 'Just the Way You Are' - Bruno Mars",
        " 'Lover' - Taylor Swift",
        " 'Love me like you do' - Ellie Goulding"
      
    ]
}

messages = {
    "happy": "Happy mood , this song just to keep the good vibes going ",
    "sad": "Feeling sad!! It's ok here's the song just for you ",
    "angry":" Angry , Let this song sream with you",
    "chill":"Just chill with this song",
    "love":"This one's is just handpicked for you",
    "inspirational":"Woah!! Need a inspo boost? This song just for u"
}
print(" Mood-Based Song Recommender ")
print("Pick your mood ")
print("Moods: happy, sad, angry, chill, inspirational, love")
mood = input("How are you feeling today ? ").lower()

if mood in songs:
    print("\n" + messages[mood])
    print(random.choice(songs[mood]))
else:
    print("No songs based on that mood  Try: happy, sad, angry, chill, inspirational, or love ")

