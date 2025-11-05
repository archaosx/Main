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
    title = r"""        |            .                                                                                            
           ▓▓                         .      ^     .           |            .                                                               
           ▓█▓▓                                                                     .      ^     .                            
          ▓▓▓▓▓▓▓              .      ^     .            |                   .      ^     .                    |            .                                          
         ░▓▓▓▓▓▓▓▓▓                       ░▒▒▒                |            .                                      
         ▓▓▓▓▓▓▓▓▓▓▓▓              ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▒░                        .      ^     .                               
        ▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓░    ░▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓█▓▓▓▓▓▓▓▓▓░                                      
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓█▓▓▓▓░ ▓▓█▓▓▓▓▓▓▓▓                                     |            .
           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓█▓▓▓░ ░░   ▓▓▓▓▒  ░        |            .                         
             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░  ░░░▒░  ░▓▓▓▓▓  ▓▓░  ▓▓▓█  ▓▓▓▓                                  .      ^     .       
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▓▓▓▓▓▓▓█▒    ▓▓▓▓█       ▓▓▓▓   ▒▓▓▓▒▒▓                        
                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓ ░▓▓▓░ █▓    ▓▓▓▓▓▓         |            .                      
                   ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▒▓█▓        ▒▓▓ ▒▓▒                             
                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░    ▓▓▓         ▓▓▓▓▓▒                              .      ^     .          
                         ▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒               ▓ ▒            ▒▓▓▓░         |            .               
   |            .                                      ▒▓                                          
         .            |          .          |          .          .              |    ^           .
    
         .            ▄████████    ▄████████     ███     ███    █▄     ▄████████ ███▄▄▄▄      .                   .
   |          .       ███    ███ | ███    ███ ▀█████████▄ ███    ███   ███    ███ ███▀▀▀██▄                |
    ^       .         ███    ███   ███    █▀     ▀███▀▀██ ███    ███   ███    ███ ███   ███=        |                 
             |       ▄███▄▄▄▄██▀  ▄███▄▄▄         ███   ▀ ███    ███  ▄███▄▄▄▄██▀ ███   ███-              .      ^     .
   .              .  ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     .  ███  .  ███    ███ ▀▀███▀▀▀▀▀   ███   ███-      .                |
         .           ▀███████████   ███    █▄     ███     ███    ███ ▀███████████ ███   ███
 |          .         ███    ███   ███    ███     ███     ███    ███   ███    ███ ███   ███          ^     |       ^
         ^            ███    ███   ██████████    ▄████▀   ████████▀    ███    ███  ▀█   █▀     |            .
               |      ███    ███     |     .               ^           ███    ███                                .
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

typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "What is your name, little Witch: "),0.05
name = input()
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "What is your Title: "),0.05
name2 = input()
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + f"Welcome {name}, have a fun trip back to wherever you died!\n", 0.05)
time.sleep(1)
stars = '.', ',', '`', '*', '|', '^', '+'
for i in range(160):
    print(random.choice(stars).rjust(random.randint(1, 140)))
    time.sleep(0.01)
show_title()

print(Style.RESET_ALL)

stars = '.', ',', '`', '*', '|', '^', '+'
for i in range(210):
    print(random.choice(stars).rjust(random.randint(5, 140)))
    time.sleep(0.01)
typewriter("""                     .                             |          ^
                                       ░▒▓███▒ ░░░██████▒░▒▒░                .        +               |
   .                    .          ▒▓██████████████████████ ░▒▓█▓▓▒   |                     .          
                   .              ▒▒░▓████████████████████████▓▓░ ░                '                 .           ^
        .           .       ░▒▒████████▒██████████████████████████████████▓          .                      
             .           ▓█░███████████████████████████████████████████▓░░░      |           +       *      .
                    ░█████████████████████████████████████████████████▓███████                 |
             .     ░█▓▓██████████████████████████████████████████████████████          .          *
        ^         ░ ▓██░██████████████████▓████░████████████████████████████▓░                    .
  .            ░██▓█████████████████████████▓▒█▓██ █▒███████████████████████████▒██                          .
              ▒███████████████████████▓██▓▒██▒▓▓▒ ▒█ ▓█░████████████████████▒  ▓ ░▒        |      |
         |     █  ███████████████████████▓ █▒▓██▓█ ░  ▒█▓█▒██████████████████████░                   .         '
               ██████████████████████▓▒░░ █   ▓ ▓██  █░ ▓▒█░█████████████████████▒░    .             
            █▓▒███████████████████████▓█▓ ▒█  ▓▒▒█  █  █▒░█ █▓░██████████████████░▒▒              |              .
    .         ▒████████████████████████▓█ ▓  █░░█  ██▒    ▒█ ▓████████████████████▒   '              ^
            ▓▓████████████████████▒▓▓█ █  ████    ██      ██▓▓░█░██▓██▓█▓█▒███████▓▓                .
             ▓███████▓██████████▓█▓▒▓▓ █▓   ██░ ░███     ███▓▓   ▓ ▒█░██░█▒▓▓█████▓█▒       |               .       |
    .         ███▒▓██▓▒████ ██▒██▒█▒ █▒ █░ ▒██████▒     ███        █░██░▓▒░▓██▒██▒▓▓     .            .
       ^      ▒░█░▒██▓░███░▓██░█▓▒█░ █▒ ░    ████░   ▒████     .     █▓ ▒░░█░▓░█▒█░▒             +              .
         .    ░▓ ░██▒░▓██ ▓▓█░█▓ █  ▓░     .  ████▓███▓             ░█   ░█ ▓░█░█       '    .        .               ^
               ▓  ██░ ▓░  ░░█ ▓▓ █           ░█████░        ░██▒     █        █ ▓               .    
                 ░██  ▒    ░█ ░▓   ▓████     ███████▒  ▓███▓▒    |            █       *              .           .
      .             ▓██████░█░████▓████████████████████████████████████░█████░                      
              ▒█▓▓██████████▓██████▒█ ▒██████░ ▒███████████████████████████████▓░.........|..........                   
                   ██████████████████████████████████████████████████▓██████.............                  '
 ____________________  █████████▓░▒▒▓▓█████████████████████████▓▒  ░▒▓███.....................'...                   '   
__________________▒▓▓█▓▓▒     ▒▓██    ████████_______________▒░▒▒........    ████.....................            
             _________________________________________________________________________________________      '         
                   ________________________________________________________________________                                                                                                                                                                                 
""", 0.00001)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + f"Your name is {name} and you are dead.", 0.05)
time.sleep(0.7)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "Almost.", 0.05)
time.sleep(1.5)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "and you are in Tierra de los Muertos, The Land of the Dead", 0.05)
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
print(Style.RESET_ALL)
typewriter("Who are you?", 0.05)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"Diana: You know us as the Triple Goddess, Past, Present and Future intertwined into one magical being", 0.05)
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter(name + ": Hecate.", 0.05)
time.sleep(1)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"Diana: You however may call us Diana", 0.05)
time.sleep(1)
print(Style.RESET_ALL)
typewriter(name + ": Where are the other two? The other versions of you.", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"Diana: They may not be present, but they are always with me")
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter(name + ": Why are you here?" )
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"Diana: I want to make you an offer", 0.05)
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter(name + ": What kind of offer?", 0.05 )
time.sleep(1.5)

def next_scene():
    typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"Diana: Join us, Ascend the ranks and reside in my realm", 0.05)
    typewriter(" and be held in such high a stature you'd be worshipped.", 0.05)
    typewriter("Diana: OR")
    typewriter("Battle your way to the light, claw your way out of Hell and rejoin your friends in the battle against Leto", 0.05)
    typewriter("I must warn you, while dead your weak, your power is determined by your will")
    print("\nOptions")
    print("Yes. Accept the offer")
    print("No. Reject the offer")

choice = input("\nChoose Yes or No")
try:
    if choice == "Yes":
        print(Style.RESET_ALL)
        typewriter(name + ": I accept your offer, Diana", 0.05)
        time.sleep(1.5)
        typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-Diana smiles.-\n The Land Inbetween is the perfect place for one who wields your power, Little Witch", 0.05)
        typewriter(f"perfect for {name2}", 0.05)
        typewriter("You ascend to The Land Inbetween, your mortal journey ends here..Coward", 0.05)
        time.sleep(1.5)
        sys.exit()
    elif choice =="No":
        print(Style.RESET_ALL)
        typewriter(name + ": I fight to the end Diana and technically I am at the end, so now I gotta fight to the beginning. No matter my power", 0.05)
        time.sleep(1.5)
        typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-Diana smiles.-\n then take this. -she waves her hand and a pearl entrusted chain appears on your neck-", 0.05)
        time.sleep(1.5)
        typewriter("Diana: This will help you against the demons down there, now Dive, Dive until down becomes up", 0.05)
        time.sleep(1.5)
        typewriter("-You dive into the lake, and swim through the merky water as the light disappears-", 0.05)
        time.sleep(1.5)
        typewriter("Diana: swim until light becomes a simple memory", 0.05)
        time.sleep(1.5)
        typewriter("-The water becomes still..-", 0.05)
        time.sleep(1.5)
        typewriter("Diana: swim until...your doom.", 0.05)
        time.sleep(1.5)
except ValueError:
        print("Gotta follow the rules here, Witch.")

typewriter("-A red warping pulse reveals chains made from water around diana's hands and head connecting to the lake-", 0.05)
time.sleep(1.5)
typewriter("Diana: How did you make me do that.", 0.05)
time.sleep(1.5)
typewriter("-A hooded figure steps out from behind the willow tree-", 0.05)
time.sleep(1.5)
typewriter("Hooded Figure: You may be the Goddess of Magic. \nbut not the Goddess of mine. \nYou can go now, Little Witch ;)", 0.05)
time.sleep(1.5)
typewriter("Diana: Where are my sisters", 0.05)
time.sleep(1.5)
typewriter("Hooded Figure: You get them, when I say.", 0.05)
time.sleep(1.5)
typewriter("-The hooded figure waves their hand and the chains disperse back into water-", 0.05)
time.sleep(1.5)
typewriter(f"Hooded Figure: Now Go, and you will not mention a word to {name}", 0.05)
time.sleep(1.5)
typewriter("-The Hooded figure disappears in ashy glowing mist -", 0.05)

Bubbles = '0', 'o', '0', '*', '@', '^', '%'
for i in range(210):
    print(random.choice(Bubbles).rjust(random.randint(5, 300)))
    time.sleep(0.01)
typewriter("-The light from the surface disappears, bioluminescence light your way along the murky waters-", 0.05)
time.sleep(1.5)
typewriter("-You swim into the caverns underwater and you see a women, sitting on the rock bed-", 0.05)
time.sleep(1.5) 
typewriter("--", 0.05)
