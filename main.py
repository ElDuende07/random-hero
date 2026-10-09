import os
import random
import sys
import time
from io import BytesIO

import requests
from PIL import Image


# Get the full path to the text file used to store already-picked heroes.
script_dir = os.path.dirname(os.path.abspath(__file__))
used_heroes_file = os.path.join(script_dir, "used_heroes.txt")

# Full list of Dota 2 heroes.
heroes = [
    "Abaddon", "Alchemist", "Ancient Apparition", "Anti-Mage", "Arc Warden", "Axe", "Bane",
    "Batrider", "Beastmaster", "Bloodseeker", "Bounty Hunter", "Brewmaster", "Bristleback",
    "Broodmother", "Centaur Warrunner", "Chaos Knight", "Chen", "Clinkz", "Clockwerk",
    "Crystal Maiden", "Dark Seer", "Dark Willow", "Dawnbreaker", "Dazzle", "Death Prophet",
    "Disruptor", "Doom", "Dragon Knight", "Drow Ranger", "Earth Spirit", "Earthshaker",
    "Elder Titan", "Ember Spirit", "Enchantress", "Enigma", "Faceless Void", "Grimstroke",
    "Gyrocopter", "Hoodwink", "Huskar", "Invoker", "Io", "Jakiro", "Juggernaut",
    "Keeper of the Light", "Kez", "Kunkka", "Legion Commander", "Leshrac", "Lich",
    "Lifestealer", "Lina", "Lion", "Lone Druid", "Luna", "Lycan", "Magnus", "Marci", "Mars",
    "Medusa", "Meepo", "Mirana", "Monkey King", "Morphling", "Muerta", "Naga Siren",
    "Nature's Prophet", "Necrophos", "Night Stalker", "Nyx Assassin", "Ogre Magi",
    "Omniknight", "Oracle", "Outworld Destroyer", "Pangolier", "Phantom Assassin",
    "Phantom Lancer", "Phoenix", "Primal Beast", "Puck", "Pudge", "Pugna", "Queen of Pain",
    "Razor", "Riki", "Ringmaster", "Rubick", "Sand King", "Shadow Demon", "Shadow Fiend",
    "Shadow Shaman", "Silencer", "Skywrath Mage", "Slardar", "Slark", "Snapfire", "Sniper",
    "Spectre", "Spirit Breaker", "Storm Spirit", "Sven", "Techies", "Templar Assassin",
    "Terrorblade", "Tidehunter", "Timbersaw", "Tinker", "Tiny", "Treant Protector",
    "Troll Warlord", "Tusk", "Underlord", "Undying", "Ursa", "Vengeful Spirit", "Venomancer",
    "Viper", "Visage", "Void Spirit", "Warlock", "Weaver", "Windranger", "Winter Wyvern",
    "Witch Doctor", "Wraith King", "Zeus",
]


def animate_text(text, delay=0.05):
    """Display text one character at a time."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def show_hero_image(hero_name):
    """Fetch and display a hero image from Dota 2's public CDN."""
    formatted_name = hero_name.lower().replace(" ", "_").replace("'", "")
    url = f"https://cdn.dota2.com/apps/dota2/images/heroes/{formatted_name}_full.png"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        image.show()
    except Exception as error:
        print(f"Could not load image for {hero_name}: {error}")


while True:
    if os.path.exists(used_heroes_file):
        with open(used_heroes_file, "r", encoding="utf-8") as file:
            used_heroes = [line.strip() for line in file if line.strip()]
    else:
        used_heroes = []

    if len(used_heroes) >= len(heroes):
        animate_text("\nAll heroes have been used! Resetting the list...\n")
        open(used_heroes_file, "w", encoding="utf-8").close()
        used_heroes = []

    available_heroes = [hero for hero in heroes if hero not in used_heroes]
    random_hero = random.choice(available_heroes)

    animate_text("Picking your hero", 0.05)
    for dot in "...":
        sys.stdout.write(dot)
        sys.stdout.flush()
        time.sleep(0.4)
    print()
    animate_text(f"\nYour hero choice is: {random_hero}\n", 0.06)

    show_hero_image(random_hero)

    with open(used_heroes_file, "a", encoding="utf-8") as file:
        file.write(random_hero + "\n")
    print("Enjoy your game")

    again = input("Pick another hero? (y/n or type 'reset' to restart): ").strip().lower()
    if again == "reset":
        open(used_heroes_file, "w", encoding="utf-8").close()
        print("Hero list reset!\n")
        continue
    if again not in ["y", "yes"]:
        break
