


def body():

    import state
    from introduction_scene import intro
    from state import raise_suspicion


    # Scene 2: The Body

    # Description:

    state.scene_count + 1

    print("\nThe deceased is a young man named Lucas Park, a nobody in the grand scheme of things. The file on him you were provided")
    print("with revealed nothing substantial. The only things of note were that he had no known living relatives and had been")
    print("arrested with charges of assult and battery, though the charges were dropped before a trial was held.")
    print("You step to where the body lay on the bed. Lifting the plastic covering you see...a face of peace. There is no hint of")
    print("pain or fear, almost as though the body is simply sleepiing. It has not been long enough for the body to start decaying.")
    print("Peace is all you see...")
    print("You lower the plastic covering over the body again as you hear your...partner walking over to the body.")
    print("\"You know, I guess being in bed isn't the worst place to die,\" he says, irritately relaxed. \"Though I can't imagine it's")
    print("a super comfortable bed.\" You still cannot fathom how he got this job, let alone why you are forced to have him as a")
    print("work partner.")

    print("\n\"What say you, lead detective? What do you think happened to this guy?\"\n")

    # Choices:

    print("\nA: \"Forensics has not confirmed anything yet.\"")
    print("B: \"It was poison.\"")
    print("C: Ignore him")

    while True:
        
        choice2 = input("\nYour answer (Enter A, B, or C): ").upper()

        if choice2 == "A":
            #print("continue dialouge for the sake of turning the assignment in I will write later")
            input("\nPress Enter to go back")
            return intro()
        elif choice2 == "B":
            #print("continue dialouge for the sake of turning the assignment in I will write later")
            raise_suspicion(1)
            input("\nPress Enter to go back")
            return intro()
        elif choice2 == "C":
            #print("continue dialouge for the sake of turning the assignment in I will write later")
            input("\nPress Enter to go back")
            return intro()
        else:
            print("\nNot an option. Please enter A, B, or C.")

    # Outcomes: (will add the actual dialouge later and gotta figure out how to track which scenes have been done)

    # A: body1: continue dialogue, option to move back to scene 1 or go to scene 4 once applicable
    # B: body2: continue dialogue, option to move back to scene 1 or go to scene 4 once applicable
    # C: body3: continue dialouge, option to move back to scene 1 or go to scene 4 once applicable

    # Consequences:

    # A: nothing
    # B: plus 1 suspicion
    # C: nothing