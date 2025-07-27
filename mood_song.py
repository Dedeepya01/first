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

print(" Mood-Based Song Recommender ")
print("Pick your mood ")
print("Moods: happy, sad, angry, chill, inspirational, love")
mood = input("How are you feeling today ? ").lower()

if mood in songs:
    print("\nHere’s a song for your vibe today:")
    print(random.choice(songs[mood]))
else:
    print("No songs based on that mood  Try: happy, sad, angry, chill, inspirational, or love ")
