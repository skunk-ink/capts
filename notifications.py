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

import smtplib
import ssl
import os
import inspect
import error_handler as error_handler
import subprocess

from sys import platform
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep as sleep
from colours import colours as colours

class email(object):
    # SMTP Settings: Using Protonmail Bridge
    SERVER = ''
    SMTP_SERVER = 'localhost'
    USERNAME = ''
    PASSWORD = ''
    PORT = 1025
    
    # Default Notification Settings
    NOTIFICATION = MIMEMultipart()
    EMAIL_FROM = 'bot@email'
    EMAIL_TO = 'your@email'
    SUBJECT = ""
    MESSAGE = ""
    
    # Trigger and Alert Settings
    CRYPTO_ID_PAIR = ''
    TRIGGER_TYPE = ''
    TRIGGER = 0.0

    def __init__(self, username = None, password = None):
        global SERVER
        global USERNAME
        global PASSWORD
        
        #input_ok = false
        
        #while input_ok == false:
        if username == None:
            self.USERNAME = EMAIL_FROM
        else:
            self.USERNAME = username
            
        if password == None:
            self.PASSWORD = 'yourpassword'
        else:
            self.PASSWORD = password
        
    def set_subject(self, subject):
        """
        Description:
        
            Set the subject message for the notification to be sent.
        
        Args: (*) Denotes required argument
        
         *  subject (string): Notification subject message
        """
        
        global SUBJECT
        
        self.SUBJECT = subject
        
    def set_message(self, message):
        """
        Description:
        
            Set the message for the notification to be sent.
            
        Args: (*) Denotes required argument
        
         *  message (string): Notification message
        """
        
        global MESSAGE
         
        self.MESSAGE = message
         
    def set_trigger(self, crypto_id_pair, trigger_type, trigger):
        """
        Description:
        
            Set the trigger action for auto-notification.
            
        Args: (*) Denotes required argument
        
         *  crypto_id_pair (string): ID name of the crypto-currency to monitor.
         *  trigger_type (string): Sets the type of trigger action. [trigger_type = GREATER | LESS | INCREASE | DECREASE | DEVIATE
         *  trigger (float): Price or Percentage change from current asset price.
        """
        
        global CRYPTO_ID_PAIR
        global TRIGGER_TYPE
        global TRIGGER
        
        self.CRYPTO_ID_PAIR = crypto_id_pair.upper()
        self.TRIGGER_TYPE = trigger_type.upper()
        self.TRIGGER = trigger
        
    def start(self):
        """
        Description:
        
            Start monitoring asset.
            
        Args:
            
            None
        """
        
        print(colours().error("notifications.notification.start() not yet complete."))
        sleep(2)
        return
        
    def stop(self):
        """
        Description:
            Stop monitoring asset.
            
        Args:
        
            None
        """
        
        print(colours().error("notification.notification.stop() not yet complete."))
        sleep(2)
        return
        
    def send(self, subject = None, message = None):
        """
        Description:
        
            Send notification.
            
        Args:
        
            None
        """
        global SUBJECT
        global MESSAGE
                
        if not subject == None:
            self.SUBJECT = str(subject)
            
        if not message == None:
            self.MESSAGE = str(message)
            
        self.NOTIFICATION['From'] = self.EMAIL_FROM
        self.NOTIFICATION['To'] = self.EMAIL_TO
        self.NOTIFICATION['Subject'] = self.SUBJECT
        
        self.NOTIFICATION.attach(MIMEText(self.MESSAGE, 'plain'))
        
        
        context = ssl.create_default_context()
        with smtplib.SMTP(self.SMTP_SERVER, self.PORT) as self.SERVER:
        
            self.SERVER.starttls()
            self.SERVER.login(self.USERNAME, self.PASSWORD)
            self.SERVER.sendmail(self.EMAIL_FROM, self.EMAIL_TO, self.NOTIFICATION.as_string())
            self.SERVER.quit()
            
        
    def send_test(self, subject = None, message = None):
        """
        Description:
        
            Send a test notification.
            
        Args:
            
            None
        """
        
        if subject == None or subject == "":
            self.set_subject("CAPTS E-Mail Notification Test")
        else:
            self.set_message(subject)
            
        if message == None or message == "":
            self.set_message("This is just a test of my e-mail notification system.")
        else:
            self.set_message(message)
            
            
        self.send()
        
        
        
class cli():
    DATA_PATH = ""
    
    if platform == 'linux':
        DATA_PATH = os.getcwd() + '/data/notifications/'      # Linux directory form
        
    elif platform == 'win32':
        DATA_PATH = os.getcwd() + '\data\\notifications\\'      # Linux directory form
        
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
                               
            self.OPTIONS = {"1" : "New Notification",
                            "2" : "Manage Notifications",
                            "3" : "Settings",
                            "4" : "Send Test",
                            "SPACE" : "",
                            "B" : "Back to C.A.P.T.S",
                            "Q" : "Quit"}
                            
            if self.CALLER == 'CAPTS':
                self.OPTIONS.pop('B')
                self.OPTIONS['Q'] = "Quit Notifications"
            
                                 
        elif menu_id.upper() == "NEW_NOTIFICATION":
            self.TITLE = ["NEW_NOTIFICATION",
                          "New Notification"]
            
            self.OPTIONS = {} # Handled in method
    ### END set_menu(menu_id)

    def main_menu(self):
        from CAPTS import CAPTS as CAPTS
        
        self.set_menu("MAIN_MENU")    # Initialize Notification System Menu

        try:
            while True:
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1" or user_input.upper() == "N":
                    self.new_notification()
                elif user_input.upper() == "4":
                    try:
                        print("\t    Sending email notification test ...", end=" ")
                        notification = email(EMAIL_FROM, PASSWORD)
                        notification.send_test()
                        print(colours().green("[OK]"))
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
    
    def new_notification(self):
        self.set_menu("NEW_NOTIFICATION")
        
        notification_options = {"Name" : "",
                                "Notification Type" : "",
                                "Trading Pair" : "",
                                "Trigger Type" : "",
                                "Trigger Price" : 0.00,
                                "Deviation Amount (%)" : 0.00}
        
        notification_name = "New Notification"        
        notification_type = "EMAIL"
        trading_pair = "BTC-USD"
        trigger_type = "GREATER"
        trigger = 0.00
        deviation = 0.00
               
        while True:
            self.print_header()
            
            notification_options["Name"] = str(notification_name).upper()
            notification_options["Notification Type"] = str(notification_type).upper()
            notification_options["Trigger Type"] = str(trigger_type).upper()
            notification_options["Trigger Price"] = float(trigger)
            notification_options["Deviation Amount (%)"] = float(deviation)
            
            index = 0
        
            for key, value in notification_options.items():
                index += 1
                
                #print("\t    " + colours().cyan(str(index)) + ": " + colours().cyan(str(key)) + " : " + str(value))
                
                if key == "Deviation Amount (%)":                
                    if trigger_type.upper() == "DEVIATE" or trigger_type.upper() == "DEVIATION":
                        print("\t    " + colours().cyan(str(index)) + ": " + colours().cyan(str(key)) + " : " + str(value))
                else:
                    print("\t    " + colours().cyan(str(index)) + ": " + colours().cyan(str(key)) + " : " + str(value))
            print()
            
            print("\t    " + colours().cyan("S") + ": Save")
            print("\t    " + colours().cyan("R") + ": Run Notification Daemon")
            print("\t    " + colours().cyan("K") + ": Kill Notification Daemon")
            print("\t    " + colours().cyan("B") + ": Back to Notifications")
            print("\t    " + colours().cyan("Q") + ": Quit")
            print()
            print()
            
            user_input = self.get_input("\tWhat would you like to do? : ")
            
            if str(user_input).upper() == "1" or str(user_input).upper() == "NAME":
                notification_name = self.get_input("\n\tEnter the Notification Name : ")
                notification_name = str(notification_name).upper()
            
            elif str(user_input).upper() == "2" or str(user_input).upper() == "NOTIFICATION TYPE":
                notification_type = self.get_input("\n\tEnter the Notification Type : ")
                notification_type = str(notification_type).upper()
                
            elif str(user_input).upper() == "3" or str(user_input).upper() == "TRIGGER TYPE":
                trigger_type = self.get_input("\n\tEnter the Trigger Type : ")
                trigger_type = str(trigger_type).upper()
                
            elif str(user_input).upper() == "4" or str(user_input).upper() == "TRIGGER PRICE":
                trigger = self.get_input("\n\tEnter the Trigger Price : ")
                trigger = int(trigger)
                
            elif str(user_input).upper() == "S" or str(user_input).upper() == "SAVE":
                with open((self.DATA_PATH + notification_name + '.cfg'), "w+") as cfg_file:
                    cfg_file.write("PID : " + "" + "\n")
                    cfg_file.write("NOTIFICATION_NAME : " + notification_name + "\n")
                    cfg_file.write("NOTIFICATION_TYPE : " + notification_type + "\n")
                    cfg_file.write("TRADING_PAIR : " + trading_pair + "\n")
                    cfg_file.write("TRIGGER_TYPE : " + trigger_type + "\n")
                    cfg_file.write("TRIGGER : " + str(trigger) + "\n")
                    cfg_file.write("DEVIATION : " + str(deviation) + "\n")
                    cfg_file.write("SUBJECT : " + "" + "\n")
                    cfg_file.write("MESSAGE : " + "" + "\n")
                    
            elif str(user_input).upper() == "R" or str(user_input).upper() == "RUN":
                with open((self.DATA_PATH + notification_name + '.cfg'), "w+") as cfg_file:
                    cfg_file.write("PID : " + "" + "\n")
                    cfg_file.write("NOTIFICATION_NAME : " + notification_name + "\n")
                    cfg_file.write("NOTIFICATION_TYPE : " + notification_type + "\n")
                    cfg_file.write("TRADING_PAIR : " + trading_pair + "\n")
                    cfg_file.write("TRIGGER_TYPE : " + trigger_type + "\n")
                    cfg_file.write("TRIGGER : " + str(trigger) + "\n")
                    cfg_file.write("DEVIATION : " + str(deviation) + "\n")
                    cfg_file.write("SUBJECT : " + "" + "\n")
                    cfg_file.write("MESSAGE : " + "" + "\n")
                    
                command = "cmd /k \"python notification_daemon.py \"{}\".cfg\"".format(notification_name)
                #print(command)
                #file_path = "notification_daemon.py \"" + notification_name + "\" \"" + notification_type + "\" \"" + trading_pair + "\" \"" + trigger_type + " " + trigger
                #os.startfile("notification_daemon.py", "python")
                
                os.system(command)
                #subprocess.call([r"python", file_path])
                sleep(5)
                #return
                
            elif str(user_input).upper() == "K" or str(user_input).upper() == "KILL":
                self.set_menu("MAIN_MENU")
                return
                
            elif str(user_input).upper() == "B" or str(user_input).upper() == "BACK":
                self.set_menu("MAIN_MENU")
                return
                
            elif str(user_input).upper() == "Q" or str(user_input).upper() == "EXIT" or str(user_input).upper() == "QUIT":
                self.clear_screen()
                exit(0)
            

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    ### END: clear_screen()
    
if __name__ == '__main__':
    cli() # Run Command Line Interface
    
