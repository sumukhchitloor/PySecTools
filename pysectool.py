import os
import subprocess
from colorama import Fore

while True:
    print(f"""{Fore.RED}   


 ██▓███ ▓██   ██▓  ██████ ▓█████  ▄████▄  ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓██░  ██▒▒██  ██▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██░ ██▓▒ ▒██ ██░░ ▓██▄   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▒██▄█▓▒ ▒ ░ ▐██▓░  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██▒ ░  ░ ░ ██▒▓░▒██████▒▒░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
▒▓▒░ ░  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░▒ ░     ▓██ ░▒░ ░ ░▒  ░ ░ ░ ░  ░  ░  ▒       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░░       ▒ ▒ ░░  ░  ░  ░     ░   ░          ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
         ░ ░           ░     ░  ░░ ░                   ░ ░      ░ ░      ░  ░
         ░ ░                     ░                                           

    """)

    scripts = [f for f in os.listdir() if f.endswith('.py') and f != 'main.py']

    for i, script in enumerate(scripts):

        script_name = os.path.splitext(script)[0]
        print(f'{i+1}. {script_name}')

    try:

        selection = int(input('Enter the number of the script to run (or press Ctrl+C to exit): '))

        if selection < 1 or selection > len(scripts):
            print('Invalid selection. Please choose a valid number.\n')
            continue

        # Get the name of the selected script
        script_name = scripts[selection-1]

        # Run the selected script using subprocess
        subprocess.run(['python', script_name])
    except ValueError:
      
        print('Invalid selection. Please enter a number.\n')
    except KeyboardInterrupt:
 
        break
