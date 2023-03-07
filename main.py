import os
import subprocess

while True:
    print('''

    __________         _________           ___________           .__          
    \______   \___.__./   _____/ ____   ___\__    ___/___   ____ |  |   ______
     |     ___<   |  |\_____  \_/ __ \_/ ___\|    | /  _ \ /  _ \|  |  /  ___/
     |    |    \___  |/        \  ___/\  \___|    |(  <_> |  <_> )  |__\___ \ 
     |____|    / ____/_______  /\___  >\___  >____| \____/ \____/|____/____  >
               \/            \/     \/     \/                              \/ 

    ''')

    # List all the Python scripts in the current directory
    scripts = [f for f in os.listdir() if f.endswith('.py') and f != 'main.py']

    for i, script in enumerate(scripts):
        # Get the name of the script without the extension
        script_name = os.path.splitext(script)[0]
        print(f'{i+1}. {script_name}')

    try:
        # Ask the user to enter the index of the script to run
        selection = int(input('Enter the number of the script to run (or press Ctrl+C to exit): '))

        # Check if the selection is a valid index
        if selection < 1 or selection > len(scripts):
            print('Invalid selection. Please choose a valid number.\n')
            continue

        # Get the name of the selected script
        script_name = scripts[selection-1]

        # Run the selected script using subprocess
        subprocess.run(['python', script_name])
    except ValueError:
        # Print an error message if the user enters non-numeric input
        print('Invalid selection. Please enter a number.\n')
    except KeyboardInterrupt:
        # Exit the loop if the user presses Ctrl+C
        break
