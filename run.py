from main import NameChanger
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__': 
    clear_console()
    print('\nWelcome in NameImageChanger!!! Please, write a access path to folder: ', end='')
    access_path = input()
    new_name = input('Write new name files: ')

    run = NameChanger(access_path, new_name)
    run.rename()