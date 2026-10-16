# 99NITF
# This is just for me btw Theme: Idle Fingers (Online Python Interpreter)
#     ****************************************************
""" SET UP INSTRUCTIONS:
1. Copy this text/code
2. Find a PYTHON interpreter
3. Paste the code into the left or top of the website where the inline code is
4. Run the code and fullscreen to avoid clutter; you might have to scroll for some dialogue
      ****************************************************
WARNING:
Best used on laptops/computers, mobile devices don't usually perform well and it's such a squished experience.
      ****************************************************
NOTES:
1. No graphics, purely text.
2. MY own little story of 99 Nights in the Forest, this is NOT canon, it's a small fan-game essentially.
3. Constantly being updated.
4. This is just an almalgamation of what I've learned of Python so far; there might be bugs.
5. Answer exactly with the same spelling or choice (case sensitive); I don't have safegaurds yet
      ****************************************************
"""
#     ^^ Instructions
#     ****************************************************
import time
#     time.sleep for delay in text; defaults to seconds
#     ^^ imports
#     ****************************************************
Welcome = "Welcome to a 99NITF simulation..."
#     ^^ Intro
#     ****************************************************
def dot ():
    print()
    print()
    print()
#     ^^ Extra
#     ****************************************************
Pelt_Trades = {"revolver ammo", "good axe", "good sack"}
#     ^^ Pelt Trader
#     ****************************************************
safe = "Safe... for tonight"
ended = "You've survived."
ending0 = "You died..."
ending1 = "Got lost along the way..."
ending2 = "Ranger: Well damn, another missing person in this god forsakened forest."
endings = [ending0, ending1, ending2]
day_counter = 0

def day(ending = " ", count = "no"):
    day_counter = 1
    global safe, ended, ending0, ending1, ending2, endings
    if ending == " ":
        print()
    elif ending == safe:
        day_counter += 1
    print(ending)
    if day_counter == 1:
        dayz = "day"
    else:
        dayz = "days"
    if count == "yes":
        time.sleep(1)
        print("********************Day", day_counter, "***********************************")
    elif count == "MPR":
        print(f"""
                        MISSING PERSON REPORT
              Name: ********* ********** *********
                    Last Seen: {day_counter} {dayz} ago
                    @ a nearby the forest
                         
                         
        If ********* is found, please report immediantly
                       to local authorities
        """)
#     ^^ Endings
#     ****************************************************
inventory = {
    "axe":"old axe",
    "sack":"old sack"}
#     ^^ Player items / equips
#     ****************************************************
def sit1():
    time.sleep(0.5)
    choiceboard = {
    "A)" : "Camping",
    "B)" : "Nothing…",
    "C)" : "What are YOU doing out here?"}
    print("Ranger: What are you doing out here?")
    print("Choices:")
    print(choiceboard)
    dot()
    time.sleep(0.5)
    choice7 = input("Choose: ")
    print()
    if choice7 == "A":
        print("You:", choiceboard["A)"])
        print("Ranger: you can't be out here… didn't you see the sign?", "You: Sign…? What?", "Ranger: You didn't see the sign...?", "Ranger: Darn these cultists-", sep="\n")
    elif choice7 == "B":
        print("You:", choiceboard["B)"])
        print("Ranger: You better find yourself out of these woods kid.", "You: Alright, alright. I'll get out of here-", sep="\n")
    elif choice7 == "C":
        print("You:", choiceboard["C)"])
        print("Ranger: I'm doing my job, trying to keeping curious kids like YOU out of this mess.", "you've survived", "...for now.", sep="\n")
        day_counter = day_counter + 1
    elif choice7 == "D":
        print("You: *runs*", "Ranger: Hey, get back here!", "booom", sep="\n")
    else:
        dot()
        print("A quiet rustling of foliage can be heard behind you.", "Ranger: We have to go!", "you've survived", "...for now.", sep="\n")
        day_counter = day_counter + 1
def sit2():
    time.sleep(1)
    print("Night passes by and strange noises fill the forest...")
    time.sleep(3)
    print("morning shines through the forest trees")
#     ^^ Situations
#     ****************************************************
# Resources ^
print(Welcome,"********************Day 1***********************************", "You've finally obtained a bunny foot after a days hard work!", sep="\n")
time.sleep(1.5)
print()
print()
#     ^^ Game begin
#     ****************************************************
choice1 = input("Would you like to trade your bunny foot with the Pelt Trader? ")
if choice1 == "yes":
    time.sleep(1)
    print()
    print("Trading with the Pelt Trader...")
    time.sleep(1)
    print()
    time.sleep(1)
    print()
    print(Pelt_Trades)
    choice2 = input("Choose an item: ")
    time.sleep(0.3)
    if choice2 == "revolver ammo":
            print("Received revolver ammo")
            inventory["ammo"] = "revolver ammo"
    elif choice2 == "good axe":
            print("Received good axe")
            inventory["axe"] = "good axe"
    elif choice2 == "good sack":
            print("Received good sack")
            inventory["sack"] = "good sack"
else: 
    inventory["item1"] = "bunny foot"
#     ^^ Game event 1: Pelt Trading
#     ****************************************************
dot()
time.sleep(2)
print("inventory:")
print(inventory)
print("Come back next time")
dot()
time.sleep(3)
#     ^^ Situations
#     ****************************************************
print("Night is approaching")
print()
time.sleep(1.5)
choice3 = input("Go outside your campfire? ")
if choice3 == "yes":
    if inventory["axe"] == "good axe":
        choice4 = input("Take your axe? ")
        print()
        if choice4 == "yes":
            time.sleep(1)
            print("... Taking axe")
            time.sleep(3)
            dot()
            print("As you approach the darkness outside your campfire you hear footsteps behind you...")
            choice5 = input("Pick a number, 1 or 0, your life depends on this. ")
            if choice5 == "1":
                time.sleep(1)
                print("... a wolf!")
                time.sleep(0.3)
                choice6 = input("Use axe? ")
                if choice6 == "yes":
                    time.sleep(0.3)
                    print("Obtained two morsels and a wolf pelt!")
                    print()
                    time.sleep(2)
                    sit1()
                else:
                    dot()
                    day(ending0, "no")
            else:
                print()
                print("...", "a deer?", "...", sep="\n")
                print()
                day(ending2, "no")
        else:
            day(ending1, "no")
    else:
        day(ending1, "no")
else:
    day(safe, "yes")
    dot()
    sit2()

# ****************************************************************
# Endings redirect
print()
if endings:
        print("Restart game to survive the night")
        day(" ", "MPR")
else:
        print("Restart game to achieve a diff ending")
