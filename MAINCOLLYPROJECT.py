import sys
from colorama import Fore, Style, init, Cursor
import time, os, random
import shutil
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

def slash_animation(art, delay=0.04, slash_char='/'):
    lines = art.strip().splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)

    term_width = shutil.get_terminal_size().columns

    print("\n" * height)

    for step in range(width + height):
        print(Cursor.UP(height), end="")
        print(Cursor.FORWARD(0), end="")
        for y, line in enumerate(lines):
            chars = list(line.ljust(width))
            pos = step - y
            if 0 <= pos < width:
                chars[pos] = slash_char
            line_str = "".join(chars)
            padding = max((term_width - len(line_str)) // 2, 0)
            print(" " * padding + line_str)
        time.sleep(delay)



ascii_art_water = [

        "██▓ ███▄    █    ▄▄▄█████▓ ██   ██ ▓█████      ██████ ▓█████ ▄▄▄ ",
        "▓██  ██ ▀█  █    ▓  ██▒    ██   ██▒▓█   ▀    ▒██    ▒ ▓█     ████▄  ",
        "▒██  ██  ▀█ ██▒   ▒ ▓██  ▒░▒██▀▀██░▒███      ░ ▓██▄   ▒███   ██  ▀█▄  ",
        "░██  ██▒  ▐▌██▒   ░ ▓██  ░ ░▓█  ██ ▒▓█  ▄      ▒   ██▒▒▓█    ██▄▄▄▄██ ",
        "░██  ██░   ▓██░     ▒██  ░ ░▓█  ██▓░▒████▒   ▒██████▒▒░▒████ ▓█   ▓██▒",
        "░▓   ░▒░   ▒ ▒      ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░",
        "▒ ░░ ░░   ░ ▒░       ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░",
        "▒ ░   ░   ░ ░      ░       ░  ░░ ░   ░      ░  ░  ░     ░    ░   ▒ ",
        "░           ░              ░  ░  ░   ░  ░         ░     ░  ░     ░  ░",

        "▒█████    █████▒     ██████  ▒█████   █    ██  ██▓      ██████ ",
        "▒██▒  ██ ▓██   ▒    ▒██    ▒ ▒██▒  ██▒ ██  ▓██ ▓██▒    ▒██     ▒",
        "▒██░  ██ ▒████ ░    ░ ▓██▄   ▒██░  ██▒ ██  ▒██ ▒██░    ░ ▓██▄",
        "▒██   ██ ░▓█▒  ░      ▒   ██ ▒██   ██░ ▓█  ░██ ▒██░      ▒   ██▒ ",
        "░ ████▓▒ ░▒█░       ▒██████▒▒░ ████▓▒░ ▒█████▓ ░██████ ▒██████▒▒",
        "░ ▒░▒░▒░  ▒ ░       ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░ ",
        "░ ▒ ▒░  ░         ░ ░▒  ░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░░ ░▒  ░ ░",
        "░ ░ ░ ▒   ░ ░       ░  ░  ░  ░ ░ ░ ▒   ░░░ ░ ░   ░ ░   ░  ░",
        "░ ░                   ░      ░ ░     ░         ░  ░      ░",
]
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_water(water_lines, frames=50, delay=0.2):
    for _ in range(frames):
        clear_console()
        for line in water_lines:
            shift = random.randrange(-2, 2)
            shifted_line = " " * max(shift, 0) + line
            shifted_line = shifted_line[:len(line)]
            print(shifted_line)
        time.sleep(delay)

def show_title():
    title_art = r"""                       
                                  ░▒░░░░░░░░▒░                                                      
                              ░▒░              ░▒░                                                  
                            ░▒░                  ░▒                   ░░░░░░░                       
                           ░▒                     ░▒           ░▓███████▓▓███████▓░                 
                          ░▒              ░░      ░░       ░▒███░                ▒███░              
                          ░░   ░▓█      ░░     ░░      ░█▓░       ░░░░░░░░░       ░██░            
                           ░   █░       ▒     ░░░       ▒▓░     ▒██▓░░       ░░▒██▒░   ░█░           
                            ░▒ ▒▓       ░░              ░░   ░█▓░░                 ░░█▓  ░█░          
                             ░░ █░                       ░▒█░    ░░▒▓▓████▓▒░░░        ▒█ ░░▒          
              ░        ░▒▒▓▒░  ░░ ▓█░░░                ░█▓░ ░▓████████████████████▓░      █ ░░          
             ░      ░██████████░ ▒░ ░██░░▒░       ░▓▓▒░░▒█████████████▒░░░░░░░░▓█████░     ▓ ░          
             ▒     ▒████░  ░██▓█   ░▒░   ▒▓███████▒░▒███████████▓░                 ███▓    ░ █          
             ▓     ███▓       ▓█        ░░░░░░░░░████▓██████▓░                      ▒██░     ▓          
             ▒▒    ▓██▓   ▒███▒             ░███▓░░  ▓██▓░                           ██▒     ▓          
              ▒▓    ▓███░              ░▓███▓░░░    ░░░                             ▒██    ░ ▒          
               ░█▓░   ▒███████▓▓▓███████░░░▓░                            ░░        ░▓█▓    ░ ▒           
                  ░▓█▓▒░  ░░▒▒▒▒░░░░▒▓█▒░                                  ▒▓▒▒▒▒▓█▓░     ▒ ░            
                       ░░░░░▒░░░░░░                                                    ▒ ░             
                                                                                  ░ ░░ ░                  
    
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
    fade_steps = [ # this flashes the title giving a lightning effect
        Style.NORMAL + Fore.LIGHTRED_EX,
        Style.DIM + Fore.LIGHTBLACK_EX,
        Style.NORMAL + Fore.LIGHTWHITE_EX,
        Style.NORMAL + Fore.WHITE,
        Style.BRIGHT + Fore.RED,
        Style.NORMAL + Fore.LIGHTRED_EX,
        Style.DIM + Fore.LIGHTBLACK_EX,
        Style.NORMAL + Fore.LIGHTWHITE_EX,
        Style.NORMAL + Fore.WHITE,
        Style.BRIGHT + Fore.RED,
        Style.NORMAL + Fore.LIGHTRED_EX,
        Style.DIM + Fore.LIGHTBLACK_EX,
        Style.NORMAL + Fore.LIGHTWHITE_EX,
        Style.NORMAL + Fore.WHITE,
        Style.BRIGHT + Fore.RED,
        Style.BRIGHT + Fore.LIGHTRED_EX
    ]

    for color in fade_steps + fade_steps[::-1]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(color + title_art)
        time.sleep(0.05)


    return title_art
# Character name and Title
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "What is your name, little Witch: "),0.05
Player = input()
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "What is your Title: "),0.05
Player_Title = input()

#Player_Original_Powers_ = copy.deepcopy(Player_Powers) # this will replace the weaker powers with the OG powers

Scylla_Health = 600,
Scylla_Max_Health = 600,


init()
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + f"Welcome {Player}, have a fun trip back to wherever you died!\n", 0.05)
time.sleep(1)
stars = '.', ',', '`', '*', '|', '^', '+'
for i in range(210):
    print(random.choice(stars).rjust(random.randint(0, 140)))
    time.sleep(0.01)# this repeats the chosen symbols at the selected range

slash_animation(show_title())


print(Style.RESET_ALL)

stars = '.', ',', '`', '*', '|', '^', '+'
for i in range(210):
    print(random.choice(stars).rjust(random.randint(0, 140)))
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
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + f"Your name is {Player} and you are dead.", 0.05)
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
typewriter (Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f"Being: {Player}...Its time to wake up...", 0.05)
time.sleep(1.5)
typewriter (Style.BRIGHT + Fore.LIGHTRED_EX + "-you wake up in a daze, you eyes wander up as you look at this radient figure before you-", 0.05)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX + "-Her eyes glow with light and her skin looks as if your staring into the cosmos itself-", 0.05)
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter("Who are you?", 0.05)
typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"Diana: You know us as the Triple Goddess, Past, Present and Future intertwined into one magical being", 0.05)
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter(Player + ": Hecate.", 0.05)
time.sleep(1)
typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"Diana: You may call us Diana", 0.05)
time.sleep(1)
print(Style.RESET_ALL)
typewriter(Player + ": How do I know your Hecate, where are the other two.", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"Diana: They may not be present, but they are always with me")
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ She bends perception as she comes closer, shrinking in size. She holds are arms }-")
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"Diana: You can feel that can't you..")
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"You can trust me")
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ You feel a connection, like a breeze blowing on your soul }-")
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter(Player + ": Why are you here?" )
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"Diana: I want to make you an offer", 0.05)
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter(Player + ": What kind of offer?", 0.05 )
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"Diana: Join me, Ascend the ranks to the Crossroads and reside in my realm", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"You'd be worshipped for your gifts by cosmic beings")
time.sleep(1.5)
typewriter("Diana: OR")
typewriter("Battle your way to the light, claw your way out of Hell and rejoin your friends in the War", 0.05)
typewriter("I must warn you, while dead your weak, your power is determined by your will.")
print("\nOptions")
print("Yes. Accept the offer")
print("No. Reject the offer")


choice = input("\nChoose yes or no").strip().lower()
if choice == "yes":
    print(Style.RESET_ALL)
    typewriter(Player + ": I accept your offer, Diana", 0.05)
    time.sleep(1.5)
    typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"-Diana smiles.-\n The Land In between is the perfect place for one who wields your power, Little Witch", 0.05)
    typewriter(f"perfect for {Player_Title}", 0.05)
    typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ You ascend to The Land In between, your mortal journey ends here..Coward }-", 0.1)
    time.sleep(1.5)
    sys.exit()
elif choice =="no":
    typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"Guess I got to pick for you",0.06)
    time.sleep(1.5)
    print(Style.RESET_ALL)
    typewriter(Player + ": I fight to the end Diana and technically I am at the end, so now I gotta fight to the beginning. I don't care how weak I am now", 0.05)
    time.sleep(1.5)
    typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"-Diana nods.-\n then take this.", 0.05)
    time.sleep(1.5)
    typewriter(Style.BRIGHT + Fore.LIGHTRED_EX + "-{ A gold chain with black pearls appear on your neck }-")
    time.sleep(1.5)
    typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"Diana: This will help you against the creatures down there, now Dive, Dive until down becomes up", 0.05)
    time.sleep(1.5)
    typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ You dive into the lake, and swim into the deep abyss }-", 0.05)
    time.sleep(1.5)
    typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"Diana: swim until light becomes a simple memory", 0.05)
    time.sleep(1.5)
    typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ The water becomes still.. }-", 0.05)
    time.sleep(1.5)
    typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"Diana: swim until...your doom.", 0.05)
    time.sleep(1.5)

print(Style.RESET_ALL)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ A red warping pulse reveals chains made from water around diana's hands and neck connecting to the lake }-", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX +"Diana: How did you make me do that.", 0.05)
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ A hooded figure steps out from behind the willow tree }-", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTBLACK_EX +"Hooded Figure: You may be the Goddess of Magic. \nbut not the Goddess of mine. \nYou can go now, Little Witch ;)", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "Diana: Where are my sisters", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTBLACK_EX +"Hooded Figure: You get them, when I say.", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ The hooded figure waves their hand and the chains disperse back into water }-", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTBLACK_EX +f"Hooded Figure: Now Go, and you will not mention a word to {Player}", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ The Hooded figure disappears in ashy glowing mist }-", 0.05)

time.sleep(1.5)

animate_water(ascii_art_water)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ The light from the surface disappears, you form a ball of light in your hand to light the way }-", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ You swim into the caverns underwater and you see a women, sitting on the rock bed }-", 0.05)
time.sleep(1.5) 
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ you swim forward to her and reach for her shoulder to check if she's ok }-", 0.05)
time.sleep(0.5)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ The necklace Hecate apparently allows you to breathe underwater }-", 0.05)
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"Hey are you-", 0.05)
typewriter("-{ Her hand grabs yours with astonishing strength and she launches you towards the cave wall }-", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTGREEN_EX +"You are hurtled into the save wall, your wounded but you heal quickly", 0.05)
time.sleep(0.6)
typewriter(Style.BRIGHT + Fore.LIGHTGREEN_EX +"Your Health is back to 300", 0.05)
time.sleep(0.6)
print(Style.RESET_ALL)
typewriter("-{ you groan }- Ok. that hurt", 0.05)
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter("-A hand slams down onto the wall next to you-", 0.05)
time.sleep(1)
typewriter(Style.BRIGHT + Fore.LIGHTBLUE_EX +"???: its been a while since I've seen someone as delicious as you swim through here", 0.05)
time.sleep(1.5)
typewriter("And a rather powerful one here, but somethings dimming your flavor", 0.05)
print(Style.RESET_ALL)
typewriter("-You summon a repulsive blast straight into her stomach and send her flying through the air-", 0.05)
time.sleep(1.5)

# put power here

print(Style.RESET_ALL)
typewriter("-{ A blur whizzes through the water and warps itself at the entrance creating a current that launches you backwards into her grasp }-", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTBLUE_EX +"???: First off all. OW. Second, How rude of you, you witches treat everyone so terribly.", 0.05)
time.sleep(1.5)
print(Style.RESET_ALL)
typewriter("-{ She notices the chain around your neck }-", 0.05)
time.sleep(1.5)
typewriter(Style.BRIGHT + Fore.LIGHTBLUE_EX + "???: This is lovely, mind if I take it for your insubordination -she reaches for it-.", 0.05)
time.sleep(1.5)
# add combat option
print(Style.RESET_ALL)
typewriter("-{ you blast her away again and she hits the rocks }-.", 0.05)
time.sleep(1.5)

# put power here


print(Style.RESET_ALL)
typewriter("-{ You sent her crashing int the rock causing an uproar of debris }-.", 0.05)
time.sleep(1.5)
typewriter("You threw me into a wall and tried to rob me, maybe you deserve how witches treated you.", 0.05)
time.sleep(1.5)
typewriter("and who the hell- are you.", 0.05)
time.sleep(1.5)
typewriter("-{ The women is gone from the rocks, you look around but its too dark, you summon an orb of light }-", 0.05)
time.sleep(1.5)
typewriter("-{ The cavern is much bigger now that you actually look around, you cant even see the bottom }-", 0.05)
time.sleep(1.5)
typewriter("-{ 2 glowing dots appear in the dark like eyes, \n then another 10 }-", 0.05)
time.sleep(1.5)
typewriter("-{ The creature comes forward, a 6 headed hydra like creature with tons of tentacles charges forward }-", 0.05)
time.sleep(1.5)
typewriter("""
                                                                          ░░        ░░░  ░▒▒▓▓░           
                                                                       ▒░░▒▓▓▒    ▒░                  
                                                                     ░░░░▓▒▒▓░  ░░ ░░░░░░░▓░              
                                                                    ▒░░░░▒     ▒ ░▒░    ░░░▒▓▒░           
                                                  ░░▒▒░░░░  ░░░░░░░▒░░▒▒      ▒░▒▒    ░░▒░   ░░            
                                                ░░░░░▒▒▒▒▒▒▒░░▒░░░░▒▒░   ░░░░ ░▓░░░ ░░ ░▒   ▒░░           
                                            ░░░░░░░░     ░▒░░░░▒▒▒▒▒▒░░░▒░░▒ ░▒▒▒░░░▓▒░░░░░▒▒▒           
                                        ░░░░░░▒░        ░▒░ ░░░▒▒░           ░ ▒▓░░░░░▒                    
                                       ░░░▒▒          ▓  ░▒▒░              ░░░▒▒     ░▒                   
                                    ░ ░░▒▒▒  ░░▒▒░░░░▒░ ░▒   ▒▒░▒▒▒        ░ ░▓▒░▒▒▓▒ ░░                  
                                   ░ ░░▒▓░ ░▒░░▒▒  ▒▒░ ▒▒  ░▒░░░▒          ▒░░▒     ▓░░░                  
                                   ▒ ░░▒░ ▒░░░▒▓  ▓▒░░▒▓▒▒░░░ ░░▒▓▓▓▒      ▒░▒▒    ░▒░▒░                  
                                   ░░░▒▓ ▒▒░▒▒▒▒  ▒░░▒▒ ░░▒▒▒▒░░░░ ░       ░ ▒▒    ░░░▒                   
                                   ░░░▒▒▓▒░ ▒▒▒▒▒ ░░░▒▒                    ░ ░▓   ░░░▒                    
                                   ░░░▒▒▒░░░░░░░▒░░ ░▒░     ░  ░ ░  ▒       ░ ▓  ░░░▒      ░░░░           
                                   ░ ░░▒░░░░ ░▒░░░░░░▒   ░ ░ ▒ ░ ░  ░       ░ ▓▒░░▒▒    ░░ ░░░ ░░▒        
                                    ░ ░▒░░░░▒░░▒░░▒░▒▓░  ░▒░▒  ░ ░ ░        ░ ░▓░▓░    ░ ░▒▒▒░░▒░░▒░      
                                     ░▒░░▒░░░▒░▒▒░▒░░▒░▒░░▒▒░▒░▒▒░         ░░ ░▒▓░    ░ ░▒▒  ░▒▒▓▓▓▒      
                                        ▒░ ░░░▒░▒▒░░░▒▒░▒▒▒▒▒▒▒▒▒   ▒    ▒░░▒ ░▒░     ░ ░▒    ░▒▓ ░       
                                          ░▒░░▒░░▒▒▒░▒▓░▓▒▓▒▒▒▒░░▒░░░░░ ░░▒▓▒ ░▒▓    ░░░▓░    ░░▒░        
                                    ▒░     ░░░▒░░ ▒▒ ▒░▓▒▒▓▒░▓▒▒▒░░ ░ ░░▒▓░ ░░ ░▓    ▒░▒▒                 
                                 ░░▒░░     ░░░▒   ▒▒░▒▒░░░░░ ░░░░░░▒▒░░▓░    ░ ░▒   ░ ░▓                  
                                ░░░▒    ▒▒░  ░▒░░▒▒░▒▒▒░░░░░░░▒▒▒▒▒▒▒▒░      ▒ ░▒ ░▒ ░▓                   
                                ▒▓░     ░░▒▓░▒░ ░░░▒░▒░░░░░░░░░▒░▒▒▒▒░▒░      ░ ░▓░░ ▒▒                    
                               ▓▒▓  ▒  ▒░░▒▒▒▒▒░░░░▒░░▒▒░░▒▒░░░  ░░░░    ░░ ░░ ░▒▒▒▒                      
                             ░▒▒░░░░░ ░░░▒▓░░ ░░░░░░▒░ ░  ░░░░░░░░░░░░░░░▒░░   ▒▓                         
                              ▒▒░▒░░░░▒▒░░░▒░░░░░ ▒░▒▒░ ░░░░░░░░░░░░░░▒▒░░   ░░▒                          
                               ▒▒░ ░▒░ ░░▒░ ░ ░  ▒░▒░░   ░░░▒▒▒▒░░░░░░░░░   ░░▒░                          
                               ▓░░░▒▒ ░░▒░░░░░░░▒▒░░░░░░░░░░░  ░ ░░░░░░    ░░░▒░                           
                              ░░░░▒▒▒░░▒░░░░░░░░░░▒▒▒▓░░░▒▒▒░░░░░░░░░░   ░░░▒▒░                             
                             ▒░░░░░▒▒░░▒░░░░░░░░░░░▒▒     ░░░ ░▒▒▒▒▒▒▒▒▒                                  
                           ░▒░░░░░▒░▒░▒▓░░░░▒░▒▒▒░░░▒▒░ ▒▒░░▒                                             
                           ▒▒▒░▒░▒░░▒▓░▒░░░▒░░░░░░▒▒░▒░░░▒░                                               
                          ▒░▓▓▒░▒░▒▒░▒▒▒▒░▒▓▒▒▒░░▓▒                                                       
                         ▒░▒▒░▓▒▒░▒▒░░▒▒▒▒░▒██▓▒░▒                                                        
                         ░▒▓  ▒░░▒▒░▒▒▒░▒▒░▒█░░▓▒▓                                                        
                         ░   ░▒▒░░░░░░░░▒▒█▓ ▓█▒▒                                                        
                                ▓▒▒░░░░░░░░▓▓░░▒                                                          
                                   ▒▓▒▒░▒░░░ ▒░                                                           
                                    ▒▓▒▒░░░░░░░▒▒                                                         
                                     ▓▓▒▒░░░░▒░░░░▒▒                                                      
                                    ░▒░░░░░  ░▒░░▒░░▓▒░░                                                  
                                ░░░▓▒▒░░░░░▒▒░░▓░░░░░▓▒░░▒▒▓                                             
                              ▒▒▓▒░░░░░░░░░░░▒░░▒▒▒▒░▒▒░░░░░▓                                             
                            ░▓▒░░░░░░░▒▒░░░░▒▒░░░▒▒░░▒▒░▒▓▓▒▓                                             
                           ▒░░░▒▒▓▓▒▒▒▒▓░░░░░▒░ ░▒▒▒░▓▓▒▒░░▒▓▒                                            
                           ▒▒░░░▒▓▓▓▒▒▒▓░░ ░ ░  ░▒▒░▒▒   ▓▒░░░▒░░▓▒                                       
                           ▒▒░░░░▓▒░▒▓▓▒░▒▒ ░░░░░▒▒░▓░    ▒▒░░░▒░░ ▒                                      
                             ▒▒░░░░  ▓▒▒▓░ ░ ░░░▒▒▒░▒       ▒▒░░▒▒░░                                      
                            ▒▒░ ░▒░▒▒▒▒▓░░░░░░ ▒▒▒▓░          ▒▒░▒░░▒                                     
                         ░▒░░▒▓░░░▒▒▒▒░░░░░░ ░░░▒▒░           ▓▒▒▒▒░▓░                                    
                   ░░░░░░░░▒░  ░▒░░▒▒▒░░     ░▒▒▒▒            ░▒▓▓▒▓▒░                                    
              ░▒▒▒░░░░░░░░▒   ░▒░░░▒▒░░   ░░▒▒░▒▒              ▒░░▓▒▒░░                                   
             ░▒░▒░░░░░░░▒     ░░░ ░░░░░ ░ ▒░▒░░▒▒              ░  ░▒░▒▒░                                  
            ░▓░░░░░░░▒▒       ▓▓░ ░░░  ░░░▒▒▒▒▒░▒                   ▒░░░                                  
           ▒░░░▒▒▒▒▒░▒       ▒▒▒▒░░  ░ ░░▒▒▒▒░░▒                     ▓░▒                                  
         ░▒▒░░▒░░░▒         ░▓▒▒▓░  ░░  ▒░░░░░░░                      ▒░▒                                 
        ▒░▒░░▒ ░▒           ▓▒▒░▒   ░░░░░                              ▒░░                                
         ▒░▒               ▒▒▒░  ░ ░▒                                    ▒                                
       ▒░▒▒                ▓▒░░░░░░▒                                                                      
      ░▒                   ▒▒▒░   ░▒                                                                      
                           ░▓▒░░  ░▒       ░▒▒░░░▒░░▒                                                     
                            ▒▒░    ░   ░▓░ ░  ░░░░░░░░▒                                                   
                            ░▒░░░   ▒▒▒░░░░░▒   ▓▓▒░ ░░░                                                   
                              ▒░░ ░░░ ░▒▒▒▒     ▒░ ░░░▒                                                   
                               ▒░░░  ░  ░░    ░░  ░░░░                                                    
                                ░▒▒░░░░░  ░  ░ ░░░░░                                                      
                                ░░░▒▒▒▒▒░░░░░░░▒░                                                         
                                ▒░░░▒▒                       ░░░▒▒▒▒░░░                                   
                                ░▒ ░░▒                ░▒░░░  ░     ░  ░  ░░▒░                             
                                 ░░░░  ▒▒░░     ░░▒░ ░  ░ ░░▒▒▒░░    ░░▒▒░░░ ▒░                           
                                   ▒░░░░░░░░░ ░    ░░░░░░░                 ░░░░                           
                                      ░▒▒░░░░░░░▒▒▒░                        ░░░                           
                                                                            ░ ░                           
                                                                           ░ ░▒                           
                                                                          ░ ░▒                            
                                                                      ░░░ ░▒░                             
                                   ░░▒▒▒▒▒░░░░░░░░░▒▒▒▒▒░       ░▒▒░ ░ ░▒▒                                
                             ░░▒░░░                    ░░░░░░▒░▒▒▒▒░░░                                    
                         ░▒▒░                                                                             
                        ░ """,0.0000001)


