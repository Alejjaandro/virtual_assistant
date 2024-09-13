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
    
        print("Adjusting noise...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        
        # Voice recognition
        try:
            speak("Te escucho")
            print("Escuchando...")
            audio = recognizer.listen(source, phrase_time_limit=20)
            
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
        except sr.WaitTimeoutError:
            print("Tiempo de espera agotado")
            speak("Tiempo de espera agotado")
            return "Vuélvelo a intentar"
        except:
            print("Error desconocido")
            speak("Error desconocido")
            return "Vuélvelo a intentar"
