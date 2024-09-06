import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser

from functions import speak


# Extract the keys from the env
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
scope = "user-modify-playback-state"

# Authenticate in Spotify
try:
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id, 
            client_secret=client_secret, 
            redirect_uri=redirect_uri, 
            scope=scope
            )
        )
except:
    pass

def open_spotify():
    try:
        speak("Abriendo Spotify")
        webbrowser.open("https://open.spotify.com/")
    except:
        speak("No se ha podido abrir Spotify")

def reproducir_playlist():
    pass

def stop_song():
    try:
        speak("Pausando cancion")
        sp.pause_playback()
    except:
        speak("No se ha podido pausar la cancion")
        
def play_song():
    try:
        speak("Reproduciendo cancion")
        sp.start_playback()
    except:
        speak("No se ha podido reproducir la cancion")
        
def next_song():
    try:
        speak("Cambiando a la cancion siguiente")
        sp.next_track()
    except:
        speak("No se ha podido reproducir la cancion")

def previous_song():
    try:
        speak("Volviendo a la cancion anterior")
        sp.previous_track()
    except:
        speak("No se ha podido reproducir la cancion")
    
