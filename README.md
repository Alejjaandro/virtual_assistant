# Welcome to my Virtual Assistant

This virtual assistant has been built completely with Pyton and works by voice.
You give it a command and it do your request.

It's not an AI assistant so the commands are harcoded, and will only recognize those written.

### The libraries used are:
[pyttsx3](https://pypi.org/project/pyttsx3/) -- [SpeechRecognition ](https://pypi.org/project/SpeechRecognition/) -- [yfinance](https://pypi.org/project/yfinance/) -- [pywhatkit](https://pypi.org/project/pywhatkit/) -- [wikipedia](https://github.com/goldsmith/Wikipedia) -- [Spotipy](https://spotipy.readthedocs.io/en/2.24.0/#)

### You can find all the accepted commands in the `commands.py` file (currently in spanish, but easy to change):
```
commands_to_search_in_internet = ["busca en internet", 
                              "buscar en internet", 
                              "busca en google", 
                              "buscar en google",
                              "abre google",
                              "abrir google"]

commands_to_search_in_youtube = ["busca en youtube",
                                 "buscar en youtube",
                                 "pon en youtube",
                                 "poner en youtube"]

commands_to_search_in_wikipedia = ["buscar en wikipedia",
                                 "busca en wikipedia"]

commads_to_ask_day = ["día es hoy",
                      "a qué día estamos",
                      "dime la fecha actual"]

commads_to_ask_hour = ["qué hora es",
                       "a qué hora estamos",
                       "dime la hora actual"]

commands_for_screenshot = ["toma una captura de pantalla", "captura la pantalla"]

commands_to_close = ["chao", "adiós", "hasta luego", "nos vemos", "eso es todo"]

commands_for_spotify = {
    "to open spotify": ["abre spotify", "abrir spotify"],
    "to play a song": ["sigue con la canción", "vuelve a reproducir", "vuelve a poner la cancion"],
    "to stop a song": ["pausa la canción", "para la canción"],
    "to move to next song": ["pasa la canción", "siguiente canción"],
    "to move to previous song": ["vuelve a la canción", "anterior canción", "canción de antes"]
}
```

## To change the language of the assistant you must go to `config.py` 
Look for the line:
```
petition = recognizer.recognize_google(audio, language='es-ES')
```
and change `language='es-ES'` to your language code.

## Don't forget to change also the Wikipedia language in `functions.py`:
```
wikipedia.set_lang('es')
```

## To use the Spotify commands you'll need to create an `.env` file like this:
```
CLIENT_ID = "##################"
CLIENT_SECRET = "###############"
REDIRECT_URI = "##############"
```
This are generated by [Spotify](https://developer.spotify.com/documentation/web-api) and will be used by [Spotipy](https://spotipy.readthedocs.io/en/2.24.0/#) to access your user info:
```
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
```
**To make the commands work you need to be listening to something in spotify, else you would get an error due to not device found (except the one that open spotify).**

Im not completely familiar with how [Spotify Web API](https://developer.spotify.com/documentation/web-api) works yet, and for now it only works for the commands established above.

## I am still working in adding more functionalities and looking hot to improve it, so I will keep upgrading it.

# Hope You enjoy it :)
