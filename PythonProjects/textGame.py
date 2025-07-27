import random





def render_status_bar(location, health, items, width=80):
    # Text to display
    left_text = f" Location: {location} "
    right_text = f"Items: {len(items)}   Health: {health} "
    # Fill the space between with green color
    middle_space = width - len(left_text) - len(right_text)
    if middle_space < 0:  # Prevent errors if text is too long
        middle_space = 0
    bar = left_text + (" " * middle_space) + right_text
    # ANSI escape for green background + white text
    print("\033[1;37;42m" + bar.ljust(width) + "\033[0m")


directions =["north","south","east","west"]
events = [
        "",
        "",
        "",
        "",
        "",
        ""
        ]

descriptions = {
    "Great Hall": "You arrive in what used to be the Great Hall, but to you it’s just 'stop number one before dysentery gets us.' Dust and decay hang in the air. You can almost hear the ghosts of failed pioneers laughing at your optimism.",
    "Library": "A library? On the trail? Sure. The shelves are full of moldy books no one asked for. You consider reading, but remember you can’t even afford shoes, let alone literacy. Something scurries behind the stacks. Probably fine.",
    "Kitchen": "Once a place of grand feasts, now a buffet for maggots. There’s a loaf of bread on the counter. Do you eat it? It’s older than your wagon, but hey, calories are calories. Your stomach protests, but it’s not like you have standards.",
    "Dining Room": "The table is set like royalty might stroll in any minute. Instead, it’s just you — smelling like sweat, regret, and week-old jerky. At the far end, something is breathing in the shadows. Hopefully it’s friendly. It won’t be.",
    "Bedroom": "Ah, the bedroom. A bed that hasn’t seen use since the Civil War and sheets that crunch when touched. You debate sleeping here. The bedbugs are laughing at you.",
    "Gallery": "Portraits of people far fancier than you glare down from the walls. You can practically hear them whisper, 'Should’ve stayed home, pioneer.' One painting’s eyes follow you. You blink. Still staring. Creepy.",
    "Dungeon": "Finally, the dungeon. Chains hang from the walls, and the smell tells you someone didn’t make it out. The trail guide didn’t warn you about this part — but hey, at least it’s not cholera.",
    "Cellar": "The cellar is cold and damp. Barrels of… something line the walls. Could be wine. Could be human soup. You pop one open. It’s neither. Best not to ask questions."
        }

map={
        "Great Hall":{"north":"Dungeon","south":"Bedroom","west":"Library","east":"Kitchen"},
        "Library":{"east":"Great Hall"},       
        "Kitchen":{"north":"Dining Room","west":"Great Hall"},
        "Dining Room":{"south":"Kitchen"}, 
        "Bedroom":{"east":"Cellar","north":"Great Hall"},
        "Gallery":{"west":"Dungeon"},
        "Dungeon":{"east":"Gallery","south":"Great Hall"},
        "Cellar":{"west":"Bedroom"}
        }
availableitems={
        "Great Hall":"",
        "Library":"book",
        "kitchen":"spoon",
        "Dining Room":"table",
        "Bedroom":"pillow",
        "Gallery":"painting",
        "Dungeon":"",
        "Cellar":"gun"

        }
items=[]
health=100
playerLocation="Great Hall"
response=""
while response != "quit":
    exits=map[playerLocation]
    print("\n" * 100)
    #print(f'you find yourself at {playerLocation}')
    #print("GPS: ", str(exits).replace('{', '[').replace('}', ']'))
    render_status_bar(playerLocation,health,items)
    print(descriptions[playerLocation])
    response = input("Which path will you take?\nnorth,south,east,west: ").lower()
    if response in directions:
        if response in map[playerLocation]:
            playerLocation = map[playerLocation][response]
        else:
            
            print("\n" * 100)
            input("You cannot go that way!\n\nPress any key to try again!")
    
    elif (response.split())[0] == 'pickup':
        if (response.split())[1] == availableitems[playerLocation]:
            print("You have picked up a ", availableitems[playerLocation])
            items.append(availableitems[playerLocation])


    else:

        print("\n" * 100)
        input("wrong direction\n\nPress any key to continue...")
    # need a statement if entered wrong pickup item and need to remove picked item from main dictionary


    
    
    
