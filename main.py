print('''

__________         _________           ___________           .__          
\______   \___.__./   _____/ ____   ___\__    ___/___   ____ |  |   ______
 |     ___<   |  |\_____  \_/ __ \_/ ___\|    | /  _ \ /  _ \|  |  /  ___/
 |    |    \___  |/        \  ___/\  \___|    |(  <_> |  <_> )  |__\___ \ 
 |____|    / ____/_______  /\___  >\___  >____| \____/ \____/|____/____  >
           \/            \/     \/     \/                              \/ 

''')

import os
import subprocess
# List all the Python scripts in the current directory
scripts = [f for f in os.listdir() if f.endswith('.py') and f != 'main.py']

# Print a numbered list of the scripts
for i, script in enumerate(scripts):
    print(f'{i+1}. {script}')

# Ask the user to enter the index of the script to run
selection = int(input('Enter the number of the script to run: '))

# Get the name of the selected script
script_name = scripts[selection-1]

# Run the selected script using subprocess
subprocess.run(['python', script_name])
