# Refactored Text RPG Game Code

from game_map import getmapRitualHall, getmapWhisperingRoom, getmapTortureChamber6
from story import callNarrator
import os
import platform
import time
import random

# Global Game State
inventory = []
currentRoom = "Whispering Room"
life = 85

rooms = {
    "Whispering Room": {"north": "Ritual Hall", "item": "candy"},
    "Ritual Hall": {"south": "Whispering Room", "east": "Torture Chamber 6", "item": "map"},
    "Torture Chamber 6": {"west": "Ritual Hall", "item": "scalpel"}
}

# Clear Screen

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")


# Show Instructions

def showInstructions():
    clear_screen()
    print('''
    ===============
     Text RPG GAME
    ===============
Instructions:    
 In order to move you must use two words: go (north, south, east, west)
 In order to pick up an item you must use: get (name of the item)
    ''')
    input("Press Enter to start the game...")
    print("Loading room...")
    time.sleep(2)
    print("...there's someone already here.")
    time.sleep(4)


# Display Status Panel

def statusPanel():
    print("\n╔════════════════════════════════════════════════════════════════════╗")
    print("║                       ENTITY STATUS PANEL                          ║")
    print("╠════════════════════════════════════════════════════════════════════╣")
    print(f"║ [*] LOCATION : {currentRoom.ljust(55)}║")
    print(f"║ [#] LIFE     : {str(life) + '%'.ljust(55)}║")
    print(f"║ [$] INVENTORY: {', '.join(inventory).ljust(55)}║")
    print("╠════════════════════════════════════════════════════════════════════╣")
    print("║ [COMMANDS]                                                         ║")
    print("║ - To move:         go [north | south | east | west]               ║")
    print("║ - To get item:     get [item name]                                ║")
    print("║ - To use item:     type the item's name                           ║")
    print("╚════════════════════════════════════════════════════════════════════╝")

# Show Map Based on Room

def showMapForRoom(room):
    maps = {
        "Ritual Hall": getmapRitualHall,
        "Whispering Room": getmapWhisperingRoom,
        "Torture Chamber 6": getmapTortureChamber6
    }
    map_func = maps.get(room)
    if map_func:
        map_func()
    else:
        print("No map available for this room.")
    input("Press Enter to resume the game...")
    clear_screen()


# Trigger Scalpel Power in Specific Room

def scalpel_Power(room):
    messages = {
        "Ritual Hall": "The scalpel hums against your skin, not with sound—but with dread.",
        "Whispering Room": "You feel it twitch in your palm, like it remembers pain nearby.\nTheir footsteps never left. You’ll hear them, too.",
        "Torture Chamber 6": "The scalpel pulses cold in your hand..."
    }
    print(messages.get(room, ""))


# Show Game Intro

def showIntro():
    print(r"""
                    ░░░░░░░░░░░░░░░░
              ░░░░░░░░░░░░░░░░░░░░░░░░
           ░░░░░░     ▒▒▒▒▒▒     ░░░░░░
        ░░░░   ▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒   ░░░░
      ░░░     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ░░░
     ░░     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ░░
    ░░    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ░░
    ░░    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ░░
     ░░     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ░░
      ░░░     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ░░░
        ░░░░     ▒▒▒▒▒▒▒▒▒▒▒▒     ░░░░
           ░░░░░░     ▒▒     ░░░░░░
              ░░░░░░░░░░░░░░░░░░
                     ░░░░░░░

    You awaken on a cold floor. Your head pounds.
    Faint light pours through cracks in the ceiling,
    dust dancing in the air like falling ash.

    The silence is thick... but not empty.

    A dull metallic scent lingers. You are not alone.
""")
    print("Location:", currentRoom)


# Handle Game Over

def triggerGameOver():
    clear_screen()
    print("it has found you...")
    input("Press Enter")
    clear_screen()
    print("you are losing blood rapidly while laying on the ground")
    input("Press Enter")
    clear_screen()
    print("\n[ IT SEES YOU LAST. ]\n[ GAME OVER ]")
    input("Press Enter")


# Run the Game
showInstructions()
clear_screen()
showIntro()

while True:
    delay = random.randint(1, 2)
    statusPanel()
    move = input("What is gonna be your next move?\n> ").lower().strip().split(" ", 1)
    print("....")
    time.sleep(delay)
    clear_screen()

    if move[0] == "get" and len(move) > 1:
        item = rooms[currentRoom].get("item")
        if item == move[1]:
            print(f'You got a {item}!')
            inventory.append(item)
            rooms[currentRoom]["item"] = ""
        else:
            print(f'No {move[1]} here, sorry!')

    elif move[0] == "go" and len(move) > 1:
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            callNarrator(currentRoom)
            if "monster" in rooms[currentRoom]:
                triggerGameOver()
                break
        else:
            print('Not a valid move, sorry!')

    elif move[0] == "map":
        if "map" in inventory:
            showMapForRoom(currentRoom)
        else:
            print("A map? ... don't think I've seen one of those...")

    elif move[0] == "exit":
        break
