


def dresser():

    from navigation_scene import navigate_to_other_scenes_scene

    # Scene 6: The Dresser

    # Description:

    print("\n\nThe dresser is fairly thin but makes up for its width with length spanning half of the wall. The dark wood frame contains")
    print("a plethora of white-stained drawers for you to look through, though there is also glass sitting on top of the dresser that")
    print("seems to have been once filled with milk.")

    # Choices:

    print("\nA: Examine the glass")
    print("B: Examine the drawers")
    print("C: Go back")

    while True:
        choice6 = input("\nWhat do you look at? ").upper()

        if choice6 == "A":
            return dresserA()
        elif choice6 == "B":
            return dresserB()
        elif choice6 == "C":
            return navigate_to_other_scenes_scene()
        else:
            print("\nNot an option. Please enter A, B, or C.")

    # Outcomes: scene traveling oooOOOOooooOOOOOOoooooooo

    # A: scene 6.1
    # B: scene 6.2
    # C: scene 4

    # Consequences: none

def dresserA():

    global scene_count

    from state import scene_count
    from state import raise_suspicion
    from state import player

    # Scene 6.1: The Glass

    # Description:

    scene_count =+ 1

    print("\n\nYou take your gloves out of your pocket and put them on before picking up the glass. There is still a small bit of milk")
    print("remaining at the bottom. Upon sniffing it, you smell the distinct smell of almonds, but it is not like almond milk. It is")
    print("a bitter scent, one much like what you smelled on the body. One like cyanide.")

    # Choices:

    print("\nA: Take the glass")
    print("B: Leave the glass")

    while True:
        choice61 = input("\nWhat do you do? ").upper()

        if choice61 == "A":
            #print("write description for the sake of turning the assignment in I will write later")
            raise_suspicion(2)
            player["inventory"].append("glass")
            input("\nPress Enter to go back")
            return dresser()
        elif choice61 == "B":
            #print("write description for the sake of turning the assignment in I will write later")
            input("\nPress Enter to go back")
            return dresser()
        else:
            print("\nNot an option. Please enter A or B.")

    # Outcomes:

    # A: you take the glass, put in pocket perhaps, prompt to go back
    # B: you leave the glass, parnter asks about it, prompt to go back

    # Consequences:

    # A: plus 2 suspiscion, glass in inventory
    # B: nothing

def dresserB():

    global scene_count

    from index import scene_count    
    from index import player

    # Scene 6.2: The Drawers

    # Description:

    scene_count =+ 1

    print("\n\nYou start opening the drawers, look though them, and promptly close them once you see they are completely empty. Any personal")
    print("belongings in the room are in the suitcases, but something catches your eye as you look through the last drawer; there is a")
    print("small, torn piece of paper tucked into the back corner of the drawer.")

    # Choices:

    print("\nA: Take the paper")
    print("B: Leave the paper")

    while True:
        choice62 = input("\nWhat do you do? ").upper()

        if choice62 == "A":
            #print("write description for the sake of turning the assignment in I will write later")
            player["inventory"].append("paper")
            input("\nPress Enter to go back")
            return dresser()
        elif choice62 == "B":
            #print("write description for the sake of turning the assignment in I will write later")
            input("\nPress Enter to go back")
            return dresser()
        else:
            print("\nNot an option. Please enter A or B.")

    # Outcomes:

    # A: you take the paper, see "DEAD" written on it, put in pocket, prompt to go back
    # B: you leave the paper, prompt to go back

    # Consequences:

    # A: paper in inventory
    # B: nothing