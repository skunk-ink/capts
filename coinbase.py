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
import cbpro
import error_handler as error
import notifications
import pandas as pd
import numpy as np
import plotly.graph_objs as go

from datetime import datetime
from plotly.offline import plot
from sys import platform
from time import sleep as sleep
from colours import colours as colours

DATA_PATH = ""

if platform == "linux":
    from getch import getch as getch
    DATA_PATH = os.getcwd() + '/data/'      # Linux directory format
elif platform == "win32":
    from msvcrt import getch as getch
    DATA_PATH = os.getcwd() + '\data\\'     # Windows directory format
            
""" Begin coinbase.api Class """
class api(object):

    # Global Variable Declaration

    public_client = ""
    private_client = ""

    ### START: __init__()
    def __init__(self):
        """
        Description:
        
            Initializations of the coinbase.api class.
        
        Args:
            None
        """
        
        global DATA_PATH
        global public_client
        global private_client
        
        key_file = DATA_PATH + 'keyfile.dat'
        key_ring = {}
        
        index = 0                                                               # Initialize int: key_index
        coinbase_keys = ["", "", ""]    
            
        with open(key_file, "r") as data_file:                                 # Open read-only file: data_file
            for line in data_file:                                              # Interate: data_file
                if line.upper().startswith('COINBASE_PRO'):                     # Check if line in file is an API key
                    key = line.strip('\n').split(' : ')                           # Split string at delimeter and initialize array: key
                    key_ring[index] = key                                       # Add key to the key_ring
                    index = index + 1                                   # Add one to key_index
        
        for key in key_ring:
            if key_ring[key][0].upper() == "COINBASE_PRO":
                coinbase_keys[0] = key_ring[key][1]
                coinbase_keys[1] = key_ring[key][2]
                coinbase_keys[2] = key_ring[key][3]
        
        self.public_client = cbpro.PublicClient()
        private_client = cbpro.AuthenticatedClient(coinbase_keys[0], coinbase_keys[1], coinbase_keys[2])
        
        # Sandbox API (Different Credentials)
        #private_client = cbpro.AuthenticatedClient(key, b64secret, passphrase, api_url="https://api-public.sandbox.pro.coinbase.com")

    ############################################################### END: __init__
    ### START: accounts()
    def accounts(self):
        """
        Description:
        
            Get data on all accounts available on the Coinbase PRO Exchange
        
        Args:
            None.
        """
        
        accounts = private_client.get_accounts()
        return accounts

    
    ############################################################### END: accounts()
    ### START: account(account_id)
    def account(self, account_id):
        """
        Description:
        
            Get data on a single account on the Coinbase PRO Exchange
        
        Args: (*) Denotes required argument
         *  account_id (string): Account ID of the account
        """
        account = private_client.get_account(account_id)
        return account
    
    ############################################################### END: account(account_id)
    ### START: buy(crypto, amount, fiat, order_type)
    def buy(self, crypto, amount, fiat=None, order_type=None):
        """
        Description:
        
            Buy crypto-currency with fiat-currency on the Coinbase PRO exchange.

        Args: (*) Denotes required argument
        
         *  crypto (string): ID name of the crypto-currency to buy.
         *  amount (float): Dollar amount of the crypto-currency to buy.
            fiat (string): ID name of the fiat-currency to sell. [default = USD]
            order_type (string): Type of order to contuct. Options are 'limit' or 'market'. [default = market]
        """
      
        # If no fiat-currency specified use 'USD'
        if fiat == None:
            fiat = 'USD'
            
        # Create product ID
        product_pair = crypto.upper() + "-" + fiat.upper()
        
        # If no order type specified use 'market'
        if order_type == None:
            order_type == 'market'

        # If limit order is placed
        if order_type == 'limit':
            sleep(1)
            
        # If market order is placed
        elif order_type == 'market':
            order_receipt = private_client.place_market_order(product_id=product_pair, side='buy', funds=amount)
            
        return order_receipt
        
    ############################################################### END: buy(crypto, amount, fiat, order_type)
    ### START: self(amount, crypto, fiat)
    def sell(self, amount, crypto, fiat=None):
        """
        Description:
        
            Sell crypto-currency for fiat-currency on the Coinbase PRO exchange.

        Args: (*) Denotes required argument
        
         *  amount (float): Dollar amount of the crypto-currency to sell.
         *  crypto (string): ID name of the crypto-currency to sell.
            fiat (string): ID name of the fiat-currency to buy. DEFAULT = USD
        """
        
        print(colours().error("sell(amount, crypto, fiat) method not yet complete."))
        sleep(1)
    
    ############################################################### END: sell(amount, crypto, fiat=None)
    ### START: trade(amount, from_crypto, to_crypto)
    def trade(self, from_crypto, to_crypto, amount=None, fiat=None):
        """
        Description:
        
            Trade one crypto currency for another on the Coinbase PRO exchange.

        Args: (*) Denotes required argument
        
            amount (float): Dollar amount of the crypto-currency to convert. DEFAULT = USD
         *  from_crypto (string): ID name the crypto-currency to convert.         
         *  to_crypto (string): ID name of crypto-currency you would like to buy.
        """
        
        print(colours().error("trade() method not yet complete."))
        sleep(1)
    
    ############################################################### END: trade(amount, from_crypto, to_crypto, fiat=None)
    ### START: ticker(crypto, fiat)
    def ticker(self, trading_pair):
        """
        Description:
        
            Collect ticker data from Coinbase Pro Exchange

        Args: (*) Denotes required argument
        
         *  crypto (string): ID name of crypto-currency
         *  fiat (string): ID name of fiat-currency
        """
        
        ticker_data = ""
        ticker_data = [['Time', ''],
                      ['Trade ID', ''],
                      ['Price', ''],
                      ['Bid', ''],
                      ['Ask', ''],
                      ['Size', ''],
                      ['Volume', '']]
                      
        data_index = 0
        element_index = 0
        
        data = self.public_client.get_product_ticker(product_id = trading_pair)
                
        for element in data:
            if element_index == 0:  # Trade ID
                ticker_data[1][1] = str(data[element])
            if element_index == 1:  # Price
                ticker_data[2][1] = str(data[element])
            if element_index == 2:  # Size
                ticker_data[5][1] = str(data[element])
            if element_index == 3:  # Time
                ticker_data[0][1] = str(data[element])
            if element_index == 4:  # Bid
                ticker_data[3][1] = str(data[element])
            if element_index == 5:  # Ask
                ticker_data[4][1] = str(data[element])
            if element_index == 6:  # Volume
                ticker_data[6][1] = str(data[element])
                   
            element_index = element_index + 1
        
        return ticker_data

    def historic_rates(self, trading_pair, start=None, end=None, granularity=None):
        """
        Description:
            Returns candle data on specified product.
            
        Args: (*) Denotes required argument
         *  trading_pair (string) : ID of the trading pair to retieve history on
            start (string) : Start time in ISO 8601
            end (string) : End time in ISO 8601
            granularity (int) : Desired timeslice in seconds. Options: 60, 300, 900, 3600, 21600, 86400
        """
        
        historic_data = self.public_client.get_product_historic_rates(trading_pair, start, end, granularity)
        return historic_data

""" Begin coinbase.web_socket Class """
class web_socket(object):
    
    def __init__(self):
        print(colours().error("coinbase.web_socket class not yet complete."))
        # See example in ./CAPTS/examples/web_socket_example.py
    
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["LTC-USD"]
        self.message_count = 0
        print("Lets count the messages!")
    def on_message(self, msg):
        self.message_count += 1
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"],
                   "\t@ {:.3f}".format(float(msg["price"])))
    def on_close(self):
        print("-- Goodbye! --")

""" Begin coinbase.graph Class """
class graph(object):
    HISTORIC_DATA_PATH = ""
    API = ""
    CANDLES = []
    TIME_DATA = []
    LOW_DATA = []
    HIGH_DATA = []
    OPEN_DATA = []
    CLOSE_DATA = []
    VOLUME_DATA = []
    EMA12 = []
    EMA26 = []
    MACD = []
    SIGNAL = []
    
    def __init__(self):
        
        global DATA_PATH   

        self.API = api()
                
    def ema12(self, values):
        values = np.array(values)
        return pd.ewm(values, span=12)[-1]
        
    def candle_graph(self, trading_pair):
        self.CANDLES = self.API.historic_rates(str(trading_pair).upper())
        print(self.CANDLES)
        
        for candle in self.CANDLES:
            self.TIME_DATA.append(datetime.utcfromtimestamp(int(candle[0])).strftime('%Y-%m-%d %H:%M:%S'))
            self.LOW_DATA.append(candle[1])
            self.HIGH_DATA.append(candle[2])
            self.OPEN_DATA.append(candle[3])
            self.CLOSE_DATA.append(candle[4])
            self.VOLUME_DATA.append(candle[5])
            
        fig = go.Figure(data=[go.Candlestick(x=self.TIME_DATA, open=self.OPEN_DATA, high=self.HIGH_DATA, low=self.LOW_DATA, close=self.CLOSE_DATA)])
        plot(fig, filename=DATA_PATH + trading_pair + '.html', auto_open=True)
        #webbrowser.open('file://' + 
        
    def write_csv(self):
        index = 0
        list_keys = ['time', 'low', 'high', 'open', 'close', 'volume']
        candles = []
        candle = {}

        for interval in self.CANDLES:
            candle = dict(zip(list_keys, interval))
            candles.append(candle)
                
        data_frame = pd.DataFrame(data=candles)
        data_frame.to_csv('data.csv')
        print('Data written to file')


""" Begin coinbase.py colsole interface """

class cli(object):
    coinbase_connection = ""
    menu_title = ""
    menu_options = ""

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
        print(colours().title("\n\t" + menu_title[1] + "\n\n"))   # Print menu title
    #################################################### END: print_header()
    ### START: print_options()

    def print_options(self):
        for option in menu_options:     # Print menu options to screen
            print("\t    " + option)
        print()
    #################################################### END: print_options()
    ### START: set_menu(menu_id)

    def set_menu(self, menu_id):
        global menu_title
        global menu_options
        
        if menu_id.upper() == "MAIN":
            menu_title = ["COINBASE_PRO_ACCOUNT_MANAGMENT",
                          "Coinbase PRO Account Managment"]
                          
            menu_options = [colours().cyan("1") + ": View Rolodex",
                            colours().cyan("2") + ": Automations / Bots",
                            colours().cyan("3") + ": Notifications",
                            colours().cyan("4") + ": Ticker",
                            colours().cyan("5") + ": Graph",
                            colours().cyan("6") + ": Buy",
                            colours().cyan("7") + ": Sell",
                            colours().cyan("8") + ": Send",
                            colours().cyan("9") + ": Receive",
                            "",
                            colours().cyan("B") + ": Back to C.A.P.T.S.",
                            colours().cyan("Q") + ": Quit"]
                   
        elif menu_id.upper() == "ROLODEX":
            menu_title = ["ACCOUNTS",
                          "Coinbase PRO Accounts Rolodex"]
                          
            menu_options = [] # Handled in coinbase_accounts_rolodex() method

        elif menu_id.upper() == "TICKER":       # If Ticker active do the following
            menu_title = ["TICKER",
                          ""]
                          
            menu_options = [""] # Handled in coinbase_ticker_window() method
            
        elif menu_id.upper() == "GRAPH":
            menu_title = ["GRAPH",
                         ""]
                         
            menu_options = [""] # Handled in method

    #################################################### END: set_menu(menu_id)
    ### START: main_menu()

    def main_menu(self):
        from CAPTS import CAPTS as CAPTS
        
        global coinbase_connection
        
        self.set_menu("MAIN")    # Initialize Coinbase PRO menu
        coinbase_connection = api()
        
        try:
            while True:
                self.print_header()
                self.print_options()
                
                user_input = self.get_input("\n\tWhat would you like to do? : ")
                
                if user_input.upper() == "1":
                    self.rolodex()
                    print(colours().error("coinbase_veiw_account() method not found."))
                    sleep(1)
                elif user_input.upper() == "2":
                    print(colours().error("creatures.creatures.cli() method not found."))
                    #creatures.cli()
                elif user_input.upper() == "3":
                    notifications.cli()
                elif user_input.upper() == "4":
                    self.ticker()
                elif user_input.upper() == "5":
                    self.coinbase_graph()
                elif user_input.upper() == "6":
                    self.buy()
                elif user_input.upper() == "7":
                    self.sell()
                elif user_input.upper() == "8":
                    self.send()
                elif user_input.upper() == "9":
                    self.receive()
                elif user_input.upper() == "B":
                    CAPTS()
                elif user_input.upper() == "EXIT" or user_input.upper() == "Q" or user_input.upper() == "QUIT":
                    self.clear_screen()    # Clear console window
                    exit(0)
        except AttributeError as e:
            print(colours().error(str(e)))
            sleep(2)
            self.main_menu()
        except KeyboardInterrupt:
            CAPTS()
    #################################################### END: main_menu()
    ### START: rolodex()

    def rolodex(self):
        global menu_title
        
        self.set_menu("ROLODEX")  # Initialize Coinbase Accounts menu
        index = 0                                       # Initialize rolodex index
        rolodex_cards = []                              # Initialize array for account ID's
        
        rolodex = coinbase_connection.accounts()             # Download account data

        # Add only active accounts to the rolodex
        for account in rolodex:
            if not float(account.get("balance")) == 0:
                rolodex_cards.append(str(account.get("id"))) # Add the new account ID to the array
        
        length = len(rolodex_cards)                 # Get the rolodex length
        index = 0                                   # Reset rolodex index counter
        
        # Start Rolodex Display loop
        try:
            while True:
                output = ""
                # Print account summary to screen
                for account in rolodex:
                    if account.get("id") == rolodex_cards[index]:
                        for key, value in account.items():
                            output += "\t > " + str(key)
                            
                            for i in range(16 - len(key)):
                                output += " "
                            
                            output += ": " + str(value) + "\n"
                                
                self.print_header()                             # Print the rolodex header
                print(output)
                print()
                print()
                    
                print("\tP = PREVIOUS  |  B = BACK  |  N = NEXT")
                    
                print()
                print()
              
                user_input = self.get_input("\tWhat would you like to do? : ")
                            
                if user_input.upper() == "P":
                    if index == 0:
                        index = length - 1
                    else:
                        index -= 1
                        
                elif user_input.upper() == "B":
                    self.main_menu()
                    
                elif user_input.upper() == "N":
                    if index == length - 1:
                        index = 0
                    else:
                        index += 1
        except KeyboardInterrupt:
            self.main_menu()
            pass
    
    #################################################### END: coinbase_accounts_rolodex()
    ### START: alerts()
    def alerts(self):
        return
    
    ### START: coinbase_ticker_window()

    def ticker(self):
        input_ok = False                                                    # Intitialize input_ok boolean
        trading_pair = ""                                                   # Initialize trading pair
                     
        try:
            trading_pair = self.get_input("\n\tEnter a trading pair : ")
            trading_pair = str(trading_pair).upper()

            self.set_menu("TICKER")
            menu_title[1] = "Viewing " + trading_pair + " Price Ticker"
                
            last_price = 0
            last_ask_price = 0
            last_bid_price = 0

            while True:
                
                self.clear_screen()  # Clear console window
                self.print_header()  # Print ticker header
                    
                divider = "\t"                                                  # Initialize divider
                ticker_data = coinbase_connection.ticker(trading_pair)      # Retrieve ticker data
                value_index = 0                                                 # Initialize value index counter
                
                string_length = len(ticker_data[0][1])
                string_length = string_length + 10
                
                for i in range(string_length):
                    divider = divider + '-'
                    
                print(divider)
                    
                for value in ticker_data:
                    output = ""
                    value1 = str(value[0])
                    value2 = str(value[1])
                        
                    if value_index == 1:
                        crypto = trading_pair.split("-")
                        output = "\t > " + value1 + ": " + value2 + " (" + str(crypto[0]).upper() + ")"
                        print(output)
                        
                    elif value_index == 2:
                        value_int = float(value2)
                            
                        if last_price > 0:
                            if last_price < value_int:
                                output = "\t > " + value1 + ": $" + colours().bold(colours().green(value2))
                                print(output)
                                    
                            elif last_price > value_int:
                                output = "\t > " + value1 + ": $" + colours().bold(colours().red(value2))
                                print(output)
                                    
                            else:
                                output = "\t > " + value1 + ": $" + value2
                                print(output)
                                    
                        else:
                            output = "\t > " + value1 + ": $" + value2
                            print(output)
                                
                        last_price = value_int
                            
                    elif value_index == 3:
                        value_int = float(value2)
                            
                        if last_bid_price > 0:
                            if last_bid_price < value_int:
                                output = "\t > " + value1 + ": $" + colours().bold(colours().green(value2))
                                print(output)
                                    
                            elif last_bid_price > value_int:
                                output = "\t > " + value1 + ": $" + colours().bold(colours().red(value2))
                                print(output)
                                    
                            else:
                                output = "\t > " + value1 + ": $" + value2
                                print(output)
                                    
                        else:
                            output = "\t > " + value1 + ": $" + value2
                            print(output)
                                
                        last_bid_price = value_int
                            
                    elif value_index == 4:                        
                        value_int = float(value2)
                            
                        if last_ask_price > 0:                            
                            if last_ask_price < value_int:
                                output = "\t > " + value1 + ": $" + colours().bold(colours().green(value2))
                                print(output)
                                    
                            elif last_ask_price > value_int:
                                output = "\t > " + value1 + ": $" + colours().bold(colours().red(value2))
                                print(output)
                                    
                            else:
                                output = "\t > " + value1 + ": $" + value2
                                print(output)
                                    
                        else:
                            output = "\t > " + value1 + ": $" + value2
                            print(output)
                                
                        last_ask_price = value_int
                            
                    else:
                        print("\t > " + value1 + ": " + value2)
                            
                    value_index = value_index + 1
                
                print(divider)
                print(colours().prompt("\n\tPress CTRL-C quit ticker : "))
                    
                sleep(1)
        except KeyboardInterrupt:
            self.main_menu()
            pass
            
    #################################################### END: ticker()
    ### START: graph()
    def coinbase_graph(self):
        self.set_menu = "GRAPH"
                        
        graph_options = {"Trading Pair" : "",
                         "Graph Type" : "",
                         "Start Date" : None,
                         "End Date" : None}
                         
        trading_pair = "BTC-USD"
        graph_type = "CANDLE"
        start_date = None
        end_date = None
        
        graph_options["Trading Pair"] = str(trading_pair).upper()
        graph_options["Graph Type"] = str(graph_type).upper()
        graph_options["Start Date"] = str(start_date).upper()
        graph_options["End Date"] = str(end_date).upper()
                    
        while True:
            self.print_header()
            
            index = 0
            
            for key, value in graph_options.items():
                index += 1
                print("\t    " + colours().cyan(str(index)) + ": " + str(key) + " = " + str(value))
                
            print()
            print("\t    " + colours().cyan("G") + ": Generate Graph")
            print("\t    " + colours().cyan("Q") + ": Quit")
            print()
            
            user_input = self.get_input("\tWhat would you like to do? : ")
            #user_input = str(user_input).upper()
            
            input_ok = False
            
            if user_input.upper() == "1" or user_input.upper().startswith("TRADING_PAIR"):
                trading_pair = self.get_input("\n\tEnter the trading pair to graph [default=BTC-USD] : ")
                graph_options["Trading Pair"] = str(trading_pair).upper()
            
            elif user_input.upper() == "2" or user_input.upper().startswith("GRAPH_TYPE"):
                graph_type = self.get_input("\n\tEnter the graph type [default=candle] : ")
                graph_options["Graph Type"] = str(graph_type).upper()
                
            elif user_input.upper() == "3" or user_input.upper().startswith("START_DATE"):
                start_date = self.get_input("\n\tEnter the start date (MM-DD-YYYY) [default=None] : ")
                graph_options["Start Date"] = str(start_date).upper()
                
            elif user_input.upper() == "4" or user_input.upper().startswith("END_Date"):
                end_date = self.get_input("\n\tEnter the end date (MM-DD-YYYY) [default=None] : ")
                graph_options["End Date"] = str(end_date).upper()
                
            elif user_input.upper() == "G" or user_input.upper() == "GRAPH":
                graph().candle_graph(trading_pair.upper())
                
            elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
                return
                    
                
    #################################################### END: graph()    
    ### START: buy()
    def buy(self):
        try:
            raise error.MethodNotFound()
                        
            input_ok = False                                                    # Intitialize input_ok boolean
            crypto = ""                                                         # Initialize crypto string
            amount = 0.00                                                       # Initiialize amount float
            fiat = ""                                                           # Initialize fiat string

            while input_ok == False:                                            # Prompt for Crypto ID
                crypto = self.get_input("\n\tEnter Crypto ID to purchase : ")
                    
                if crypto.isalpha():
                    input_ok = True
                        
            input_ok = False;
            
            while input_ok == False:
                fiat = self.get_input("\n\tEnter Fiat Currency ID used to buy [default = USD] : ")   # Prompt for Fiat Currency ID
                
                if fiat.isalpha() or fiat == "":
                    input_ok = True
                    
            while input_ok == False:
                amount = self.get_input("\n\tEnter the " + fiat + " dollar amount you'd like to buy : ")
                
                if fiat.isnumeric():
                    input_ok = True
                
            self.set_menu("TICKER")
            menu_title[1] = "Viewing " + crypto.upper() + "-" + fiat.upper() + " Price Ticker"
            
        except error.MethodNotFound:
            print(colours().error("coinbase.coinbase.buy() under development."))
            sleep(1)
            return
        except KeyboardInterrupt:
            return
    #################################################### END: buy(crypto, amount, fiat)
    ### START: clear_screen()
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    #################################################### END: clear_screen()

if __name__ == '__main__':
    cli()