


def closet():

    from navigation_scene import navigate_to_other_scenes_scene

    # Scene 7: The Closet

    # Description:

    print("\n\nUpon opening the door to the closet, you see that it is completely empty. There is not even an irioning board")
    print("like many other hotels often have. All there is are hangers not being used...and a dark shape in the corner. You realize it")
    print("is a safe the hotel provides hidden in the dark corner of the closet.")

    # Choices:

    print("\nA: Examine the safe")
    print("B: Go back")

    while True:
        choice7 = input("\nWhat do you do? ").upper()

        if choice7 == "A":
            return safe()
        elif choice7 == "B":
            return navigate_to_other_scenes_scene()
        else:
            print("\nNot an option. Please enter A or B.")

    # Outcomes:

    # A: 7.1
    # B: 4

    # Consequences: nothing

def safe():

    from index import player

    # Scene 7.1: The Safe

    # Description:

    print("\n\nYou crouch down to the floor of the closet and bring the safe out of the corner, turning it so the keypad to enter the code")
    print("is facing you. It appears to be a simple four digit code. Gently shaking the safe produces a sound of something moving within")
    print("the containment. Something someone cared enough about to have wanted to keep it hidden.")

    # Choices:

    print("\nA: Enter code")
    print("B: Go back")

    while True:
        choice71 = input("\nWhat do you do? ").upper()

        # how do I write an if statement for something only showing up if item is in inventory even if another item is 
        # in the inventory how do inventories???

        if choice71 == "A" and "paper" in player["inventory"]:
            #print("write description for the sake of turning the assignment in I will write later")
            code = input("\nEnter code: ")
            if code == "4514":
                return diary()
            else:
                print("\n\nIncorrect. Try again.")
                return safe ()
        elif choice71 == "A" and "paper" not in player["inventory"]:
            print("\nYou input a few codes but none of them are correct. Return once you find something that will help you input the right code.")
            input("\nPress Enter to go back")
            return closet()
        elif choice71 == "B":
            return closet()
        else:
            print("\nNot an option. Please enter A or B.")

    # Outcomes:

    # A: if paper in inventory, describe paper again and prompt to enter code; else prompt to go back
    # B: scene 7

    # Consequences:

    # A: if code right, scene 7.2; else say incorrect and prompt enter code again
    # B: nothing

def diary():

    global scene_count

    from index import scene_count
    from index import raise_suspicion
    from index import player

    # Scene 7.2: Diary

    # Description:

    scene_count =+ 1

    print("\n\nEntering the correct code and opening the safe reveals...a small diary. There does not seem to be anything else in the")
    print("safe; it is just the diary. Upon closer inspection, you see-printed in bold letters on the front of the diary-the")
    print("deceased's name.")

    # Choices:

    print("\nA: Take the diary")
    print("B: Leave the diary")

    while True:
        choice72 = input("\nWhat do you do? ").upper()

        if choice72 == "A":
            #print("write description for the sake of turning the assignment in I will write later")
            raise_suspicion(2)
            player["inventory"].append("diary")
            input("\nPress Enter to go back")
            return closet()
        elif choice72 == "B":
            #print("write description for the sake of turning the assignment in I will write later")
            input("\nPress Enter to go back")
            return closet()
        else:
            print("\nNot an option. Please enter A or B.")

    # Outcomes:

    # A: you take the diary, put in pocket, prompt to go back
    # B: you leave the diary, someone from forensics comes over to see if it's evidence, prompt to go back

    # Consequences:

    # A: plus 2 suspicion
    # B: nothing