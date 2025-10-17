import sys
from colorama import Fore, Style, init
import time, os, random

init(autoreset=False)

for i in range(3):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("frame", i)
    time.sleep(0.4)

def typewriter(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()
def show_title():
    title = r"""

   ▄████████    ▄████████     ███     ███    █▄     ▄████████ ███▄▄▄▄  
  ███    ███   ███    ███ ▀█████████▄ ███    ███   ███    ███ ███▀▀▀██▄
  ███    ███   ███    █▀     ▀███▀▀██ ███    ███   ███    ███ ███   ███
 ▄███▄▄▄▄██▀  ▄███▄▄▄         ███   ▀ ███    ███  ▄███▄▄▄▄██▀ ███   ███
▀▀███▀▀▀▀▀   ▀▀███▀▀▀         ███     ███    ███ ▀▀███▀▀▀▀▀   ███   ███
▀███████████   ███    █▄      ███     ███    ███ ▀███████████ ███   ███
  ███    ███   ███    ███     ███     ███    ███   ███    ███ ███   ███
  ███    ███   ██████████    ▄████▀   ████████▀    ███    ███  ▀█   █▀ 
  ███    ███                                       ███    ███          
"""


    fade_steps = [
        Style.NORMAL + Fore.LIGHTRED_EX,
        Style.DIM + Fore.LIGHTBLACK_EX,
        Style.NORMAL + Fore.LIGHTWHITE_EX,
        Style.NORMAL + Fore.WHITE,
        Style.BRIGHT + Fore.RED,
        Style.BRIGHT + Fore.LIGHTRED_EX,
        Style.NORMAL + Fore.LIGHTRED_EX,
        Style.DIM + Fore.LIGHTBLACK_EX,
        Style.NORMAL + Fore.LIGHTWHITE_EX,
        Style.NORMAL + Fore.WHITE,
        Style.BRIGHT + Fore.RED,
        Style.BRIGHT + Fore.LIGHTRED_EX
    ]

    for color in fade_steps + fade_steps[::-1]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(color + title)
        time.sleep(0.05)

typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "What is your name, little Witch.: "),0.05
name = input()
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "Welcome " + name + ", have a fun trip back to wherever you died!", 0.05)
time.sleep(1)
stars = '.', ',', '`', '*', '|', '^', '+'
for i in range(160):
    print(random.choice(stars).rjust(random.randint(1, 140)))
    time.sleep(0.01)
show_title()

stars = '.', ',', '`', '*', '|', '^', '+'
for i in range(210):
    print(random.choice(stars).rjust(random.randint(1, 140)))
    time.sleep(0.01)
typewriter("""
                                      ▒░▓▒▓██░░▒ ░  ▓░░██▓▒▒░░                                      
                                   ░░▒▒█▓████████▒███████████░▒░                                    
                             ░░    ░█▓▓███████████████████████▓█░    ░                              
                            ░░█▒▓▓██████████████▓██▒██▓████████████▓▒▓ ░                            
                          ░▓▒ ▒█████████▓█▒▓▒█▒████▒███▒▒░███████████▒ ▓▒▒                          
                        ▒░█████▒▒████████▓▓██▒ ▒ █ █▓▓░██ ▓▒▓██████▒▒█████░▒                        
                       ░░██▓█████████▒██░▓▒ ░ ██  █ ░ ▓░█ █▒██▓████████▓███░░                       
                     ░█▒█▓█████████▓██▒▒░▒  █▒█ █ █    ████▒███▓█▒████████▓███░                     
                     ▒▒██▓▓█▒███▓▒░█████▒ ██▓░█ ░ █   ▒ █  ▓▒▓███ ▒████▒█▓▓██▒▒                     
                     ░██▓░▓▓▒█░█▒░▓▒▓▒▒░▓ ▓▓ ▓█ ██ ▒  ▓███ ▓░░▒▒▓▓░▒█ █▓▓█░▒██▒                     
                     ▓█▒░▒░░█░▓ ▒ ░▒░▒░ ░░█▒▓   ███░ ▒█▒▓ ▓▓ ░▒▒░░▓░ ▓░█░░▒▒▒█▓                      
                     ░ ▒█ ▓▓ ▒░█ ░▒ ░▒░  ▓░  ▒  ░████  ▓ ░▓  ░▓░ ▓░ ▓ ▒ ▓▓ █▒ ░                     
                       █▓ ▒░ ▒ ▒ ░▒ ▒ ░░ ▓░       ████    ▓ ░░░░ ▒  ▒ ▒ ░▒ ▓█                       
                      ░ ▒ █░ ░ ░    ▒ ░         ░████        ░ ░      ░  █ ░ ░                      
                       ░░░▓   █               ░░████                        ▓░                         
                       ▓  ▒                    █████                     ▓  █                       
                       ▒       ░▒▒▒▓███▓████████████████░░▓██████▒░▓        ▒                       
    ------------------- --░░▓██████████████████████████████████████████▒░----------------------                           
           --------------   ░░▒▒███████████████████████████████████▒░---------------------                               
     --------------------------- - ▓▓█░▓░▒▒▒ ▓██████▒ ░░ ░▓▓█▒▓▓ ░------------                                 
              ||||||||||||  ░░░░▒░▓ ░    ░▒░  ░▓▓▓▓-------░------▒░   ░░▒░░░                              
                                  ░░░░░▒░       ▒████-------------------------        
""", 0.00001)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "Your name is " + name + " and your dead", 0.05)
time.sleep(1)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "Kind of", 0.05)
time.sleep(1)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "and you are in Tierra de los Muertos, Land of the Dead", 0.05)
time.sleep(1)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "Under the Weeping Willow, your unconscious soul lays rest", 0.05)
time.sleep(1)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "-footsteps walk along the mirrored lake, floating off over you-", 0.05)
time.sleep(1)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "-A voice...divine and calm-", 0.05)
time.sleep(1)
typewriter (name + "...Its time to WAKE UP!", 0.05)
time.sleep(1.5)
typewriter ("-you wake up in a daze, you eyes wander up as you look at this radient figure before you-", 0.05)