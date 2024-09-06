import pyttsx3
import speech_recognition as sr

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
