


def entrance():

    from navigation_scene import navigate_to_other_scenes_scene

    # Scene 5: The Enterance

    # Description:

    print("\n\nAt the entrance to the room stands one of the members of the hotel's staff and a young man, close to if not the same age")
    print("as the deceased. They are talking to one of the officers, supposedly about the dead body in the room. You walk to the")
    print("doorway where they stand, going to get information from them as well, your partner following you like a pathetic hound as you")
    print("approach...\n")

    # Choices:

    print("\nA: The young man")
    print("B: The staff member")
    print("C: Go back")

    while True:
        choice5 = input("\nWho will you speak to first? ").upper()

        if choice5 == "A":
            return young_man_conversation()
        elif choice5 == "B":
            return staff_member_conversation()
        elif choice5 == "C":
            return navigate_to_other_scenes_scene()
        else:
            print("\nNot an option. Please enter A, B, or C.")

    # Outcomes: again, basically just moving scenes

    # A: scene 5.1
    # B: scene 5.2
    # C: scene 4

    # Consequences: none

def young_man_conversation():

    global scene_count

    from index import scene_count
    from index import raise_suspicion

    # Scene 5.1: The Young Man

    # Description:

    scene_count =+ 1

    print("\n\nThe young man appears quite distressed about the situation and your presence does not seem to be of any help. The police")
    print("officer tells you the man's name and that he was a friend of the deceased, having been travling with him. Turning to you")
    print("without making eye contact, the young man starts to recount his memory of earlier tongiht.")
    print("\"We had planned to go to that medieval restaurant thing nearby, made a reservation and everything, but Lucas had been stuck")
    print("in bed all day with a stuffy nose, and it didn't seem like he'd feel any better by the time we would have to leave. He")
    print("told me to go ahead without him, that he'd just ask the hotel for something, so I did...but when I got back...\" the man")
    print("glances at the body on the bed and shuts his eyes as he swallows before continuing, \"he hasn't been...wasn't in the best")
    print("headspace ever since his family died...almost like he was paranoid he'd be next...")

    print("\n\"I should've stayed with him, actually talked to him about everything he went through with his family...\"")

    # Choices:

    print("\nA: \"It is a shame they all died so recently.\"")
    print("B: \"He must have been carrying a lot of grief.\"")
    print("C: \"Thank you for your cooperation.\"")

    while True:
        choice51 = input("\nWhat do you say? ").upper()

        if choice51 == "A":
            #print("continue dialouge for the sake of turning the assignment in I will write later")
            raise_suspicion(1)
            input("\nPress Enter to go back")
            return entrance()
        elif choice51 == "B":
            #print("continue dialouge for the sake of turning the assignment in I will write later")
            input("\nPress Enter to go back")
            return entrance()
        elif choice51 == "C":
            return entrance()
        else:
            print("\nNot an option. Please enter A, B, or C.")

    # Outcomes: both continue dialouge (include comment from partner and friend sayin twasnt suicide) and prompt to go back

    # Consequences:

    # A: plus 1 suspicion
    # B: nothing
    # C: nothing


def staff_member_conversation():

    global scene_count

    from index import scene_count
    from index import raise_suspicion

    # Scene 5.2: The Staff Member

    # Description:

    scene_count =+ 1

    print("\n\nThe staff member appears to be simply annoyed by the situation, but the constant tapping of her foot and erratic movement")
    print("of her eyes reveal a person riddled with anxiety, possibly even fear. The police office tells you her name and position as")
    print("a member of the cleaning department. Crossing her arms, the staff member starts to explain what she knows about the situation.")
    print("\"I was cleaning this hallway like any other day. There wasn't anyone else scheduled to clean this hall, but someone joined me")
    print("and cleaned the side of the hall this room is on. Couldn't tell you if she went into this room or not, and she left as soon")
    print("as she was done with her side. Don't remeber who it was either. I thought we could check the security cameras, but then I")
    print("rememberd we don't have any.")

    print("\n\"Hopefully someone literally dying in here is a good enough reason for the owners to put some proper security measures in...\"")

    # Choices:

    print("\nA: \"Security is very important when housing people.\"")
    print("B: \"The current security here does not pose as an obstacle for an intruder.\"")
    print("C: \"Thank you for your cooperation.\"")

    while True:
        choice52 = input("\nWhat do you say? ").upper()

        if choice52 == "A":
            #print("continue dialouge for the sake of turning the assignment in I will write later")
            input("\nPress Enter to go back")
            return entrance()
        elif choice52 == "B":
            #print("continue dialouge for the sake of turning the assignment in I will write later")
            raise_suspicion(1)
            input("\nPress Enter to go back")
            return entrance()
        elif choice52 == "C":
            return entrance()
        else:
            print("\nNot an option. Please enter A, B, or C.")

    # Outcomes: both continue dialouge (include comment from partner) and prompt to go back

    # Consequences:

    # A: nothing
    # B: plus 1 suspicion
    # C: nothing