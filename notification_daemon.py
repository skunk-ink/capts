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

import os, os.path
import errno
import sys

from time import sleep as sleep
from sys import platform
from coinbase import api
from notifications import email
from colours import colours as colours

class notification(object):
    DATA_PATH = ""
    PID_PATH = ""
    
    # Notification Settings
    SUBJECT = ""
    MESSAGE = ""

    # Trigger and Alert Settings
    PID = ''
    NOTIFICATION_NAME = ""
    TRADING_PAIR = ''       # BTC-USD, ETH-USD, ETH-BTC, etc.
    TRIGGER_TYPE = ''       # GREATER | DEVIATE | LESS
    TRIGGER = 0.00
    DEVIATION = 0.00    # Can be either a price amount or percentage
    NOTIFICATION_TYPE = ""  # EMAIL | SMS
    
    def __init__(self):
        if platform == 'linux':
            self.DATA_PATH = os.getcwd() + '/data/notifications/'      # Linux directory form
        elif platform == 'win32':
            self.DATA_PATH = os.getcwd() + '\data\\notifications\\'      # Linux directory form
     
    @classmethod
    def init_trigger(self, pid, notification_name, notification_type, trading_pair, trigger_type, trigger):
        if platform == 'linux':
            self.DATA_PATH = os.getcwd() + '/data/notifications/'      # Linux directory form
        elif platform == 'win32':
            self.DATA_PATH = os.getcwd() + '\data\\notifications\\'      # Linux directory form
            
        self.PID = int(pid)
        self.NOTIFICATION_NAME = str(notification_name).upper()
        self.NOTIFICATION_TYPE = str(notification_type).upper()
        self.TRADING_PAIR = str(trading_pair).upper()
        self.TRIGGER_TYPE = str(trigger_type).upper()
        self.TRIGGER = float(trigger)
        #self.DEVIATION = float(deviation)
        #self.PID_FILE = PID_PATH + self.NOTIFICATION_NAME + '.pid'
        
        print(self.DATA_PATH)
        with open((self.DATA_PATH + notification_name + '.cfg'), "w+") as cfg_file:
            #cfg_file.write("PID_FILE : " + self.PID_FILE + "\n")
            cfg_file.write("PID : " + str(self.PID) + "\n")
            cfg_file.write("NOTIFICATION_NAME : " + self.NOTIFICATION_NAME + "\n")
            cfg_file.write("NOTIFICATION_TYPE : " + self.NOTIFICATION_TYPE + "\n")
            cfg_file.write("TRADING_PAIR : " + self.TRADING_PAIR + "\n")
            cfg_file.write("TRIGGER_TYPE : " + self.TRIGGER_TYPE + "\n")
            cfg_file.write("TRIGGER : " + str(self.TRIGGER) + "\n")
            #cfg_file.write("DEVIATION : " + str(self.DEVIATION) + "\n")
            cfg_file.write("SUBJECT : " + self.SUBJECT + "\n")
            cfg_file.write("MESSAGE : " + self.MESSAGE + "\n")

        print("-- Current Notification Setup --")
        print()
        print(" PID : " + str(self.PID))
        print(" NOTIFICATION_NAME : " + self.NOTIFICATION_NAME)
        print(" NOTIFICATION_TYPE : " + self.NOTIFICATION_TYPE)
        print(" TRADING_PAIR : " + self.TRADING_PAIR)
        print(" TRIGGER_TYPE : " + self.TRIGGER_TYPE)
        print(" TRIGGER : " + str(self.TRIGGER))
        print(" SUBJECT : " + self.SUBJECT)
        print(" MESSAGE : " + self.MESSAGE)
        
        #self.run()
        
    @classmethod
    def init_deviation(self, pid, notification_name, notification_type, trading_pair, trigger_type, trigger, deviation):
        if platform == 'linux':
            self.DATA_PATH = os.getcwd() + '/data/notifications/'      # Linux directory form
        elif platform == 'win32':
            self.DATA_PATH = os.getcwd() + '\data\\notifications\\'      # Linux directory form
            
        self.PID = int(pid)
        self.NOTIFICATION_NAME = str(notification_name).upper()
        self.NOTIFICATION_TYPE = str(notification_type).upper()
        self.TRADING_PAIR = str(trading_pair).upper()
        self.TRIGGER_TYPE = str(trigger_type).upper()
        self.TRIGGER = float(trigger)
        self.DEVIATION = float(deviation)
        
        print(self.DATA_PATH)
        with open((self.DATA_PATH + notification_name + '.cfg'), "w+") as cfg_file:
            cfg_file.write("PID : " + str(self.PID) + "\n")
            cfg_file.write("NOTIFICATION_NAME : " + self.NOTIFICATION_NAME + "\n")
            cfg_file.write("NOTIFICATION_TYPE : " + self.NOTIFICATION_TYPE + "\n")
            cfg_file.write("TRADING_PAIR : " + self.TRADING_PAIR + "\n")
            cfg_file.write("TRIGGER_TYPE : " + self.TRIGGER_TYPE + "\n")
            cfg_file.write("TRIGGER : " + str(self.TRIGGER) + "\n")
            cfg_file.write("DEVIATION : " + str(self.DEVIATION) + "\n")
            cfg_file.write("SUBJECT : " + self.SUBJECT + "\n")
            cfg_file.write("MESSAGE : " + self.MESSAGE + "\n")

        print("-- Current Notification Setup --")
        print()
        print(" PID : " + str(self.PID))
        print(" NOTIFICATION_NAME : " + self.NOTIFICATION_NAME)
        print(" NOTIFICATION_TYPE : " + self.NOTIFICATION_TYPE)
        print(" TRADING_PAIR : " + self.TRADING_PAIR)
        print(" TRIGGER_TYPE : " + self.TRIGGER_TYPE)
        print(" TRIGGER : " + str(self.TRIGGER))
        print(" DEVIATION : " + str(self.DEVIATION))
        print(" SUBJECT : " + self.SUBJECT)
        print(" MESSAGE : " + self.MESSAGE)
        
        #self.run()
        
    @classmethod
    def init_with_cfg(self, pid, file_path):

        self.PID = int(pid)
        
        with open(file_path, "r") as cfg_file:
            for line in cfg_file:
                if line.startswith('NOTIFICATION_NAME'):
                    temp = line.split(":")
                    self.NOTIFICATION_NAME = str(temp[1]).strip().upper()
                    
                elif line.startswith('NOTIFICATION_TYPE'):
                    temp = line.split(":")
                    self.NOTIFICATION_TYPE = str(temp[1]).strip().upper()
                    
                elif line.startswith('TRADING_PAIR'):
                    temp = line.split(":")
                    self.TRADING_PAIR = str(temp[1]).strip().upper()
                    
                elif line.startswith('TRIGGER_TYPE'):
                    temp = line.split(":")
                    self.TRIGGER_TYPE = str(temp[1]).strip().upper()
                    
                elif line.startswith('TRIGGER'):
                    temp = line.split(":")
                    self.TRIGGER = float(temp[1])
                    
                elif line.startswith('DEVIATION'):
                    temp = line.split(":")
                    self.DEVIATION = float(temp[1])
        
        print("-- Current Notification Setup --")
        print()
        print(" PID : " + str(self.PID))
        print(" NOTIFICATION_NAME : " + self.NOTIFICATION_NAME)
        print(" NOTIFICATION_TYPE : " + self.NOTIFICATION_TYPE)
        print(" TRADING_PAIR : " + self.TRADING_PAIR)
        print(" TRIGGER_TYPE : " + self.TRIGGER_TYPE)
        print(" TRIGGER : " + str(self.TRIGGER))
        print(" DEVIATION : " + str(self.DEVIATION))
        print(" SUBJECT : " + self.SUBJECT)
        print(" MESSAGE : " + self.MESSAGE)
        
        with open((self.DATA_PATH + self.NOTIFICATION_NAME + '.cfg'), "w+") as cfg_file:
            cfg_file.write("PID : " + str(self.PID) + "\n")
            cfg_file.write("NOTIFICATION_NAME : " + self.NOTIFICATION_NAME + "\n")
            cfg_file.write("NOTIFICATION_TYPE : " + self.NOTIFICATION_TYPE + "\n")
            cfg_file.write("TRADING_PAIR : " + self.TRADING_PAIR + "\n")
            cfg_file.write("TRIGGER_TYPE : " + self.TRIGGER_TYPE + "\n")
            cfg_file.write("TRIGGER : " + str(self.TRIGGER) + "\n")
            cfg_file.write("DEVIATION : " + str(self.DEVIATION) + "\n")
            cfg_file.write("SUBJECT : " + self.SUBJECT + "\n")
            cfg_file.write("MESSAGE : " + self.MESSAGE + "\n")

    def run(self, verbose=False):
        coinbase_api = api()
        email_notification = email()
        
        ticker_data = coinbase_api.ticker(self.TRADING_PAIR)
        update_count = 0
        
        while True:
            last_price = float(ticker_data[2][1])
            ticker_data = coinbase_api.ticker(self.TRADING_PAIR)
        
            self.clear_screen()
            
            update_count += 1
            
            if verbose == True:
                print("-- Current Notification Setup --")
                print()
                print(" PID : " + str(self.PID))
                print(" NOTIFICATION_NAME : " + self.NOTIFICATION_NAME)
                print(" NOTIFICATION_TYPE : " + self.NOTIFICATION_TYPE)
                print(" TRADING_PAIR : " + self.TRADING_PAIR)
                print(" TRIGGER_TYPE : " + self.TRIGGER_TYPE)
                print(" TRIGGER : " + str(self.TRIGGER))
                print(" DEVIATION : " + str(self.DEVIATION))
                print(" SUBJECT : " + self.SUBJECT)
                print(" MESSAGE : " + self.MESSAGE)
                print()
                print()
            
            if self.TRIGGER_TYPE.upper() == "GREATER":
                if float(last_price) <= float(self.TRIGGER) and float(ticker_data[2][1]) > float(self.TRIGGER):
                    if verbose == True: print(colours().yellow("Sending e-mail ..."), end = " ")
                        
                    email_notification.send(("ALERT: {0} GREATER THAN ${1:.2f}".format(self.TRADING_PAIR, self.TRIGGER)), ("CAPTS Alert: {0} = ${1:.2f}".format(self.TRADING_PAIR, float(ticker_data[2][1]))))
                   
                    if verbose == True: print(colours().green("[OK]"))
            
            elif self.TRIGGER_TYPE.upper() == "DEVIATE":
                deviation_amt = float(self.TRIGGER) * (float(self.DEVIATION) / 100)
                print("+: " + str(float(self.TRIGGER) + float(deviation_amt)))
                print("-: " + str(float(self.TRIGGER) - float(deviation_amt)))
                if float(ticker_data[2][1]) <= (float(self.TRIGGER) - deviation_amt) or float(ticker_data[2][1]) >= (float(self.TRIGGER) + deviation_amt):
                    if verbose == True: print("Deviation setting not ready")
                
            elif self.TRIGGER_TYPE.upper() == "LESS":
                if float(last_price) >= float(self.TRIGGER) and float(ticker_data[2][1]) < float(self.TRIGGER):
                    if verbose == True: print(colours().yellow("Sending e-mail ..."), end = " ")
                    email_notification.send(("ALERT: {0} LESS THAN ${1:.2f}".format(self.TRADING_PAIR, self.TRIGGER)), ("CAPTS Alert: {0} = ${1:.2f}".format(self.TRADING_PAIR, float(ticker_data[2][1]))))
                    if verbose == True: print(colours().green("[OK]"))
                            
            if verbose == True: print("Update " + str(update_count) + ": {0} ${1:.4f}".format(self.TRADING_PAIR, float(ticker_data[2][1])))

            sleep(1)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    ### END: clear_screen()
    
    def mkdir_p(self, path): # Taken from https://stackoverflow.com/a/600612/119527
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

    def safe_open(self, path):
        ''' Open "path" for writing, creating any parent directories as needed.
        '''
        self.mkdir_p(os.path.dirname(path))
        return open(path, "w+")
        
if __name__ == "__main__":
    notification_d = notification()
    # Collect the PID for this instance
    pid = str(os.getpid())
    
    if len(sys.argv) > 2:
        if str(sys.argv[4]).upper() == "GREATER" or str(sys.argv[4]).upper() == "LESS":
            notification_d.init_trigger(pid, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        elif str(sys.argv[4]).upper() == "DEVIATE":
            notification_d.init_deviation(pid, sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
        
        notification_d.run(verbose=True)
    else:
        notification_d.init_with_cfg(pid, sys.argv[1])
        notification_d.run(verbose=True)
        