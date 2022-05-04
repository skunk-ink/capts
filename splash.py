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

import time
import os
from sys import platform
from colours import colours as colours

if platform == "linux":
    from getch import getch as getch
elif platform == "win32":
    from msvcrt import getch as getch

class splash(object):
    def __init__(self, theme):
        self.clear_screen()
        
        if theme.upper() == "CAP_AMERICA":
            self.cap_america()
        elif theme.upper() == "WINTER_SOLDIER":
            self.winter_soldier()
        elif theme.upper() == "OH_CANADA":
            self.oh_canada()

    ### START: clear_screen()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    #################################################### END: clear_screen()

    def cap_america(self):
        print()
        print()
        print()
        print(colours().white("\t                                                 _                   "))
        print(colours().white("\t                      ___     __ _     _ __     | |__    ____        "))
        print(colours().white("\t                     / __/   / _` |   |  _ \    |  _/   / __/        "))
        print(colours().white("\t                    | (_    | (_| |   | |_) \   | |_    \__ \        "))
        print(colours().white("\t                     \___\ ⍟ \__,_|") + colours().red("█") + colours().white("⍟") + colours().red("█") + colours().white("| .__/") + colours().red("█▄") + colours().white("⍟  \__| ⍟ /___/ ⍟      "))
        print(colours().red("\t                               ████") + colours().white_bg("░░░") + colours().white("|_|") + colours().white_bg("░░░") + colours().red("████                     "))
        print(colours().red("\t                             ███") + colours().white_bg("░░░") + colours().blue("▄▄█████▄▄") + colours().white_bg("░░░") + colours().red("███                   "))
        print(colours().red("\t                            ██") + colours().white_bg("░░░") + colours().blue("██████") + colours().white("─") + colours().blue("██████") + colours().white_bg("░░") + colours().red("███                  "))
        print(colours().red("\t                           ██") + colours().white_bg("░░░") + colours().blue("██████") + colours().white("───") + colours().blue("██████") + colours().white_bg("░░░") + colours().red("██                 "))
        print(colours().red("\t                           ██") + colours().white_bg("░░") + colours().blue("███▄▄") + colours().white("───────") + colours().blue("▄▄███") + colours().white_bg("░░") + colours().red("██                 "))
        print(colours().red("\t                           ██") + colours().white_bg("░░") + colours().blue("██████") + colours().white("─────") + colours().blue("██████") + colours().white_bg("░░") + colours().red("██                 "))
        print(colours().red("\t                           ██") + colours().white_bg("░░") + colours().blue("█████") + colours().white("──") + colours().blue("▄█▄") + colours().white("──") + colours().blue("█████") + colours().white_bg("░░") + colours().red("██                 "))
        print(colours().red("\t                           ██") + colours().white_bg("░░░") + colours().blue("███") + colours().white("──") + colours().blue("▄███▄") + colours().white("──") + colours().blue("███") + colours().white_bg("░░░") + colours().red("██                 "))
        print(colours().red("\t                            ██") + colours().white_bg("░░░") + colours().blue("█████████████") + colours().white_bg("░░░") + colours().red("██                  "))
        print(colours().red("\t                             ███") + colours().white_bg("░░░") + colours().blue("▀▀█████▀▀") + colours().white_bg("░░░") + colours().red("███                   "))
        print(colours().white("\t                 CRYPTO ANALYSIS AND PROGRAMMATIC TRADING SOFTWARE   "))
        print(colours().red("\t                                ▀█████████████▀                      "))
        print(colours().white("\t                                                                     "))
        print()
        print()
        print("\t\t\t                 press any key")
        print()
        print("\t\t\t             WHERE'S THE ANY KEY!?")
        
        getch()
        
    def winter_soldier(self):
        print()
        print()
        print()
        print(colours().white("\t                                                 _                   "))
        print(colours().white("\t                      ___     __ _     _ __     | |__    ____        "))
        print(colours().white("\t                     / __/   / _` |   |  _ \    |  _/   / __/        "))
        print(colours().white("\t                    | (_    | (_| |   | |_) \   | |_    \__ \        "))
        print(colours().white("\t                     \___\ ⍟ \__,_|") + colours().red("█") + colours().white("⍟") + colours().red("█") + colours().white("| .__/") + colours().red("█▄") + colours().white("⍟  \__| ⍟ /___/ ⍟      "))
        print(colours().red("\t                               ████") + colours().white("░░░|_|░░░") + colours().red("████                     "))
        print(colours().red("\t                             ███") + colours().white("░░░") + colours().red("▄▄█████▄▄") + colours().white("░░░") + colours().red("███                   "))
        print(colours().red("\t                            ██") + colours().white("░░░") + colours().red("██████") + colours().white("─") + colours().red("██████") + colours().white("░░") + colours().red("███                  "))
        print(colours().red("\t                           ██") + colours().white("░░░") + colours().red("██████") + colours().white("───") + colours().red("██████") + colours().white("░░░") + colours().red("██                 "))
        print(colours().red("\t                           ██") + colours().white("░░") + colours().red("███▄▄") + colours().white("───────") + colours().red("▄▄███") + colours().white("░░") + colours().red("██                 "))
        print(colours().red("\t                           ██") + colours().white("░░") + colours().red("██████") + colours().white("─────") + colours().red("██████") + colours().white("░░") + colours().red("██                 "))
        print(colours().red("\t                           ██") + colours().white("░░") + colours().red("█████") + colours().white("──") + colours().red("▄█▄") + colours().white("──") + colours().red("█████") + colours().white("░░") + colours().red("██                 "))
        print(colours().red("\t                           ██") + colours().white("░░░") + colours().red("███") + colours().white("──") + colours().red("▄███▄") + colours().white("──") + colours().red("███") + colours().white("░░░") + colours().red("██                 "))
        print(colours().red("\t                            ██") + colours().white("░░░") + colours().red("█████████████") + colours().white("░░░") + colours().red("██                  "))
        print(colours().red("\t                             ███") + colours().white("░░░") + colours().red("▀▀█████▀▀") + colours().white("░░░") + colours().red("███                   "))
        print(colours().white("\t                 CRYPTO ANALYSIS AND PROGRAMMATIC TRADING SOFTWARE   "))
        print(colours().red("\t                                ▀█████████████▀                      "))
        print(colours().white("\t                                                                     "))
        print()
        print()
        print("\t\t\t                 press any key")
        print()
        print("\t\t\t             WHERE'S THE ANY KEY!?")
        
        getch()

    def oh_canada(self):
        print()
        print(colours().white("\t                                       _                 "))
        print(colours().white("\t            ___     __ _     _ __     | |__    ____      "))
        print(colours().white("\t           / __/   / _` |   | '_ \    |  _/   / __/      "))
        print(colours().white("\t          | (_    | (_| |   | |_) \   | |_    \__ \      "))
        print(colours().white("\t           \___\ ⍟ \__,_|") + colours().red("▄") + colours().white("⍟") + colours().red("█") + colours().white("| .__/") + colours().red("██") + colours().white("⍟") + colours().red("▄") + colours().white(" \__| ⍟ /___/ ⍟    "))
        print(colours().red("\t                       ████") + colours().white_bg("░") + colours().white("|_|") + colours().white_bg("░░░░░") + colours().red("████                 "))
        print(colours().red("\t                     ███") + colours().white_bg("░░░") + colours().red(colours().white_bg("▄▄")) + colours().red("█████") + colours().red(colours().white_bg("▄▄")) + colours().white_bg("░░░") + colours().red("███               "))
        print(colours().red("\t                    ██") + colours().white_bg("░░░") + colours().red("██████") + colours().white_bg("─") + colours().red("██████") + colours().white_bg("░░") + colours().red("███              "))
        print(colours().red("\t                   ██") + colours().white_bg("░░░") + colours().red("██████") + colours().white_bg("───") + colours().red("██████") + colours().white_bg("░░░") + colours().red("██             "))
        print(colours().red("\t                   ██") + colours().white_bg("░░") + colours().red("███") + colours().red(colours().white_bg("▄▄")) + colours().white_bg("───────") + colours().red(colours().white_bg("▄▄")) + colours().red("███") + colours().white_bg("░░") + colours().red("██             "))
        print(colours().red("\t                   ██") + colours().white_bg("░░") + colours().red("██████") + colours().white_bg("─────") + colours().red("██████") + colours().white_bg("░░") + colours().red("██             "))
        print(colours().red("\t                   ██") + colours().white_bg("░░") + colours().red("█████") + colours().white_bg("──") + colours().red(colours().white_bg("▄")) + colours().red("█") + colours().red(colours().white_bg("▄")) + colours().white_bg("──") + colours().red("█████") + colours().white_bg("░░") + colours().red("██             "))
        print(colours().red("\t                   ██") + colours().white_bg("░░░") + colours().red("███") + colours().white_bg("──") + colours().red(colours().white_bg("▄")) + colours().red("███") + colours().red(colours().white_bg("▄")) + colours().white_bg("──") + colours().red("███") + colours().white_bg("░░░") + colours().red("██             "))
        print(colours().red("\t                    ██") + colours().white_bg("░░░") + colours().red("█████████████") + colours().white_bg("░░░") + colours().red("██              "))
        print(colours().red("\t                     ███") + colours().white_bg("░░░") + colours().red(colours().white_bg("▀▀")) + colours().red("█████") + colours().red(colours().white_bg("▀▀")) + colours().white_bg("░░░") + colours().red("███               "))
        print(colours().white("\t       CRYPTO ANALYSIS AND PROGRAMMATIC TRADING SOFTWARE "))
        print(colours().red("\t                        ▀█████████████▀                  "))
        print(colours().white("\t                                                         "))
        print(colours().white("\t                         press any key                   "))
        print(colours().white("\t                                                         "))
        print(colours().white("\t                     WHERE'S THE ANY KEY!?               "))
        print()
        
        getch()
        