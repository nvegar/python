playlist = {"title" : "Soft Pop hits", 
"author" : "Nacor Vega", 
"songs" : [
    {"title": "I'm not the only one", "artist": ["Sam Smith"], "album": "In the lonely hour", "duration": 3.59},
    {"title": "Photograph", "artist": ["Ed Sheeran"], "album": "X", "duration": 4.19},
    {"title": "We don't talk anymore", "artist": ["Charlie Puth/ Selena Gomez"], "album": "Nine track mine", "duration": 3.38},
    {"title": "Hold my hand", "artist": ["Lady Gaga"], "album": "Hold my hand", "duration": 3.45},
    {"title": "A thousand years", "artist": ["Cristina Perri"], "album": "A thousand year", "duration": 4.45},
    {"title": "Perfect", "artist": ["Ed Sheeran"], "album": "Divide", "duration": 4.23},
    {"title": "All of me", "artist": ["John Legend"], "album": "Love in the future", "duration": 4.30},
    {"title": "Someone like you", "artist": ["Adele"], "album": 21 , "duration": 4.45},
    {"title": "When I was your man", "artist": ["Bruno Mars"], "album": "Unorthodox Jukebox", "duration": 3.34},
    {"title": "Girls like you", "artist": ["Maroon 5"], "album": "Red pill blues", "duration": 3.35},
    {"title": "Too at goodbyes", "artist": ["Sam Smith"], "album": "The thrill of it all", "duration": 3.21},
    {"title": "Just give me a reason", "artist": ["Pink/ Nate Rues"], "album": "The truth about love", "duration": 4.03},
    {"title": "You're beautiful", "artist": ["James Blunt"], "album": "Greatest Hits ever", "duration": 3.29},
    {"title": "Thinking out loud", "artist": ["Ed Sheeran"], "album": "X", "duration": 4.42},
    {"title": "Just the way you are", "artist": ["Bruno Mars"], "album": "Doo-wops and Hooligans", "duration": 3.41},
    {"title": "Set fire to the rain", "artist": ["Adele"], "album": 21, "duration": 4.03},
    {"title": "Rude!", "artist": ["Magic"], "album": "Rude", "duration": 3.45},
    {"title": "The scientist", "artist": ["Coldplay"], "album": "A rush of blood to the head", "duration": 5.10},
    {"title": "Love on the brain", "artist": ["Rihanna"], "album": "ANTI", "duration": 3.44},
    {"title": "Señorita", "artist": ["Shawn Mendes/ Camila Cabello"], "album": "Señorita", "duration": 3.11}
    ]
}

total_lenght = 0
for song in playlist["songs"]:
   total_lenght += song["duration"]

print(total_lenght / 24)