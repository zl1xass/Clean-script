import time
from colorama import init, Fore, Back, Style
from termcolor import colored
import os

init()

def countdown():
    for i in range(5, 0, -1):
        print(colored(str(i), 'blue'))  
        time.sleep(1)
    print(colored("Welcome to Z1s Scripts", 'blue'))
    time.sleep(1)

def clear_linux():
    print(colored("Starting Arch Linux cleanup...", 'green'))
    os.system('sudo pacman -Syu')
    os.system('sudo pacman -Rns $(pacman -Qtdq)')
    os.system('sudo paccache -r')
    print(colored("Arch Linux cleanup completed.", 'green'))

def clear_windows():
    print(colored("Starting Windows cleanup...", 'blue'))
    os.system('del /q/f/s %TEMP%\\*')
    os.system('del /q/f/s %WINDIR%\\Temp\\*')
    print(colored("Windows cleanup completed.", 'blue'))

def main():
    countdown()

    while True:
        os_choice = input(colored("Which operating system are you using? (linux/windows): ", 'blue')).strip().lower()
        
        if os_choice == "linux":
            clear_linux()
            break
        elif os_choice == "windows":
            clear_windows()
            break
        else:
            print(colored("Invalid input, Please type < linux > or < windows >'.", 'red'))

if __name__ == "__main__":
    main()
