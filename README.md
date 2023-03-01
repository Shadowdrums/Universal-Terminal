# Universal-Terminal
a python tool to use multiple python programs in a single directory and its sub folders from 1 terminal

This program displays a menu of Python scripts located in the current directory and its subdirectories. It allows the user to select a script to run, copy a script to the Windows startup folder, or quit the program.

To start, the program gets the current directory and lists all Python scripts in the directory and its subdirectories. It stores the scripts' filenames, file paths, and first lines in a dictionary, which is used to display the menu options.

The program then enters a loop where it displays the menu options and prompts the user to enter a choice. If the user enters 'q', the program quits. If the user enters 'c', the program prompts the user to enter the number of the script they want to copy to the Windows startup folder.

If the user enters a valid script number, the program uses the shutil module to copy the selected script to the Windows startup folder. If the script is already in the startup folder, the program informs the user and prompts for another choice. If the script is successfully copied, the program informs the user.

If the user enters a valid script number that is not 'c', the program executes the selected script using the os.system function, which runs the script in a new shell. After the script finishes running, the program informs the user.

If the user enters an invalid choice, the program prompts for another choice.
