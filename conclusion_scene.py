


def conclusion():

    from navigation_scene import navigate_to_other_scenes_scene
    from index import player
    from endings import ending1
    from endings import ending2
    from endings import ending3

    # Scene 8: Conclusion only show as option at base if all other scenes have been visited idk how to do that right now

    # Description:

    print("\n\n\"Well, I think this has been a productive investigation thus far,\" your partner comments, stretching his arms. Has he even")
    print("done anything worthy of being called 'productive'? He yawns as he continues, \"Not the optimal time to have it though. I")
    print("think it's just about time for the sun to come out...\" Looking at you, he puts his hands on his hips. \"I'm guessing you")
    print("already have an idea of what happened in mind, but I think it's best we leave any further investigation for after we get")
    print("some rest.")

    print("\n\"So, you ready to head back to the station, lead detective?\"")

    # Choices:

    print("\nA: Leave")
    print("B: Go back")

    while True:
        choice8 = input("\nWhat will you do? ").upper()

        if choice8 == "A":
            if player["suspicion"] <4:
                return ending1()
            elif player["suspicion"] >3 and "glass" in player["inventory"] or "diary" in player["inventory"]:
                return ending2()
            else:
                return ending3()
        elif choice8 == "B":
            return navigate_to_other_scenes_scene()
        else:
            print("\nNot an option. Please enter A or B.")

    # Outcomes:

    # A: win/lose results
    # B: Return to scene 4, will now have option to leave

    # Consequences: nothing