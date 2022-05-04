"""                              _                 
      ___     __ _     _ __     | |__    ____      
     / __/   / _` |   | '_ \    |  _/   / __/      
    | (_    | (_| |   | |_) \   | |_    \__ \      
     \___\ ⍟ \__,_|▄⍟█| .__/██⍟▄ \__| ⍟ /___/ ⍟    
                 ████░|_|░░░░░████                 
               ███░░░▄▄█████▄▄░░░███               
              ██░░░██████─██████░░███              
             ██░░░██████───██████░░░██             
             ██░░███▄▄───────▄▄███░░██             
             ██░░██████─────██████░░██             
             ██░░█████──▄█▄──█████░░██             
             ██░░░███──▄███▄──███░░░██             
              ██░░░█████████████░░░██              
               ███░░░▀▀█████▀▀░░░███               
 CRYPTO ANALYSIS AND PROGRAMMATIC TRADING SOFTWARE 
                  ▀█████████████▀                  
""" 

import os
import sys
import inspect
import coinbase
import kraken
import notifications

from time import sleep as sleep
from colours import colours as colours
from splash import splash as splash



class CAPTS(object):

    menu_title = ""     # Initialize string: menu_title
    menu_options = {}   # Initialize array: menu_options
    menu_prompt = ""    # Initialize string: menu_prompt
    api = ""
    
### START: __init__()

    def __init__(self):
        self.clear_screen()
        self.set_menu("MAIN")
        self.main_menu()
#################################################### END: __init__()
### START: get_input(prompt)

    def get_input(self, prompt):
        user_input = input(colours().prompt(prompt))
        return user_input         
#################################################### END: get_input(prompt)
### START: print_header()

    def print_header(self):
        self.clear_screen()  # Clear console window
        print(colours().title("\n\t" + self.menu_title[1] + "\n\n"))   # Print menu title
#################################################### END: print_header()
### START: print_options()

    def print_options(self):
        for key, value in self.menu_options.items():
            if str(key) == 'SPACE':
                print()
            else:
                print("\t    " + colours().cyan(str(key)) + ": " + str(value))
        print()
#################################################### END: print_options()
### START: set_menu(menu_id)

    def set_menu(self, menu_id):
        global menu_title
        global menu_options
        
        if menu_id.upper() == "MAIN":   # If Main menu requested do the following
            self.menu_title = ["MAIN", 
                          "Crypto Analysis and Programmatic Trading Software (C.A.P.T.S.)"]
                          
            self.menu_options = {"1" : "Connect to Coinbase Pro API", 
                            "2" : "Connect to Kraken API",
                            "3" : "Notification Manager",
                            "SPACE" : "", 
                            "Q" : "Quit"}


#################################################### END: set_menu(menu_id)
### START: main_menu()

    def main_menu(self):
        self.set_menu("MAIN")
        
        while True:
            self.print_header()
            self.print_options()
            
            user_input = self.get_input("\n\tWhat would you like to do? : ")
            
            if user_input.upper() == "1" or user_input.upper() == "C":
                coinbase.cli()
            elif user_input.upper() == "2" or user_input.upper() == "K":
                kraken.kraken()
            elif user_input.upper() == "3" or user_input.upper() == "N":
                notifications.cli(sys.argv[0])
            elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                self.clear_screen()    # Clear console window
                exit(0)
#################################################### END: main_menu()

### START: clear_screen()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
#################################################### END: clear_screen()

if __name__ == '__main__':
    splash("OH_CANADA")
    #print(sys.argv[0])
    #sleep(5)
    CAPTS()
