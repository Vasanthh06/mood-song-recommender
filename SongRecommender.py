import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import random
from tkinter import ttk

# Predefined Song Database for different languages
songs_db = {
    "English": {
        "Happy": [
            ("Shape of You", "https://www.youtube.com/watch?v=JGwWNGJdvx8"),
            ("Happy", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
            ("Can't Stop the Feeling ", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
            ("Unstoppable","https://youtu.be/oS07d8Gr4tw")
        ],
        "Sad": [
            ("Someone Like You", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
            ("Let Her Go", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
            ("Fix You ", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
            ("Let me Down Slowly","https://youtu.be/jLNrvmXboj8")
        ],
        "Energetic": [
            ("Eye of the Tiger", "https://www.youtube.com/watch?v=btPJPFnesV4"),
            ("Stronger ", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
            ("Uptown Funk", "https://www.youtube.com/watch?v=OPf0YbXqDm0"),
            ("Believer","https://youtu.be/W0DM5lcj6mw")
        ],
        "Relaxing": [
            ("Weightless", "https://www.youtube.com/watch?v=UfcAVejslrU"),
            ("Sunset Lover", "https://www.youtube.com/watch?v=4uZb0-pF5nU"),
            ("Perfect", "https://www.youtube.com/watch?v=2Vv-BfVoq4g"),
            ("Love me Like you do","https://youtu.be/JrNMyzsYr4M")
        ]
    },
    "Kannada": {
        "Happy": [
            ("Aakasha Isthe","https://youtu.be/HfNtBJSkprk"),
            ("Dorassani","https://youtu.be/uN0AGOKNY-o"),
            ("Raktha Sambhandagala","https://youtu.be/5UfA_hGRGz0"),
            ("Maayavi","https://youtu.be/TMY1g8pAktk")
        ],
        "Sad": [
            ("777 Charlie","https://youtu.be/PubWT2Eg51w"),
            ("Bombe Adsonu","https://youtu.be/otNb9dP61EE"),
            ("Baanina Haniyu","https://youtu.be/xSJJTDrVrb0"),
            ("Once upon a time","https://youtu.be/hj_0Jd61XFI")
        ],
        "Energetic": [
            ("Vikranth Rona", "https://youtu.be/I3t9agGhWyI"),
            ("Jackie Jackie","https://youtu.be/9eShOnkYfUg"),
            ("Pankaja","https://youtu.be/8Bt5MP4WEwQ"),
            ("Mastu Mastu Hudgi","https://youtu.be/fozzwQ_ZS3U")
        ],
        "Relaxing": [
            ("Yenagali","https://youtu.be/twgEwLoswcs"),
            ("Naguva Nayana","https://youtu.be/AJSeaFthdeE"),
            ("Enunu Bekagidhe","https://youtu.be/fclPhO1FsOY"),
            ("Lullaby","https://youtu.be/4sQRTJdIMQo")
        ]
    },
    "Hindi": {
        "Happy": [
            ("Chittiyaan kalaiyaan","https://youtu.be/zpsVpnvFfZQ"),
            ("Tujh Mein Rab Diktha Hai", "https://youtu.be/qoq8B8ThgEM"),
            ("Chand Sifarish","https://youtu.be/zWEOx7TSM6I"),
            ("Yeh isaq hai","https://youtu.be/b_sCZbYyuO4")
        ],
        "Sad": [
            ("Agar tum Sath ho","https://youtu.be/pon8irRa8II"),
            ("Kaun Tujhe","https://youtu.be/Ov0YGGSY6gY"),
            ("Tum hi ho","https://youtu.be/Umqb9KENgmk"),
            ("Sanam teri Kasam","https://youtu.be/LOmC1dlZ2BE")
        ],
        "Energetic": [
            ("Dilbar","https://youtu.be/JFcgOboQZ08"),
            ("Nashe si Chandh Gayi","https://youtu.be/HoCwa6gnmM0"),
            ("Aaj ki rath","https://youtu.be/hxMNYkLN7tI"),
            ("Chikni Chameli","https://youtu.be/QcQpqWhTBCE")
        ],
        "Relaxing": [
            ("Kesariya","https://youtu.be/BddP6PYo2gs"),
            ("Zara Zara","https://youtu.be/NeXbmEnpSz0"),
            ("Yeh Raaten yeh Mausam","https://youtu.be/4HRC6c5-2lQ"),
            ("Heeriye","https://youtu.be/RLzC55ai0eo")
        ]
    },
    "Telugu": {
        "Happy": [
            ("Appudo Ippudo","https://youtu.be/X_HleAX9jVM"),
            ("Mirchi","https://youtu.be/VQ2-HPwxAZY"),
            ("Iddarammayiltho","https://youtu.be/NPnxw00z63I"),
            ("Pilla Gali","https://youtu.be/cRoGLfZ_-OQ")
        ],
        "Sad": [
            ("Oosupodu","https://youtu.be/e4N9al7vhVQ"),
            ("Nee Yadalo Naaku","https://youtu.be/VffosKXVZoY"),
            ("Oh Rendu Premalu","https://youtu.be/7BGTwvgxYtU"),
            ("Adiga","https://youtu.be/evbYFsSJ4pU")
                    ],
        "Energetic": [
            ("BlockBuster","https://youtu.be/FmjJ-e5uGuY?list=PLmSENmS6NCjUEHRbJ_us8o0zeMXoX26Nq"),
            ("Seeti maar","https://youtu.be/F5X694sak5U"),
            ("Ramoola ramoola","https://youtu.be/Bg8Yb9zGYyA"),
            ("Jigelu Rani","https://youtu.be/Fhfpa-6utR8")
        ],
        "Relaxing": [
            ("Inthandham","https://youtu.be/dOKQeqGNJwY"),
            ("Anaganaga oka uru","https://youtu.be/F3Td3_c96vo"),
            ("Kallu moosi yochisthey","https://youtu.be/-6uqH-0TiDk"),
            ("Hey Rangule","https://youtu.be/aPEdQ0G8GtY")
        ]
    }
}


# Separate list for audio songs
audio_songs_db = {
    "English": {
        "Happy": [
            ("Dandelions", "https://music.youtube.com/watch?v=HZbsLxL7GeM&si=8fsc3y7jSixSvdN5"),
            ("Shape of You", "https://music.youtube.com/watch?v=xTvyyoF_LZY&si=ApH0K_Wt-4OGdv1v")
        ],
        "Sad": [
            ("Let Me Down Slowly", "https://music.youtube.com/watch?v=50VNCymT-Cs"),
            ("Someone You Loved", "https://music.youtube.com/watch?v=bCuhuePlP8o")
        ],
        "Energetic": [
            ("Believer", "https://music.youtube.com/watch?v=W0DM5lcj6mw"),
            ("Thunder", "https://music.youtube.com/watch?v=fKopy74weus")
        ],
        "Relaxing": [
            ("Photograph", "https://music.youtube.com/watch?v=nSDgHBxUbVQ"),
            ("Perfect", "https://music.youtube.com/watch?v=2Vv-BfVoq4g")
        ]
    },
    "Telugu": {
        "Happy": [
            ("Pemaluu", "https://music.youtube.com/watch?v=Uz96yAcVFkE"),
            ("Rangule", "https://music.youtube.com/watch?v=SMyIKBtDFQE")
        ],
        "Sad": [
            ("Po Pove Ekantham", "https://music.youtube.com/watch?v=DtIiHizO3Lg&si=5B3gRS56Lbb-4N03"),
            ("Karige Loga", "https://music.youtube.com/watch?v=DV_WP62Oo4c&si=23AsrSVHOzGU54o3")
        ],
        "Energetic": [
            ("Private party", "https://music.youtube.com/watch?v=_WCQkPLiNro&si=yN2HuPekUCa-dPJ4"),
            ("Arabic Kuthu", "https://music.youtube.com/watch?v=9nRvqemGydw&si=tuZWrLlCPudLzO1w")
        ],
        "Relaxing": [
            #("Apudo Ipudo", "https://music.youtube.com/watch?v=zx1-Z5PJkfg&si=cI6psiwFOq82WvBz"),
            #("Inkem Inkem", "https://music.youtube.com/watch?v=rTNAIm6h1xo&si=aH0TZ6vl-Fx4Vg4v")
        ]
    },
    "Kannada": {
        "Happy": [
            ("madarangi yalli", "https://music.youtube.com/watch?v=3zSDtKlEpZI&si=WK3hUkToQxNAZt76"),
            ("Thara Thara", "https://music.youtube.com/watch?v=pG4l8KKEIDM&si=IdNKhrhecLuxYPZ3")
        ],
        "Sad": [
            ("Hesaru Poorthi", "https://music.youtube.com/watch?v=6XoZOpm6NOg&si=OuXRjxagjUA8VwUG"),
            ("Oh Manase Manase", "https://music.youtube.com/watch?v=TwolRGOSqPM&si=0Bi-migKcpVPIL5k")
        ],
        "Energetic": [
            ("Jackie jackie", "https://music.youtube.com/watch?v=kdfys_XeBBM&si=FltYntV9vTvT0mdV"),
            ("Jeeva Kannada", "https://music.youtube.com/watch?v=zKTMKKI_kjc&si=Pzz0zhJhvjjiIgIX")
        ],
        "Relaxing": [
            ("SojuGada", "https://music.youtube.com/watch?v=wzXM50C0x10&si=-32uRd6uofilHmbV"),
            ("Munjane Manjalli", "https://music.youtube.com/watch?v=oDyMLiIskPg&si=RhUgZ30iISkrvv17")
        ]
    },
    "Hindi": {
        "Happy": [
            ("Aankh Marey", "https://music.youtube.com/watch?v=Xhcvv3r9h_Y"),
            ("Jai Jai Shivshankar", "https://music.youtube.com/watch?v=gvyUuxdRdR4")
        ],
        "Sad": [
            ("Agar Tum Saath Ho", "https://music.youtube.com/watch?v=vwWl6o7PqL4"),
            ("Tujhe Bhula Diya", "https://music.youtube.com/watch?v=aDaFW0h1U_k")
        ],
        "Energetic": [
            ("Zinda", "https://music.youtube.com/watch?v=_o2rsLf24bA"),
            ("Bhaag Milkha Bhaag", "https://music.youtube.com/watch?v=EIyMQqZhzU8")
        ],
        "Relaxing": [
            ("Ae Dil Hai Mushkil", "https://music.youtube.com/watch?v=vUCM_0evdQY"),
            ("Raabta", "https://music.youtube.com/watch?v=wCZE4eCro6M")
        ]
    }
}

# Function to update moods dynamically when language is changed
def update_mood_dropdown(*args):
    selected_language = language_var.get()
    mood_menu['menu'].delete(0, 'end')  # Clear existing moods

    if selected_language in songs_db:
        available_moods = songs_db[selected_language].keys()
        for mood in available_moods:
            mood_menu['menu'].add_command(label=mood, command=tk._setit(mood_var, mood))
        mood_var.set(next(iter(available_moods)))  # Set first available mood

# Function to play a random song
def play_random_song():
    selected_language = language_var.get()
    selected_mood = mood_var.get()
    selected_type = type_var.get()

    song_source = songs_db if selected_type == "Video" else audio_songs_db

    if selected_language in song_source and selected_mood in song_source[selected_language]:
        if song_source[selected_language][selected_mood]:
            song, link = random.choice(song_source[selected_language][selected_mood])
            song_label.config(text=f"Now Playing: {song}", fg="white")
            webbrowser.open(link)
        else:
            song_label.config(text="No songs available for this mood.", fg="white")
    else:
        song_label.config(text="No songs available for this selection.", fg="white")

# ---------- GUI SETUP ----------
root = tk.Tk()
root.title("🎵 Mood-Based Song Recommender")
root.geometry("550x700")
root.configure(bg="#1e1e2e")

# ----------- HEADER -----------
title = tk.Label(root, text="🎧 Mood-Based Music Recommender", font=("Helvetica", 20, "bold"),
                 fg="#ffffff", bg="#1e1e2e", pady=20)
title.pack()

# ----------- LANGUAGE SELECTION -----------
section1 = tk.LabelFrame(root, text="Language", font=("Arial", 14), fg="white", bg="#2c2c3e")
section1.pack(padx=20, pady=10, fill="x")

language_var = tk.StringVar(value="English")
language_dropdown = ttk.Combobox(section1, textvariable=language_var, values=list(songs_db.keys()), state="readonly", font=("Arial", 12))
language_dropdown.pack(padx=10, pady=10)
language_var.trace("w", update_mood_dropdown)

# ----------- MOOD SELECTION -----------
section2 = tk.LabelFrame(root, text="Mood", font=("Arial", 14), fg="white", bg="#2c2c3e")
section2.pack(padx=20, pady=10, fill="x")

mood_var = tk.StringVar(value="Happy")
mood_menu = ttk.Combobox(section2, textvariable=mood_var, values=list(songs_db["English"].keys()), state="readonly", font=("Arial", 12))
mood_menu.pack(padx=10, pady=10)

# ----------- TYPE SELECTION -----------
section3 = tk.LabelFrame(root, text="Choose Type", font=("Arial", 14), fg="white", bg="#2c2c3e")
section3.pack(padx=20, pady=10, fill="x")

type_var = tk.StringVar(value="Video")
audio_radio = tk.Radiobutton(section3, text="Audio", variable=type_var, value="Audio", font=("Arial", 12), bg="#2c2c3e", fg="white", selectcolor="#444")
video_radio = tk.Radiobutton(section3, text="Video", variable=type_var, value="Video", font=("Arial", 12), bg="#2c2c3e", fg="white", selectcolor="#444")
audio_radio.pack(padx=10, pady=5)
video_radio.pack(padx=10, pady=5)

# ----------- PLAY BUTTON -----------
play_button = tk.Button(root, text="▶️ Play a Random Song", command=play_random_song,
                        font=("Arial", 14, "bold"), bg="#4e7eff", fg="white", padx=20, pady=10)
play_button.pack(pady=20)

# ----------- NOW PLAYING LABEL -----------
song_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#1e1e2e", fg="#ffffff", wraplength=400, justify="center")
song_label.pack(pady=20)

root.mainloop()
