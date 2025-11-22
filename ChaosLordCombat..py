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
        "name": "Primordial Beam",
        "damage_range": (70, 100),
        "desc": "Rays of pure destruction"},
}

Chaos_Lord_Powers = {
    '1': {
        "name": "Pandamonium Blast",
        "damage_range": (40, 100),
        "desc": "A blast of Pure Chaos\n"},
    '2': {
        "name": "Deadlight Burst",
        "damage_range": (70, 120),
        "desc": "I can kill every living thing on this world....\n"},
    '3': {
        "name": "Wailing Horde",
        "damage_range": (20, 110),
        "desc": "I have all the Chaos in my corner...\n"},
    '4': {
        "name": "Life Force Drain",
        "damage_range": (75, 100),
        "desc": "You can't kill me..You cant kill me\n"},
}
def chaos_lord_combat():
    player_health = 300
    chaos_lord_health = 1000
    while player_health > 0 and chaos_lord_health > 0:
        # show moves
        typewriter(Style.BRIGHT + Fore.LIGHTRED_EX + "Your move, Little Witch...:", 0.05)
        for key, move in Player_OG_Powers.items():
            typewriter(
                Style.BRIGHT + Fore.LIGHTWHITE_EX + f"{key}) {move['name']} (damage {move['damage_range'][0]}-{move['damage_range'][1]})",
                0.02)
        # get valid choice
        choice = input(Style.BRIGHT + Fore.LIGHTRED_EX + "Pick your chaos (1-4): ").strip()
        if choice not in Player_OG_Powers:
            typewriter(Style.BRIGHT + Fore.LIGHTRED_EX + "Invalid choice — you fumble and lose your turn!", 0.05)
        else:
            # player's attack resolution
            low, high = Player_OG_Powers[choice]['damage_range']
            damage = random.randint(low, high)
            typewriter(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"You use {Player_OG_Powers[choice]['name']} and deal {damage} damage!",
                0.05)
            chaos_lord_health -= damage
            if chaos_lord_health <= 0:
                typewriter(Style.BRIGHT + Fore.LIGHTGREEN_EX + "The Chaos Lord has been defeated! You win!", 0.05)
                typewriter(Style.BRIGHT + Fore.LIGHTGREEN_EX + "You step forwards into the woodlands....!", 0.05)
                break
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"Chaotic HP: {chaos_lord_health} | Your HP: {player_health}")

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
        print(f"After Their turn — Chaotic HP: {chaos_lord_health} | Your HP: {player_health}")
        print("-" * 40)

        if player_health <= 0:
            print("You have been defeated...")
            typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"The hooded figure reveals their form, its you..., your face", 0.05)
            typewriter(Style.BRIGHT + Fore.LIGHTRED_EX +"-{ He throws the cloak down }- \n when you resurrect again, you have to do the same thing i did", 0.05)
            typewriter(Style.BRIGHT + Fore.LIGHTBLACK_EX +"Condemn these souls to torture, once i leave the time line will restart, chain Hecate and curse scylla to death", 0.05)
            typewriter(Style.BRIGHT + Fore.LIGHTBLACK_EX +"If you ever want to see our friends again you must...",0.05)

if __name__ == "__main__":
    chaos_lord_combat()
