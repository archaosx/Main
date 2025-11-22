import random
import time
import sys
from colorama import Fore, Style, init
init(autoreset=False)

def typewriter(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

Player_Powers = {
    '1': {
        "name": "Repulsive Blast",
        "damage_range": (40, 80),
        "desc": "A blast of magic\n"},
    '2': {
        "name": "Slash",
        "damage_range": (50, 100),
        "desc": "Your power formed into a sharp blade\n"},
    '3': {
        "name": "Shield Charge",
        "damage_range": (20, 60),
        "desc": "A blast of magic\n"},
    '4': {
        "name": "Lightning",
        "damage_range": (20, 50),
        "desc": "Shocking innit\n"},

    }
# Player_Original_Powers_ = copy.deepcopy(Player_Powers) # this will replace the weaker powers with the OG powers
Scylla_Powers = {
    1: {
        "name": "Tidal Uproar",
        "damage_range": (40, 90),
        "desc": "The waters hate you",
        "target": "player"},
    2: {
        "name": "Bite",
        "damage_range": (60, 100),
        "desc": "A BLOODY way to die",
        "target": "player"},
    3: {
        "name": "Tail Whip",
        "damage_range": (70, 90),
        "desc": "Her tail lashes at you,",
        "target": "player"},
    4: {
        "name": "Call of the dogs",
        "damage_range": (60, 120),
        "desc": "Her heads frenzy you",
        "target": "player"},
    }
def scylla_combat1():
    player_health = 300
    scylla_health = 700
    while player_health > 0 and scylla_health > 0:
        # show moves
        typewriter(Style.BRIGHT + Fore.LIGHTRED_EX + "Your move, Little Witch...:", 0.05)
        for key, move in Player_Powers.items():
            typewriter(
                Style.BRIGHT + Fore.LIGHTWHITE_EX + f"{key}) {move['name']} (damage {move['damage_range'][0]}-{move['damage_range'][1]})",
                0.02)
        # get valid choice
        choice = input(Style.BRIGHT + Fore.LIGHTRED_EX + "Pick your chaos (1-4): ").strip()
        if choice not in Player_Powers:
            typewriter(Style.BRIGHT + Fore.LIGHTRED_EX + "Invalid choice — you fumble and lose your turn!", 0.05)
        else:
            # player's attack resolution
            low, high = Player_Powers[choice]['damage_range']
            damage = random.randint(low, high)
            typewriter(
                Style.BRIGHT + Fore.LIGHTGREEN_EX + f"You use {Player_Powers[choice]['name']} and deal {damage} damage!",
                0.05)
            scylla_health -= damage
            if scylla_health <= 0:
                typewriter(Style.BRIGHT + Fore.LIGHTGREEN_EX + "Scylla has been defeated! You win!", 0.05)
                break
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"Scylla HP: {scylla_health} | Your HP: {player_health}")

        # --- Scylla's turn (random choice) ---
        boss_choice = random.choice(list(Scylla_Powers.values()))
        bname = boss_choice['name']
        blow, bhigh = boss_choice['damage_range']
        bdamage = random.randint(blow, bhigh)

        # apply effect according to target
        if boss_choice.get('target') == 'player':
            player_health -= bdamage
            print(f"Scylla uses {bname}! {boss_choice['desc']} You take {bdamage} damage.")

        # clamp healths and show status
        player_health = max(0, player_health)
        scylla_health = max(0, scylla_health)
        print(f"After Scylla's turn — Scylla HP: {scylla_health} | Your HP: {player_health}")
        print("-" * 40)

        if player_health <= 0:
            print("You have been defeated...")

if __name__ == "__main__":
 scylla_combat1()
