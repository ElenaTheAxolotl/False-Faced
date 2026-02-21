


def navigate_to_other_scenes_scene():

    from index import scene_count
    from examine_dresser import dresser
    from examine_closet import closet
    from interactions_at_room_entrance import entrance
    from conclusion_scene import conclusion

    # Scene 4: Base only if both body and room have been visited (realized I wanted it after eheh)
    
    # Description:

    print("\n\nAfter familiarizing yourself with the who and the where-and dealing with your partner-you start looking for more clues")
    print("that will tell you what happened. The dresser under the television has many drawers potentionally containing pieces of")
    print("evidence, and a closet on the other side of the room could be concealing more information. There is also the sound of voices")
    print("coming from the door into the room. They seem to be discussing the current state of the room they are at the entrance to.")

    # Choices:

    while True:
        if scene_count <7:
            print("\nA: The dresser")
            print("B: The closet")
            print("C: The entrance")

            choice4 = input("\nWhere do you go? ").upper()

            if choice4 == "A":
                return dresser()
            elif choice4 == "B":
                return closet()
            elif choice4 == "C":
                return entrance()
            else:
                print("\nNot an option. Please enter A, B, or C.")
        
        else:
            print("\nA: The dresser")
            print("B: The closet")
            print("C: The entrance")
            print("D: Continue")

            choice4 = input("\nWhere do you go? ").upper()

            if choice4 == "A":
                return dresser()
            elif choice4 == "B":
                return closet()
            elif choice4 == "C":
                return entrance()
            elif choice4 == "D":
                return conclusion()
            else:
                print("\nNot an option. Please enter A, B, C, or D.")

    # Outcomes: literally just moving scenes

    # Consequences: none