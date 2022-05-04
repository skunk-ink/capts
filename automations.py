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

# Note: This script needs to be made in to a daemon

import cbpro
import os
import time

from sys import platform
from datetime import datetime
from coinbase import api
from time import sleep as sleep
from colours import colours as colours

class brain(object):
    TIMESTAMP = ""
    CB_API = ""
    ID = 0
    DECISION = None       # Options: BUY, HOLD, SELL
    PRODUCT = ["BTC-USD"]   # Options: BTC-USD, ETH-USD, LTC-USD, BTC-EUR etc...
    ASSET_VALUE = 0.00
    ASSET_TREND = 0.00      # Trend represented as a slope value
    TRIGGER_HIGH = 0.00
    TRIGGER_LOW = 0.00
    
    EMA12 = 0.00
    EMA26 = 0.00
        
    def __init__(self):
    
        self.TIMESTAMP = self.timestamp()
        
        self.CB_API = api()

        if platform == "linux":
            self.DATA_PATH = os.getcwd() + '/data/automations/New Automation/'
            self.BRAIN = DATA_PATH + 'brain/'
            self.MEMORY = self.BRAIN + self.TIMESTAMP + '.mem'
            self.LOG_PATH = self.DATA_PATH + 'log/'
            self.COINBASE_EXCHANGE_DATA = self.DATA_PATH + 'data/historic_rates/' + self.TIMESTAMP + '.dat'
        elif platform == "win32":
            self.DATA_PATH = os.getcwd() + '\data\automations\New Automation\\'
            self.BRAIN = DATA_PATH + 'brain\\'
            self.MEMORY = self.BRAIN + self.TIMESTAMP + '.mem'
            self.LOG_PATH = self.DATA_PATH + 'log\\'
            self.COINBASE_EXCHANGE_DATA = self.DATA_PATH + 'data\historic_rates\\' + self.TIMESTAMP + '.dat'
        
        self.ID = 0
        self.DECISION = "HOLD"       # Options: BUY, HOLD, SELL
        self.PRODUCT = ["BTC-USD"]   # Options: BTC-USD, ETH-USD, LTC-USD, BTC-EUR etc...
        self.ASSET_VALUE = 0.00
        self.ASSET_TREND = 0.00      # Trend represented as a slope value
        self.TRIGGER_HIGH = 0.00
        self.TRIGGER_LOW = 0.00
        
        self.EMA12 = 0.00
        self.EMA26 = 0.00
    
    def main(self):
        
        
    def update(self):
        print(colours().error("creature.brain.update() method not yet complete."))

    def timestamp(self):
        ts = list(str(datetime.now()))
        i = 0
        
        for character in ts:
            if character == " ":
                ts[i] = "_"
                
            if character == ":":
                ts[i] = "-"
            
            i += 1
                
        ts = "".join(ts)
        
        return ts

        
class cli():
    CALLER = 'NONE'
    TITLE = ""
    OPTIONS = {}
    
    def __init__(self, caller = None):
        global CALLER
        
        if not caller == None:
            self.CALLER = caller
        
        self.clear_screen()
        self.set_menu("MAIN_MENU")
        self.main_menu()
    
            
    ### END __init__()
    
    def get_input(self, prompt):
        user_input = input(colours().prompt(prompt))
        return user_input
    ### END get_input(prompt)
    
    def print_header(self):
        self.clear_screen()  # Clear console window
        print(colours().title("\n\t" + self.TITLE[1] + "\n\n"))   # Print menu title
    ### END print_header()
        
    def print_options(self):
        for key, value in self.OPTIONS.items():
            if str(key) == 'SPACE':
                print()
            else:
                print("\t    " + colours().cyan(str(key)) + ": " + str(value))
        print()
    ### END set_menu(menu_id)
    
    def set_menu(self, menu_id):
        global TITLE
        global OPTIONS
        
        if menu_id.upper() == "MAIN_MENU":
            self.TITLE = ["MAIN_MENU",
                         "C.A.P.T.S. Notification System"]
                               
            self.OPTIONS = {"ID" : brain.ID,
                            "Name" : "New Creature",
                            "Products" : brain.PRODUCT,
                            "Asset Value" : brain.ASSET_VALUE,
                            "Trend" : brain.ASSET_TREND
                            "Decision" : brain.DECISION,
                            "SPACE" : "",
                            "B" : "Back to Automation Managment",
                            "Q" : "Quit"}
                            
            if self.CALLER == 'CAPTS':
                self.OPTIONS.pop('B')
                self.OPTIONS['Q'] = "Quit Automation"

    ### END set_menu(menu_id)

    def main_menu(self):
        from CAPTS import CAPTS as CAPTS
        
        self.set_menu("MAIN")    # Initialize Notification System Menu

        try:
            while True:
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper == "1" or user_input.upper() == "N":
                    print(colour.error("notifications.notification.new() method not yet complete."))
                elif user_input.upper() == "4":
                    try:
                        notification = email("capts_bot@protonmail.com", "D1ZyeRhs4pcZ7_i-Z-lDZg")
                        notification.send_test()
                        sleep(2)
                    except Exception as e:
                        print(colours().error(str(e)))
                        sleep(3)
                if user_input.upper() == "B":
                    if 'B' in self.OPTIONS:
                        CAPTS()
                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    self.clear_screen()    # Clear console window
                    exit(0)
        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
        except KeyboardInterrupt:
            if 'B' in self.OPTIONS:
                CAPTS()
            else:
                self.clear_screen()
                exit(0)
    ### END main_menu()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    ### END: clear_screen()
    