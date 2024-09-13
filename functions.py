from pathlib import Path
import datetime
import yfinance as yf
import pywhatkit
import wikipedia
import webbrowser
import pyautogui

from config import speak
from stocks_info import stocks_info

def greetings():
    speak("Hola, ¿en qué puedo ayudarte?")

# ASK DAY AND HOUR
def ask_day(): 
    dia = datetime.date.today()
    dia_semana = dia.weekday()
    
    calendario = {0: 'Lunes', 
                  1: 'Martes', 
                  2: 'Miércoles', 
                  3: 'Jueves', 
                  4: 'Viernes', 
                  5: 'Sábado', 
                  6: 'Domingo'}
    
    speak(f"Hoy es {calendario[dia_semana]}")

def ask_hour():
    hora = datetime.datetime.now()
    hora = f"{hora.hour}:{hora.minute}"
    
    speak(f"Son las {hora}")

# ASK FOR SEARCH IN WEB
def ask_for_search(command):
    if "abrir" or "abre" in command:
        speak("Abriendo Google")
        webbrowser.open('https://www.google.com')
    else:
        if 'google' in command:
            speak("Buscando en Google")
            command = command.split('google ')[1]
            pywhatkit.search(command)
            speak("Esto es lo que he encontrado")
        if 'internet' in command:
            command = command.split('internet ')[1]
            speak("Buscando en Internet")
            pywhatkit.search(command)
            speak("Esto es lo que he encontrado")

# ASK FOR SEARCH IN YOUTUBE
def ask_for_youtube(command):
    command = command.split('youtube ')[1]
    speak("Buscando en YouTube")
    pywhatkit.playonyt(command)

# ASK FOR SEARCH IN WIKIPEDIA
def ask_for_wikipedia(command):
    try:
        command = command.split('wikipedia ')[1]
        speak("Buscando en Wikipedia")
        wikipedia.set_lang('es')
        sugestions = wikipedia.search(command)
        
        if len(sugestions) > 0:
            command = sugestions[0]
            wiki = wikipedia.summary(command, 1)
            webbrowser.open(f"https://es.wikipedia.org/wiki/{command}")
            speak(wiki)
        else:
            speak("No se ha podido encontrar la información, inténtalo de nuevo")
            
    except:
        speak("No se ha podido encontrar la información, inténtalo de nuevo")

# ASK STOCKS PRICE
def ask_price_action(action):
    try: 
        # Search for the first ticker that contains the name of the action
        matches = [key for key in stocks_info.keys() if action in key]
        if len(matches) == 0:
            speak("No se ha podido encontrar la acción, inténtalo de nuevo")
            return
        
        # Get the ticker of the action
        action = matches[0]
        ticker = stocks_info[action]
        # Get the price of the action
        action = yf.Ticker(ticker)
        price = action.history(period='1d')['Close'][0]
        return round(price, 2)
    except:
        speak("No se ha podido encontrar la acción, inténtalo de nuevo")

# def ask_screenshot():
#     try:
#         speak("Tomando captura de pantalla")
#         screeshot_date = datetime.datetime.now()
#         filename = f"screeshot_{screeshot_date.day}-{screeshot_date.month}-{screeshot_date.year}_{screeshot_date.hour}:{screeshot_date.minute}:{screeshot_date.second}"
#         print(filename)
        
#         screenshot = pyautogui.screenshot()
#         file_path = Path.cwd() / filename
#         print(file_path)
#         screenshot.save(file_path, "PNG")
#         return filename
    
#     except:
#         speak("No se ha podido tomar la captura de pantalla, inténtalo de nuevo")