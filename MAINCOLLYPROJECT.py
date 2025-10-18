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

init(autoreset=True)

stars = '.', ',', '`', '*', '|', '^', '+'
for i in range(210):
    print(random.choice(stars).rjust(random.randint(1, 140)))
    time.sleep(0.01)
typewriter("""
                                .     ▒░▓▒▓██░░▒ ░  ▓░░██▓▒▒░░                        |              
        .            |              ░░▒▒█▓████████▒███████████░▒░                                    |
   |                            |  ░█▓▓███████████████████████▓█░    ░             *            .    
                            ░░█▒▓▓██████████████▓██▒██▓████████████▓▒▓ ░                            
       .        +          ░▓▒ ▒█████████▓█▒▓▒█▒████▒███▒▒░███████████▒ ▓▒▒                          *
                        ▒░█████▒▒████████▓▓██▒ ▒ █ █▓▓░██ ▓▒▓██████▒▒█████░▒                        
               |      ░░██▓█████████▒██░▓▒ ░ ██  █ ░ ▓░█ █▒██▓████████▓███░░            |           
                     ░█▒█▓█████████▓██▒▒░▒  █▒█ █ █    ████▒███▓█▒████████▓███░                             |
            .        ▒▒██▓▓█▒███▓▒░█████▒ ██▓░█ ░ █   ▒ █  ▓▒▓███ ▒████▒█▓▓██▒▒                 +    
                     ░██▓░▓▓▒█░█▒░▓▒▓▒▒░▓ ▓▓ ▓█ ██ ▒  ▓███ ▓░░▒▒▓▓░▒█ █▓▓█░▒██▒                     
     |               ▓█▒░▒░░█░▓ ▒ ░▒░▒░ ░░█▒▓   ███░ ▒█▒▓ ▓▓ ░▒▒░░▓░ ▓░█░░▒▒▒█▓           .           |
           .         ░ ▒█ ▓▓ ▒░█ ░▒ ░▒░  ▓░  ▒  ░████  ▓ ░▓  ░▓░ ▓░ ▓ ▒ ▓▓ █▒ ░                     
                       █▓ ▒░ ▒ ▒ ░▒ ▒ ░░ ▓░       ████    ▓ ░░░░ ▒  ▒ ▒ ░▒ ▓█                       .
      |               ░ ▒ █░ ░ ░    ▒ ░         ░████        ░ ░      ░  █ ░ ░                      
                       ░░░▓   █        |      ░░████      |       .         ▓░                         |
            |          ▓  ▒                    █████                     ▓  █             |          
                       ▒       ░▒▒▒▓███▓████████████████░░▓██████▒░▓        ▒                       .
    ------------------- --░░▓██████████████████████████████████████████▒░----------------------                           
           --------------   ░░▒▒███████████████████████████████████▒░---------------------                               
     --------------------------- - ▓▓█░▓░▒▒▒ ▓██████▒ ░░ ░▓▓█▒▓▓ ░------------                                 
              ||||||||||||  ░░░░▒░▓ ░    ░▒░  ░▓▓▓▓-------░------▒░   ░░▒░░░                              
                                  ░░░░░▒░       ▒████-------------------------        
""", 0.00001)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "Your name is " + name + " and you are dead.", 0.05)
time.sleep(0.7)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "Almost.", 0.05)
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
time.sleep(1.5)
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
    typewriter("Being: You are in Tierra de los Muertos, The Land of the Dead, where you once lived, long ago", 0.05)
    time.sleep(1.5)
    typewriter("Being: You were murdered by a rather sinister spell cast by my sister, Leto.", 0.05)
    time.sleep(1.5)
    typewriter(name + ": Wait what, no- I need to go back home", 0.05)
    time.sleep(1.5)
    typewriter("Being: Home is far away, we are deep within the crossroads between realms", 0.05)
    time.sleep(1.5)
    typewriter(name + ": then why can't i just force my way out", 0.05)
    time.sleep(1.5)
    typewriter("being: YOU CANT!-,", 0.05)
    time.sleep(1.5)
    typewriter(name + ": why", 0.05)
    time.sleep(1.5)
    typewriter("Being: This place contains some of the most vile creatures, unable to escape, unlike you", 0.05)
    time.sleep(1.5)
    typewriter("Being: And you have no control over your power output whilst dead, if you break out you risk letting them all out.", 0.05)
    time.sleep(1.5)
    typewriter(name + ": so how do I get out-", 0.05)
    time.sleep(1.5)
    typewriter("Being: before we get to that I want to make you an offer", 0.05)
    time.sleep(1.5)
    typewriter(name + ": What kind of offer?", 0.05)

def scenario_who_are_you():
    typewriter("Diana: You know us as the Triple Goddess, Past, Present and Future intertwined into one magical being", 0.05)
    time.sleep(1.5)
    typewriter(name + ": Hecate, The Goddess of Magic", 0.05)
    time.sleep(1)
    typewriter("Diana: You however may call us Diana", 0.05)
    time.sleep(1)
    typewriter(name + ": Where are the other two? The older versions of you.", 0.05)
    time.sleep(1.5)
    typewriter("Diana: They may not be present, but they are always with me")
    time.sleep(1.5)
    typewriter(name + ": Why are you here, have you come to stop me?" )
    time.sleep(1.5)
    typewriter("Diana: I want to make you an offer", 0.05)
    time.sleep(1.5)
    typewriter(name + ": What kind of offer?", 0.05 )
    time.sleep(1.5)

def next_scene():
    typewriter("Diana: Join us, Ascend the ranks and Surrender to the Hand of Hecate and eventually take up my mantle", 0.05)
    typewriter("Diana: OR")
    typewriter("Battle your way to the top, and claw your way out of Hell and rejoin your friends in the battle against Leto", 0.05)
