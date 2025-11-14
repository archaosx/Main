from MAINCOLLYPROJECT import typewriter
from colorama import Fore, Style
import random
import time

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
        "desc": "The water is your enemy!"},
    2: {
        "name": "Bite",
        "damage_range": (60, 100),
        "desc": "RUN BEFORE SHE RIPS YOU APART!"},
    3: {
        "name": "Tail Slam",
        "damage_range": (40, 90),
        "desc": "Slammed by your tail"},
    4: {
        "name": "Havoc",
        "damage_range": (50, 100),
        "desc": "Destruction"},
}
# ==={ DARK NEREIDS }===
Dark_Nereids ={
    1: {
        "name": "Siren Song",
        "damage_range": (60, 90),
        "desc": "DONT LISTE-, actually it's beautiful..."},
    2: {
        "name": "Aquatic Rage",
        "damage_range": (60, 100),
        "desc": "The ocean hates you!"},
    3: {
        "name": "Clawed Frenzy",
        "damage_range": (40, 90),
        "desc": "The pod advances on your soul"},
    4: {
        "name": "Damned Memories",
        "damage_range": (50, 100),
        "desc": "The screams of their victims drown you"},
}
# ==={ CHAOS LORD }===
Chaos_Lord ={
    1: {
        "name": "Devastating Blast",
        "damage_range": (60, 100),
        "desc": "."},
    2: {
        "name": "Wailing Horde",
        "damage_range": (60, 100),
        "desc": "A stampede of demons"},
    3: {
        "name": "Clawed Frenzy",
        "damage_range": (40, 90),
        "desc": "The pod advances on your soul"},
    4: {
        "name": "Damned Memories",
        "damage_range": (50, 100),
        "desc": "The screams of their victims drown you"},
}