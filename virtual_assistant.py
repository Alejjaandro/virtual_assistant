from config import *
from functions import * 
from commands import *
from spotify_command import *
# ========== Actions ==========
def ask_commands():
    
    greetings()
    
    end = False
    
    while not end:
        command = convert_speech_to_text().lower()
        # command = input("Command: ").lower()
        
        try:
            # Close
            for phrase in commands_to_close:
                if phrase in command:
                    speak("Hasta luego")
                    end = True
                    break
                else:
                    continue

            # Search in internet
            for phrase in commands_to_search_in_internet:
                if phrase in command:
                    ask_for_search(command)
                    continue
                else:
                    continue
                
            # Search in youtube
            for phrase in commands_to_search_in_youtube:
                if phrase in command:
                    ask_for_youtube(command)
                    continue
                else:
                    continue
                
            # Search in wikipedia
            for phrase in commands_to_search_in_wikipedia:
                if phrase in command:
                    ask_for_wikipedia(command)
                    continue
                else:
                    continue
                
            # Ask the day
            for phrase in commads_to_ask_day:
                if phrase in command:
                    ask_day()
                    continue
                else:
                    continue
                
            # Ask the hour   
            for phrase in commads_to_ask_hour:
                if phrase in command:
                    ask_hour()
                    continue
                else:
                    continue
                
            # Ask for screenshot
            # if 'toma una captura de pantalla' in command:
            #     filename = ask_screenshot()
            #     if not filename:
            #         continue
            #     else:
            #         speak(f"La imagen se ha guardado en {filename}")
            #         continue
                                
            # Ask for stocks prices        
            if 'precio de las acciones' in command:
                # Extract the name of the action
                action = command.split('precio de las acciones de ')[1].lower()
                # Get the price of the action
                precio = ask_price_action(action)
                if not precio:
                    speak("No se ha podido encontrar la acción, inténtalo de nuevo")
                    continue
                
                speak(f"El precio de las acciones de {action} es de {precio} dólares")
                continue
            
            # Spotify commands
            for phrase in commands_for_spotify["to open spotify"]:
                if phrase in command:
                    open_spotify()
                    continue
                else:
                    continue
            
            for phrase in commands_for_spotify["to play a song"]:
                if phrase in command:
                    play_song()
                    continue
                else:
                    continue
            
            for phrase in commands_for_spotify["to stop a song"]:
                if phrase in command:
                    stop_song()
                    continue
                else:
                    continue
            
            for phrase in commands_for_spotify["to move to next song"]:
                if phrase in command:
                    next_song()
                    continue
                else:
                    continue
            
            for phrase in commands_for_spotify["to move to previous song"]:
                if phrase in command:
                    previous_song()
                    continue
                else:
                    continue
                
        except:
            speak("No he podido entenderlo, inténtalo de nuevo")


ask_commands()