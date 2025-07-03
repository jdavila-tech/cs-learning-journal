
import sys
import time
from operator import truediv

has_visited_ritual_hall = False
has_visited_torture_chamber6 = False
def callNarrator(currentRoom):

   #Booleans to track if a room has been visited to skip the story
    global has_visited_ritual_hall #lets the function change the global variable
    global has_visited_torture_chamber6

    global user

    if not has_visited_ritual_hall:

        if currentRoom=="Ritual Hall" :
            def slow_type(text, delay=.09):
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(delay)
                print()

            slow_type("""
            After pushing forward into the cold, piercing dark, 
            I stumble—barely keeping balance—into a vast, still chamber. 
    
            My breath catches in my throat. 
            Everything here feels... wrong.
    
            The silence is too complete. The air, too stale. 
            Something presses on my mind, like a scream I can’t hear.
    
            Is this madness?
    
            No—there, on the ground. A folded paper, damp and smudged, 
            its surface covered in frantic symbols and crude drawings.
    
            A guide...? 
            Or a warning?
    
            Either way... it’s too late to turn back now.
            """, 0.009)
            input("press any key to continue")
            user= str(input("..by the way, what is your name? > "))
            has_visited_ritual_hall = True


            print()
            print("[You found a map. Type 'get map' to grab it]")
            print('''
             ░░░░░░░░░░░░░░░░░
           ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
         ░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒░
       ░▒▒▓▓███████▓▓▓▓▓▓▓▓▓▓▒▒▒▒░
      ▒▒▓▓███▓▓▓░░░░░░░░░░▓▓██▓▓▒▒
     ▒▒▓▓██▓░░░░      ░░░░░░▓▓▓▓▓▒
     ▓▓▓▓▓░░   ▒▒▒▒▒▒▒░░░░░░░░▓▓▓▓
    ▓▓▓▓░   ▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░░▓▓▓
    ▓▓░    ▒▓▓███████▓▓▓▒░░░░░░░▓▓
    ▓░    ▓▓████░░░░████▓░░░░░░░▓▓
    ▓░    ▓▓██░  ▲▲   ░██▓░░░░░░░▓
    ▓░    ▓▓█   ▓▓▓▓   ░█▓░░░░░░░▓
    ▓▓░   ▓▓░   ▓░░▓    ▓▓░░░░░░▓▓
    ▓▓▓░  ▓▓░   ░░░░    ▓▓▓░░░░▓▓▓
     ▓▓▓▓░▓▓▓          ▓▓▓▓▓▓▓▓▓▓
      ▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓
       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
             ▓▓▓▓▓▓▓▓▓▓▓
            ''')
        print("[To use it just type 'map']")

    if not has_visited_torture_chamber6:
        if currentRoom=="Torture Chamber 6":
            print("here goes the story for ",currentRoom)
            def slow_type(text, delay=0.005):
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(delay)
                print()

            slow_type("""
                       The door creaks open, heavy and rusted, revealing a narrow stone hall.

                       I step inside... and instantly regret it.

                       The walls are streaked—dark, dried, impossible to identify. 
                       The smell is overwhelming: copper, rot, something chemical beneath it all.

                       Chains dangle from the ceiling like waiting fingers. 
                       Hooks line the walls. A rusted drain gapes in the center of the floor.

                       What happened here?

                       No... I don’t want to know.

                       But as I turn to leave, I see it—scratched into the stone:
                       a single word repeated again and again in shaky lines—

                       
                   """, 0.008)
            print("it reads... ... . .. .\n ..",user)
            input("\npress any key to continue")
            print("You find an old, blood-stained scalpel near your name on the wall.\nIt's cold to the touch, but... it feels like it's meant for you.Almost \nlike someone left it behind for you.")
            has_visited_torture_chamber6=True

