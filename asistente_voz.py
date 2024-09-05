import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import webbrowser
import datetime
import wikipedia
from cartera_acciones import stocks_info

# ========== Texto to voice ==========
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ========== Voice to text ==========
def convert_speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
    
        recognizer.pause_threshold = 1
        print("Escuchando...")
        
        audio = recognizer.listen(source)
        
        # Voice recognition
        try:
            print("Recognizing...")
            petition = recognizer.recognize_google(audio, language='es-ES')
            print(f"User: {petition}")
            return petition
            
        except sr.UnknownValueError:
            print("No se ha podido reconocer la voz")
            speak("No he entendido lo que has dicho, inténtalo de nuevo")
            return "Vuélvelo a intentar"
        
        except sr.RequestError:
            print("Error en la conexión")
            speak("Error en la conexión")
            return "Vuélvelo a intentar"
        
        except:
            print("Error desconocido")
            speak("Error desconocido")
            return "Vuélvelo a intentar"
        
# ========== Actions ==========
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

def ask_commands():
    greetings()
    
    finish = False
    while not finish:
        # command = convert_speech_to_text().lower()
        command = input("Command: ").lower()
        
        if 'youtube' in command:
            speak("¿Qué quieres buscar en YouTube?")
            # command = convert_speech_to_text()
            command = input("Command: ").lower()
            pywhatkit.playonyt(command)
            continue
        
        elif 'abrir google' in command:
            speak("Abriendo Google")
            webbrowser.open('https://www.google.com')
            continue
        
        elif "día es hoy" in command:
            ask_day()
            continue
        
        elif "qué hora es" in command:
            ask_hour()
            continue
        
        elif "busca en wikipedia" in command:
            speak("Buscando en Wikipedia")
            
            # Remove the first phrase of the query
            command = command.replace("busca en wikipedia", "")
            print(command)
            wikipedia.set_lang("es")
            
            result = wikipedia.summary(command, sentences=1)
            speak("Según Wikipedia")
            speak(result)
            continue
        
        elif "busca en internet" in command:
            speak("Buscando en Google")
            command = command.replace("busca en internet", "")
            pywhatkit.search(command)
            speak("Esto es lo que he encontrado")
            continue
        
        elif 'precio de las acciones' in command:
            # Extract the name of the action
            action = command.split('precio de las acciones de ')[1].lower()
            # Get the price of the action
            precio = ask_price_action(action)
            if not precio:
                continue
            
            speak(f"El precio de las acciones de {action} es de {precio} dólares")
            continue
               
        elif 'eso es todo' in command:
            speak("Me piro, vampiro")
            break


ask_commands()