from functions import * 
from commands import *
# ========== Actions ==========
def ask_commands():
    
    greetings()
    
    end = False
    
    while not end:
        # command = convert_speech_to_text().lower()
        command = input("Command: ").lower()

        for phrase in commands_to_search_in_internet:
            if phrase in command:
                ask_for_search(command)
                continue
            else:
                continue
            
        for phrase in commands_to_search_in_youtube:
            if phrase in command:
                ask_for_youtube(command)
                continue
            else:
                continue
        
        for phrase in commands_to_search_in_wikipedia:
            if phrase in command:
                ask_for_wikipedia(command)
                continue
            else:
                continue
        
        for phrase in commads_to_ask_day:
            if phrase in command:
                ask_day()
                continue
            else:
                continue
            
        for phrase in commads_to_ask_hour:
            if phrase in command:
                ask_hour()
                continue
            else:
                continue
                
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
               
        for phrase in commands_to_close:
            if phrase in command:
                speak("Hasta luego")
                end = True
                break
            else:
                continue


ask_commands()