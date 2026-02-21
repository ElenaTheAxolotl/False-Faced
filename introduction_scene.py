


def intro():

    from index import scene_count
    from examine_body import body
    from examine_room import room
    from navigation_scene import navigate_to_other_scenes_scene
    from index import player

    print(scene_count)
    print(player)
    # Scene 1: Intro

    # Description: 

    print("\n\nYou stand in the middle of a hotel room, one barely big enough to fit two beds let alone the amount of people currently")
    print("inspecting it. The most notable part of the room is on the bed nearest to the window. There, under a plastice sheet, lies")
    print("a dead body. It is heavily suspected that foul play is involved. You, the leading detective on this case, must figure out")
    print("what happened to the deceased.\n")

    # Choices:

    while True:
       
       if scene_count <2:
            print("\nA: Inspect the body")
            print("B: Examine the room")

        
            choice1 = input("\nWhat will you do first? (Enter A or B) ").upper()

            if choice1 == "A":
                return body()
            elif choice1 == "B":
                return room()
            else:
                print("\nNot an option. Please enter A or B.")

       else:            
            print("\nA: Inspect the body")
            print("B: Examine the room")
            print("C: Continue")

        
            choice1 = input("\nWhat will you do first? (Enter A or B) ").upper()

            if choice1 == "A":
                return body()
            elif choice1 == "B":
                return room()
            elif choice1 == "C":
                return navigate_to_other_scenes_scene()
            else:
                print("\nNot an option. Please enter A or B.")

    

    # Outcomes: basically just moving to another scene

    # A: get info about dead person (Scene 2)
    # B: get info about the room (Scene 3)

    # Consequences: none for either