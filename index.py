# detective game heheheheheh

suspicion = 0
inventory = []
scene_count = 0

# Dictionary ig (Object JSON) I don't think I can use this anywhere rn but good to know

# mech1 = {
#    "type": "flying",
#    "color": "red",
#    "hp" = 100
# }

def intro ():

    # Scene 1: Intro
    print(scene_count)
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
                return base()
            else:
                print("\nNot an option. Please enter A or B.")

    

    # Outcomes: basically just moving to another scene

    # A: get info about dead person (Scene 2)
    # B: get info about the room (Scene 3)

    # Consequences: none for either

def body ():

    # Scene 2: The Body

    # Description:

    #scene_count +=1

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
            #suspicion +=1
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


def room ():

    # Scene 3: The Room

    # Description:

    #scene_count +=1

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
            #suspicion +=1
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

# I need a way to prompt the base scene but only if all of the previous scenes have been visited how do?????


def base ():

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
                return end()
            else:
                print("\nNot an option. Please enter A, B, C, or D.")

    # Outcomes: literally just moving scenes

    # Consequences: none


def entrance ():

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
            return entranceA()
        elif choice5 == "B":
            return entranceB()
        elif choice5 == "C":
            return base()
        else:
            print("\nNot an option. Please enter A, B, or C.")

    # Outcomes: again, basically just moving scenes

    # A: scene 5.1
    # B: scene 5.2
    # C: scene 4

    # Consequences: none


def entranceA ():

    # Scene 5.1: The Young Man

    # Description:

    #scene_count +=1

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
            #suspicion +=1
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


def entranceB ():

    # Scene 5.2: The Staff Member

    # Description:

    #scene_count +=1

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
            #suspicion +=1
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


def dresser ():

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
            return base()
        else:
            print("\nNot an option. Please enter A, B, or C.")

    # Outcomes: scene traveling oooOOOOooooOOOOOOoooooooo

    # A: scene 6.1
    # B: scene 6.2
    # C: scene 4

    # Consequences: none

def dresserA ():

    # Scene 6.1: The Glass

    # Description:

    #scene_count +=1

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
            #suspicion +=2
            inventory.append("glass")
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

def dresserB ():

    # Scene 6.2: The Drawers

    # Description:

    #scene_count +=1

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
            inventory.append("paper")
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


def closet ():

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
            return base()
        else:
            print("\nNot an option. Please enter A or B.")

    # Outcomes:

    # A: 7.1
    # B: 4

    # Consequences: nothing

def safe ():

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

        if choice71 == "A" and "paper" in inventory:
            #print("write description for the sake of turning the assignment in I will write later")
            code = input("\nEnter code: ")
            if code == "4514":
                return diary()
            else:
                print("\nIncorrect. Try again.")
                return safe ()
        elif choice71 == "A" and "paper" not in inventory:
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

def diary ():

    # Scene 7.2: Diary

    # Description:

    #scene_count +=1

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
            #suspicion +=2
            inventory.append("diary")
            input("\nPress Enter to go back")
            return safe()
        elif choice72 == "B":
            #print("write description for the sake of turning the assignment in I will write later")
            input("\nPress Enter to go back")
            return safe()
        else:
            print("\nNot an option. Please enter A or B.")

    # Outcomes:

    # A: you take the diary, put in pocket, prompt to go back
    # B: you leave the diary, someone from forensics comes over to see if it's evidence, prompt to go back

    # Consequences:

    # A: plus 2 suspicion
    # B: nothing

# also need a way to prompt this scene but only if all of the previous scenes have been visited maybe variables are 
# always the answer I don't knoowwwwwwww

def end ():

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
            if suspicion <4:
                return end1()
            elif suspicion >3 and inventory ["paper"]:
                return end2()
            else:
                return end3()
        elif choice8 == "B":
            return base()
        else:
            print("\nNot an option. Please enter A or B.")

    # Outcomes:

    # A: win/lose results
    # B: Return to scene 4, will now have option to leave

    # Consequences: nothing

def end1 ():

    # Scene 8.1: Ending 1

    # Description: suspicion less than 4

    print("\n\nYou head to the door leading out of the room, the young man and the staff member having already left. Before stepping out,")
    print("you take one last look at the covered corpse lying on the bed. It is still, quiet, peaceful even. You take a breath and exit")
    print("the room, for once not feeling extremely irritated by the ever present feeling of your partner never far behind you.")
    print("You continue working on the case throughout the following month. Although the autospsy does provide confirmation that the")
    print("death was caused by cyanide poisoning, there is no conclusive evidence that another party was involved. The young man's")
    print("alibi of being at the restaurant was proven to be true, and no one else came forward with any evidence to point towards")
    print("it being a murder. The only suggestion of such a thing was found within the pages of the deceased's diary, where he seemed")
    print("to endlessly ramble on about his family's death being a conspiracy and that he was going to be killed next.")
    print("The case was ruled as a suicide, attribing the contents of the diary as proof of a distressed mental state and paranoia that")
    print("led to the deceased taking his own life.")
    print("When the ruling was given, your partner gave you an...odd look and said, \"I'm not sure how I feel about this whole thing.")
    print("\n\"It leaves a bitter taste in my mouth.\"")
    
    print("\nYou got away with it.\n")

def end2 ():

    # Scene 8.2: Ending 2

    # Description: suspicion greater than or equal to 4, inventory not have glass or diary
    
    #print("I have to rewrite this cus I realized the inventory served no purpose otherwise I will write later I just wanna turn the 
    # assignment in right now mate"

    print("\nYou were caught.\n")

def end3 ():

    # Scene 8.3: Ending 3

    # Description suspicion greater than or equal to 4, inventory has glass and/or diary

    #print("gonna write this later hope this is fine for now just can't do it tonight brain hurt from variables no work
    # wow this is over 700 lines of code already my goodness and it's just gonna get longer hope it's not too bad
    # reading it all geez")

    print("\nYou were caught.\n")

# to start the game mwahahahaha this'll only play the intro, body, and room scenes though cus idk how do to do what I
# want to move on to the rest boooooo
intro ()