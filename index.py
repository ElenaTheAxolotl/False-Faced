# detective game heheheheheh

# def scene1 ():

# Scene 1: Intro

# Description: 

print("\nYou stand in the middle of a hotel room, one barely big enough to fit two beds let alone the amount of people currently")
print("inspecting it. The most notable part of the room is on the bed nearest to the window. There, under a plastice sheet, lies")
print("a dead body. It is heavily suspected that foul play is involved. You, the leading detective on this case, must figure out")
print("what happened to the deceased.\n")

# Choices:

print("\nA: Inspect the body")
print("B: Examine the room")

choice1 = input("\nWhat will you do first? (Enter the letter) ")

# Outcomes: basically just moving to another scene

# A: get info about dead person (Scene 2)
# B: get info about the room (Scene 3)

# Consequences: none for either


# Scene 2: The Body

# Description:

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

choice2 = input("\nYour answer: ")

# Outcomes: (will add the actual dialouge later and gotta figure out how to track which scenes have been done)

# A: continue dialogue, option to move back to scene 1 or go to scene 4 once applicable
# B: continue dialogue, option to move back to scene 1 or go to scene 4 once applicable
# C: continue dialouge, option to move back to scene 1 or go to scene 4 once applicable

# Consequences:

# A: minus 1 suspicion
# B: plus 1 suspicion
# C: nothing


# Scene 3: The Room

# Description:

print("\nLooking around the room, there is not much to see. A few forensics workers are looking for evidence, but the room is")
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

choice3 = input("\nYour answer: ")

# Outcomes:

# A: continue dialogue, option to move back to scene 1 or go to scene 4 once applicable
# B: continue dialogue, option to move back to scene 1 or go to scene 4 once applicable
# C: continue dialogue, option to move back to scene 1 or go to scene 4 once applicable

# Consequences:

# A: plus 1 suspicion
# B: minus 1 suspicion
# C: nothing


# Scene 4: Base (realized I wanted it after eheh)

# Description:

print("\nAfter familiarizing yourself with the who and the where-and dealing with your partner-you start looking for more clues")
print("that will tell you what happened. The dresser under the television has many drawers potentionally containing pieces of")
print("evidence, and a closet on the other side of the room could be concealing more information. There is also the sound of voices")
print("coming from the door into the room. They seem to be discussing the current state of the room they are at the entrance to.")

# Choices:

print("\nA: The dresser")
print("B: The closet")
print("C: The entrance")

choice4 = input("\nWhere do you go? ")

# Outcomes: literally just moving scenes

# Consequences: none


# Scene 5: The Enterance

# Description:

print("\nAt the entrance to the room stands one of the members of the hotel's staff and a young man, close to if not the same age")
print("as the deceased. They are talking to one of the officers, supposedly about the dead body in the room. You walk to the")
print("doorway where they stand, going to get information from them as well, your partner following you like a pathetic hound as you approach...\n")

# Choices:

print("\nA: The young man")
print("B: The staff member")
print("C: Go back")

choice5 = input("\nWho will you speak to first? ")

# Outcomes: again, basically just moving scenes

# A: scene 5.1
# B: scene 5.2
# C: scene 4

# Consequences: none


# Scene 5.1: The Young Man

# Description:

print("\nThe young man appears quite distressed about the situation and your presence does not seem to be of any help. The police")
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

choice51 = input("\nWhat do you say? ")

# Outcomes: both continue dialouge (include comment from partner and friend sayin twasnt suicide) and prompt to go back

# Consequences:

# A: plus 1 suspicion
# B: minus 1 suspicion
# C: nothing


# Scene 5.2: The Staff Member

# Description:

print("\nThe staff member appears to be simply annoyed by the situation, but the constant tapping of her foot and erratic movement")
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

choice52 = input("\nWhat do you say? ")

# Outcomes: both continue dialouge (include comment from partner) and prompt to go back

# Consequences:

# A: minus 1 suspicion
# B: plus 1 suspicion
# C: nothing


# Scene 6: The Dresser

# Description:

print("\nThe dresser is fairly thin but makes up for its width with length spanning half of the wall. The dark wood frame contains")
print("a plethora of white-stained drawers for you to look through, though there is also glass sitting on top of the dresser that")
print("seems to have been once filled with milk.")

# Choices:

print("\nA: Examine the glass")
print("B: Examine the drawers")
print("C: Go back")

choice6 = input("\nWhat do you look at? ")

# Outcomes: scene traveling oooOOOOooooOOOOOOoooooooo

# A: scene 6.1
# B: scene 6.2
# C: scene 4

# Consequences: none

# Scene 6.1: The Glass

# Description:

print("\nYou take your gloves out of your pocket and put them on before picking up the glass. There is still a small bit of milk")
print("remaining at the bottom. Upon sniffing it, you smell the distinct smell of almonds, but it is not like almond milk. It is")
print("a bitter scent, one much like what you smelled on the body. One like cyanide.")

# Choices:

print("\nA: Take the glass")
print("B: Leave the glass")

choice61 = input("\nWhat do you do? ")

# Outcomes:

# A: you take the glass, put in pocket perhaps, prompt to go back
# B: you leave the glass, parnter asks about it, prompt to go back

# Consequences:

# A: plus 2 suspiscion, glass in inventory
# B: nothing

# Scene 6.2: The Drawers

# Description:

print("\nYou start opening the drawers, look though them, and promptly close them once you see they are completely empty. Any personal")
print("belongings in the room are in the suitcases, but something catches your eye as you look through the last drawer; there is a")
print("small, torn piece of paper tucked into the back corner of the drawer.")

# Choices:

print("\nA: Take the paper")
print("B: Leave the paper")

choice62 = input("\nWhat do you do? ")

# Outcomes:

# A: you take the paper, see "DEAD" written on it, put in pocket, prompt to go back
# B: you leave the paper, prompt to go back

# Consequences:

# A: paper in inventory
# B: nothing


# Scene 7: The Closet

# Description:

print("\nUpon opening the door to the closet, you see that it is completely empty. There is not even an irioning board")
print("like many other hotels often have. All there is are hangers not being used...and a dark shape in the corner. You realize it")
print("is a safe the hotel provides hidden in the dark corner of the closet.")

# Choices:

print("\nA: Examine the safe")
print("B: Go back")

choice7 = input("\nWhat do you do? ")

# Outcomes:

# A: 7.1
# B: 4

# Consequences: nothing

# Scene 7.1: The Safe

# Description:

print("\nYou crouch down to the floor of the closet and bring the safe out of the corner, turning it so the keypad to enter the code")
print("is facing you. It appears to be a simple four digit code. Gently shaking the safe produces a sound of something moving within")
print("the containment. Something someone cared enough about to have wanted to keep it hidden.")

# Choices:

print("\nA: Enter code")
print("B: Go back")

choice71 = input("\nWhat do you do? ")

# Outcomes:

# A: if paper in inventory, describe paper again and prompt to enter code; else prompt to go back
# B: scene 7

# Consequences:

# A: if code right, scene 7.2; else say incorrect and prompt enter code again
# B: nothing

# Scene 7.2: Code

# Description:

print("\nEntering the correct code and opening the safe reveals...a small diary. There does not seem to be anything else in the")
print("safe; it is just the diary. Upon closer inspection, you see-printed in bold letters on the front of the diary-the")
print("deceased's name.")

# Choices:

print("\nA: Take the diary")
print("B: Leave the diary")

choice72 = input("\nWhat do you do? ")

# Outcomes:

# A: you take the diary, put in pocket, prompt to go back
# B: you leave the diary, someone from forensics comes over to see if it's evidence, prompt to go back

# Consequences:

# A: plus 2 suspicion
# B: nothing


# Scene 8: Conclusion

# Description:

print("\n\"Well, I think this has been a productive investigation thus far,\" your partner comments, stretching his arms. Has he even")
print("done anything worthy of being called 'productive'? He yawns as he continues, \"Not the optimal time to have it though. I")
print("think it's just about time for the sun to come out...\" Looking at you, he puts his hands on his hips. \"I'm guessing you")
print("already have an idea of what happened in mind, but I think it's best we leave any further investigation for after we get")
print("some rest.")

print("\n\"So, you ready to head back to the station, lead detective?\"")

# Choices:

print("\nA: Leave")
print("B: Go back")

choice8 = input("\nWhat will you do? ")

# Outcomes:

# A: win/lose results
# B: Return to scene 4, will now have option to leave

# Consequences: nothing

# Scene 8.1: Win

# Description: suspicion less than 4

print("\nYou head to the door leading out of the room, the young man and the staff member having already left. Before stepping out,")
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
print("\"It leaves a bitter taste in my mouth.\"")
 
print("You got away with it.")

# Scene 8.2: Lose

# Description: suspicion greater than or equal to 4
 
print("\nYou head to the door leading out of the room, the young man and the staff member having already left. But before you can")
print("step out of the doorway, your partner roughly grabs your wrist as his face dawns a such a serious expression that it is")
print("almost unnerving.")
print("\"Wait,\" he begins, \"I have something to say. I know you're the lead detective on this case, but I've been doing some deducing")
print("of my own and have come to an important conclusion.\" He stands up straight, his grip not having loosened on your wrist.")
print("\"I am going to add a potential suspect to the investigation.\" An unsettling smile crosses his face. \"That suspect is you,")
print("Victoria Corvi.\" You are unable to stop your body from going rigid at the sound of those words.")
print("\"I take my job very seriously, you know. And now I've seen enough tonight to justify my suspicions of you. I hope you didn't")
print("think you could get away with murder that easily.\"")
print("You knew you hated him for a reason.")

print("You were caught.")