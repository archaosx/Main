import random
import time
import sys


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
        "damage_range": (20, 100),
        "desc": "A blast of magic\n"},
    '4': {
        "name": "Heal",
        "damage_range": (-20, -50),
        "desc": "You heal slower than normal\n"},
}

health = 250
Scylla_Health = 600
while health > 0 and Scylla_Health > 0:
    typewriter("1 | Repulsive Blast!",0.05)
    typewriter("2 | Slash!", 0.05)
    typewriter("3 | Shield Charge!", 0.05)
    typewriter("4 | Slash!", 0.05)
    choice = int(input('Pick your chaos'))
    while choice < 1 or choice > 4:
        print('You have to listen to the rules this time, Little Witch...')
        choice = int(input())
    choice = str(choice)
    low, high = Player_Powers[choice]['damage_range']
    damage = random.randint(low, high)
    print(damage, 0.05)
    if choice != '4':
        Scylla_Health -= damage
    else:
        Scylla_Health += damage
    print(Scylla_Health)