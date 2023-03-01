import os
import shutil

# Get the current directory
current_dir = os.getcwd()

# Get a list of all Python scripts in the current directory and its subdirectories
scripts = []
for root, dirs, files in os.walk(current_dir):
    for filename in files:
        if filename.endswith('.py') and not filename.startswith('__'):
            scripts.append(os.path.join(root, filename))

# Create a menu of available scripts
menu = {}
for i, script in enumerate(scripts):
    with open(script, 'r') as f:
        first_line = f.readline().strip()
        menu[i+1] = (os.path.relpath(script, current_dir), first_line)

# Display the menu options and provide the option to copy a script
while True:
    print('\nHere are the scripts you can run or copy to the startup folder:')
    for option, (script, description) in menu.items():
        print(f'{option}: {script} ({description})')
    
    print('\nEnter the number of the script you want to run or copy to the startup folder.')
    print('Type "q" to quit.')
    print('Type "c" to copy a script to the startup folder.')
    
    # Get the user's choice
    choice = input('> ')

    # Exit if the user chooses to quit
    if choice == 'q':
        print('Goodbye!')
        break
    
    # Allow the user to copy a script to the startup folder
    elif choice == 'c':
        script_choice = input('Enter the number of the script you want to copy to the startup folder: ')
        
        try:
            script_choice = int(script_choice)
        except ValueError:
            print("Oops! That wasn't a number. Please enter a number.")
            continue
        
        if script_choice not in menu:
            print("Sorry, I don't have a script for that number. Please choose a number from the menu.")
            continue
        
        script_path = menu[script_choice][0]
        script_name = os.path.relpath(script_path, current_dir)
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        destination_path = os.path.join(startup_folder, script_name)
        
        if os.path.exists(destination_path):
            print(f"{script_name} is already in the startup folder.")
            continue
        
        shutil.copy2(script_path, destination_path)
        print(f"{script_name} has been copied to the startup folder.")
    
    # Validate the user's choice
    else:
        try:
            choice = int(choice)
        except ValueError:
            print("Oops! That wasn't a number. Please enter a number or 'q' to quit.")
            continue

        if choice not in menu:
            print("Sorry, I don't have a script for that number. Please choose a number from the menu.")
            continue

        # Execute the selected script
        script_path = menu[choice][0]
        script_name = os.path.relpath(script_path, current_dir)
        print(f'Running "{script_name}"...')
        os.system(f'python "{script_path}"')
        print(f'"{script_name}" has finished.')
