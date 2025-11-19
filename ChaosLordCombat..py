import time
import random
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
        "name": "Heal",
        "damage_range": (20, 50),
        "desc": "You heal slower than normal\n"},
}

Chaos_Lord_Powers = {
    '1': {
        "name": "Pandamonium Blast",
        "damage_range": (40, 100),
        "desc": "A blast of Pure Chaos\n"},
    '2': {
        "name": "Deadlight Burst",
        "damage_range": (70, 120),
        "desc": "A burst of Wraithborne Power\n"},
    '3': {
        "name": "Wailing Horde",
        "damage_range": (20, 110),
        "desc": "The spirits you've murdered, feel their pain\n"},
    '4': {
        "name": "Life Force Drain",
        "damage_range": (75, 100),
        "desc": "You loose your life force.....\n"},
}
def chaos_lord_combat():
    player_health = 300
    chaos_lord_health = 1000
    while player_health > 0 and chaos_lord_health > 0:
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
            chaos_lord_health -= damage
            if chaos_lord_health <= 0:
                typewriter(Style.BRIGHT + Fore.LIGHTGREEN_EX + "The Chaos Lord has been defeated! You win!", 0.05)
                break
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"Scylla HP: {chaos_lord_health} | Your HP: {player_health}")

        # --- Scylla's turn (random choice) ---
        boss_choice = random.choice(list(Chaos_Lord_Powers.values()))
        bname = boss_choice['name']
        blow, bhigh = boss_choice['damage_range']
        bdamage = random.randint(blow, bhigh)

        # apply effect according to target
        if boss_choice.get('target') == 'player':
            player_health -= bdamage
            print(f"Scylla uses {bname}! {boss_choice['desc']} You take {bdamage} damage.")

        # clamp healths and show status
        player_health = max(0, player_health)
        chaos_lord_health = max(0, chaos_lord_health)
        print(f"After Scylla's turn — Scylla HP: {chaos_lord_health} | Your HP: {player_health}")
        print("-" * 40)

        if player_health <= 0:
            print("You have been defeated...")
chaos_lord_combat()