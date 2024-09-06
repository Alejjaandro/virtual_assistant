import datetime
import yfinance as yf
import pywhatkit
import wikipedia
import webbrowser

from config import speak
from stocks_info import stocks_info

def greetings():
    speak("Hola, ¿en qué puedo ayudarte?")
    
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

def ask_for_search(command):
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

def ask_for_youtube(command):
    command = command.split('youtube ')[1]
    speak("Buscando en YouTube")
    pywhatkit.playonyt(command)

def ask_for_wikipedia(command):
    try:
        command = command.split('wikipedia ')[1]
        speak("Buscando en Wikipedia")
        wikipedia.set_lang('es')
        sugestions = wikipedia.search(command)
        print(sugestions)
        
        if len(sugestions) > 0:
            command = sugestions[0]
            wiki = wikipedia.summary(command, 1)
            speak(wiki)
            webbrowser.open(f"https://es.wikipedia.org/wiki/{command}")
        else:
            speak("No se ha podido encontrar la información, inténtalo de nuevo")
            
    except:
        speak("No se ha podido encontrar la información, inténtalo de nuevo")

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
