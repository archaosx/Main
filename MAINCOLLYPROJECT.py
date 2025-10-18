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
time.sleep(0.7)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "Kind of", 0.05)
time.sleep(1.5)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "and you are in Tierra de los Muertos, Land of the Dead", 0.05)
time.sleep(1.5)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "Under the Weeping Willow, your unconscious soul lays rest.", 0.05)
time.sleep(1.5)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "-footsteps walk along the mirrored lake, floating off over you-", 0.05)
time.sleep(1.5)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "-A voice...divine and calm-", 0.05)
time.sleep(1.5)
typewriter ("Being: "+ name + "...Its time to WAKE UP!", 0.05)
time.sleep(1.5)
typewriter ("-you wake up in a daze, you eyes wander up as you look at this radient figure before you-", 0.05)
typewriter("-Her eyes glow with light and her skin looks as if your staring into the cosmos itself-", 0.05)
typewriter("-as you look at your surroundings questions form in your mind")

def start():
    print("As you look around to your surroundings two questions form in your mind..", 0.05)
    print("1. Where am I?")
    print("2. Who are you?")
    choice = input("Choose 1 or 2: ")
    if choice == "1":
        scenario_where_am_i()
    elif choice == "2":
        scenario_who_are_you()
    else:
        print("Gotta follow the rules here, Witch.")
        start()

def scenario_where_am_i():
    print("Being: You are in Tierra de los Muertos, The Land of the Dead, where you once lived, long ago", 0.05)
    print("Being: You were murdered by a rather sinister spell", 0.05)
    print(name + ": Wait what, no- I need to go back home")
    print("Being: Home is far away, we are deep within the crossroads between realms")
    print(name + ": then why can't i just force my way out")
    print("being: YOU CANT!-,")
    print(name + ": why")
    print("Being: This place contains some of the most vile creatures, unable to resurrect themselves like you")
    print("Being: And you have no control over your power output whilst dead")
    print(name + ": creatures like who-")