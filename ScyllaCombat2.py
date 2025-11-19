import random
from colorama import Fore, Style, init
import sys
import time
init(autoreset=False)
import copy

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
        "name": "Heal",
        "damage_range": (20, 50),
        "desc": "You heal slower than normal\n"},

    }
Player_OG_Powers = {
    '1': {
        "name": "Concussive Blast",
        "damage_range": (60, 140),
        "desc": "A blast of magic"},
    '2': {
        "name": "Slash",
        "damage_range": (100, 150),
        "desc": "Your power formed into a sharp blade"},
    '3': {
        "name": "Absorb",
        "damage_range": (100, 120),
        "desc": "Their power becomes your own"},
    '4': {
        "name": "Heal",
        "damage_range": (70, 100),
        "desc": "You heal slower than normal"},

}
Scylla_Powers ={
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

Player_Original_Powers_ = copy.deepcopy(Player_Powers) # this will replace the weaker powers with the OG powers

Player_Health = 600
Scylla_Health = 700
while Player_Health > 0 and Scylla_Health > 0:
    # show moves
    typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"Unleash your chaos, Little Witch...:", 0.05)
    for key, move in Player_OG_Powers.items():
        typewriter(Style.BRIGHT + Fore.LIGHTWHITE_EX + f"{key}) {move['name']} (damage {move['damage_range'][0]}-{move['damage_range'][1]})",0.02)
    # get valid choice
    choice = input(Style.BRIGHT + Fore.LIGHTRED_EX +"Pick your chaos (1-4): ").strip()
    if choice not in Player_OG_Powers:
        typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"Invalid choice — you gotta follow these rules, miss your turn!",0.05)
    else:
        # player's attack resolution
        low, high = Player_OG_Powers[choice]['damage_range']
        damage = random.randint(low, high)
        typewriter(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"You use {Player_OG_Powers[choice]['name']} and deal {damage} damage!", 0.05)
        Scylla_Health -= damage
        if Scylla_Health <= 0:
            scylla_health = 0
            typewriter(Style.BRIGHT + Fore.LIGHTGREEN_EX + "Scylla has been defeated! You win!", 0.05)
            break
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX +f"Scylla HP: {Scylla_Health} | Your HP: {Player_Health}")

    # --- Scylla's turn (random choice) ---
    boss_choice = random.choice(list(Scylla_Powers.values()))
    bname = boss_choice['name']
    blow, bhigh = boss_choice['damage_range']
    bdamage = random.randint(blow, bhigh)

    # apply effect according to target
    if boss_choice.get('target') == 'player':
     Player_Health -= bdamage
     print(f"Scylla uses {bname}! {boss_choice['desc']} You take {bdamage} damage.")

    # clamp healths and show status
    player_health = max(0, Player_Health)
    scylla_health = max(0, Scylla_Health)
    print(f"After Scylla's turn — Scylla HP: {Scylla_Health} | Your HP: {Player_Health}")
    print("-" * 40)

    if player_health <= 0:
        print("You have been defeated...")