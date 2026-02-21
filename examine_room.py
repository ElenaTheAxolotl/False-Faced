


def room():

    global scene_count

    from index import scene_count
    from introduction_scene import intro
    from index import raise_suspicion

    # Scene 3: The Room

    # Description:

    scene_count =+ 1

    print("\n\nLooking around the room, there is not much to see. A few forensics workers are looking for evidence, but the room is")
    print("practically bare, the only furniture being the two beds, a television, and a dresser below the television. There are two")
    print("suitcases on the floor next to the closet, one opened with clothes falling out of it while the other is completely shut,")
    print("as though it was ready to be picked up and leave at a moment's notice.")
    print("Your attention on the suitcases appearently drew the attention of someones else: your...partner. He walks up to you,")
    print("asking,")

    print("\n\"Think the suitcases could lead to something, lead detective?\"\n")

    # Choices:

    print("\nA: \"One of them knew they were in danger.\"")
    print("B: \"Not until we know whose is whose.\"")
    print("C: Ignore him")

    while True:

        choice3 = input("\nYour answer (Enter A, B, or C): ").upper()

        if choice3 == "A":
            #print("continue dialouge for the sake of turning the assignment in I will write later")
            raise_suspicion(1)
            input("\nPress Enter to go back")
            return intro()
        elif choice3 == "B":
            #print("continue dialouge for the sake of turning the assignment in I will write later")
            input("\nPress Enter to go back")
            return intro()
        elif choice3 == "C":
            #print("continue dialouge for the sake of turning the assignment in I will write later")
            input("\nPress Enter to go back")
            return intro()
        else:
            print("\nNot an option. Please enter A, B, or C.")

    # Outcomes:

    # A: continue dialogue, option to move back to scene 1 or go to scene 4 once applicable
    # B: continue dialogue, option to move back to scene 1 or go to scene 4 once applicable
    # C: continue dialogue, option to move back to scene 1 or go to scene 4 once applicable

    # Consequences:

    # A: plus 1 suspicion
    # B: nothing
    # C: nothing