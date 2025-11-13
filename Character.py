from MAINCOLLYPROJECT import typewriter
from colorama import Fore, Style
import random
import time
class Character:
    def __init__(self, name, hp, damage, defence, powers) -> None:
       self.name = name
       self.hp = hp
       self.max_hp = hp
       self.damage = damage
       self.defence = defence
       self.powers = powers

    def is_alive(self):
        return self.hp > 0

# different abilities for the player | these are their weakened stats, their power is returned during the revelation midbattle
Player_Powers = {
    1: {
        "name": "Repulsive Blast",
        "damage_range": (40, 80),
        "desc": "A blast of magic"},
    2: {
        "name": "Slash",
        "damage_range": (50, 120),
        "desc": "Your power formed into a sharp blade"},
    3: {
        "name": "Shield Charge",
        "damage_range": (20, 100),
        "desc": "A blast of magic"},
    4: {
        "name": "Heal",
        "damage_range": (-20, -50),
        "desc": "You heal slower than normal"},
}
# OG powers
Player_OG_Powers = {
    1: {
        "name": "Concussive Blast",
        "damage_range": (60, 140),
        "desc": "A blast of magic"},
    2: {
        "name": "Slash",
        "damage_range": (100, 150),
        "desc": "Your power formed into a sharp blade"},
    3: {
        "name": "Absorb",
        "damage_range": (100, 120),
        "desc": "Their power becomes your own"},
    4: {
        "name": "Heal",
        "damage_range": (-70, -100),
        "desc": "You heal slower than normal"},
}
# ==={ SCYLLA POWERS }===
Scylla_Powers ={
    1: {
        "name": "Tidal Uproar",
        "damage_range": (60, 90),
        "desc": "A blast of magic"},
    2: {
        "name": "Tidal Uproar",
        "damage_range": (60, 90),
        "desc": "A blast of magic"},
    3: {
        "name": "Tidal Uproar",
        "damage_range": (60, 90),
        "desc": "A blast of magic"},
    4: {
        "name": "Tidal Uproar",
        "damage_range": (60, 90),
        "desc": "A blast of magic"},
}
def take_damage(self, amount):
        reduced = max(1,amount - self.defence)
        self.hp -= reduced
        typewriter(f"{self.name} takes {reduced} damage! (HP: {self.hp}/{self.max_hp})", 0.05)

    def heal(self, amount):
        self.hp =min(self.max_hp, self.hp + amount)
        typewriter((Style.BRIGHT + Fore.LIGHTGREEN_EX + f"{self.name} regenerates {amount} HP! (HP: {self.hp}/{self.max_hp})",0.05))




def use_power(attacker, target, choice):
    if isinstance(choice, str) and choice.isdigit():
        choice = int(choice)

    if choice not in Player_Powers:
        typewriter(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"{Player} How does one fumble like this, you really are a basic witch.", 0.05)
        return False

    ability = Player_Powers[choice]
    name = ability["name"]
    desc = ability["desc"]
    dmg_min, dmg_max = ability["damage"]

    typewriter(f"\n{attacker.name} uses {name}! {desc}")
    damage = random.randint(dmg_min, dmg_max)

    if damage < 0:
        heal_amount = abs(damage)
        attacker.hp = min(attacker.max_hp + heal_amount)
        typewriter(f"{attacker.name} heals for {heal_amount} HP! {attacker.hp}/{attacker.max_hp}", 0.05)
        return True

    final_damage = max (1, damage + attacker.damage - target.defence)
    target.hp = max(0, target.hp - final_damage)
    typewriter(f"{target.name} uses {name}! {desc}")

    return True

def player_turn(player, boss):
    typewriter(f"{player.name} takes {player.damage} damage!", 0.05)