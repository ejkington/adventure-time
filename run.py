import time

"""
Start of game asking players if they want too play.
if no the game ends with string printed
(Thats too bad, hope too see you another day.)
if yes players is asked to state their name and the game continues.
if the input is not yes or no,
player is asked too try again and returned and asked the question again
"""
# Grabable object

SWORD = 0

# Cutting down on duplication
REQUIRED = ("Wrong input try again \n")


def start():
    print("Hello and welcome to Morbidus castle \n")
    time.sleep(2)
    
    print("Are you ready too play? \n yes or no \n")
   

    answer_1_1 = input(">").lower().strip()

    if "yes" in answer_1_1:
        print("Great now please state you name.\n")
        name = input()
        time.sleep(2)
        print("Hello\n" + name)
        time.sleep(2)
        prison()

    elif "no" in answer_1_1:
        print("Thats too bad, hope too see you another day.\n")

    else:
        print(REQUIRED)
        time.sleep(2)
        start()


"""
First scene players are asked if too wait or struggle
if players input is wait game continues
if players input is struggle game continues
if wrong input player is sent back to start of prison 1
"""


def prison():
    print("You wake up in a dark room your hands and feets are tied to a bed \n")
    time.sleep(2)
    print("you dont remember how you got there \n")
    time.sleep(2)
    print("you hear sounds of foot steps comming closer. \n")
    time.sleep(2)
    print("What do you do? \n")
    time.sleep(2)
    print("Try too struggle too get your hands free. \n")
    time.sleep(2)
    print("Lay still and wait. \n")
    time.sleep(2)
    print("Wait or Struggle? \n")
    time.sleep(2)
    prison2()

# second prison scene player is asked to struggle or to wait
# if wrong input player is asked to try again and sent back to input field


def prison2():

    answer_2_1 = input(">\n").lower().strip()

    # checks for players input in second scene
    # if wrong input player gets sent
    # back to start of prison2 function.

    if "struggle" in answer_2_1:
        time.sleep(2)
        print("You take all the streangth you have in your body to try too get lose \n")
        time.sleep(2)
        print("After a short struggle you get your hands free and can get your feets free \n")
        time.sleep(2)
        print("They sounds getting closer and the door opens\n")
        time.sleep(2)
        print("What do you do next? \n")
        time.sleep(2)
        print("Hide or attack? \n")
        time.sleep(2)
        prison3()

    elif "wait" in answer_2_1:
        time.sleep(2)
        print("You here the footsteps get to the room, you hear keys \n")
        time.sleep(2)
        print("the doors opens a man enters the room \n")
        time.sleep(2)
        print("the man goes up to you, hes clothes is covered in blood \n")
        time.sleep(2)
        print("he takes a hold of your arm \n")
        time.sleep(2)
        print("What do you do? \n")
        time.sleep(2)
        print("try to run away \n")
        time.sleep(2)
        print("attack him \n")
        time.sleep(2)
        print("Attack or run \n")
        prison4()

    else:
        print(REQUIRED)
        print("wait or struggle? \n")
        prison2()


def prison4():

    answer_2_3 = input("> \n").lower().strip()

    if "attack" in answer_2_3:
        fight1()

    elif "run" in answer_2_3:
        runaway()

    else:
        print(REQUIRED)
        time.sleep(2)
        print("attack or run \n")
        prison4()


def runaway():
    print("The door is open and you make a run for it \n")
    time.sleep(2)
    print("you get out and run down a long hallway its dark and you can barley see \n")
    time.sleep(2)
    print("the end of the hallway is a dead end but you can feel a sharp object leaning against the wall. \n")
    time.sleep(2)
    print("the man in running towards you \n")
    time.sleep(2)
    time.sleep(2)
    print("by the feel of it you think the object is a sword \n")
    time.sleep(2)
    print("do you grab the sword ? \n")
    time.sleep(2)
    print("Yes / No \n")
    choice()

# third scene prison players is asked to attack or to hide
# if wrong input player is asked to try again and sent back to input field


def prison3():

    answer_2_2 = input("> \n").lower().strip()

    if "attack" in answer_2_2:
        fight1()

    elif "hide" in answer_2_2:
        print("The man is sees you hiding he takes out a butchers knife \n")
        time.sleep(2)
        print("and chops of your head. \n")
        time.sleep(2)
        print("You die instantly and with no pain. \n")
        time.sleep(2)
        print("would you like to play again? \n")
        time.sleep(2)
        print("Yes / No \n")
        time.sleep(2)
        play_again1()

    else:
        print(REQUIRED)
        print("Hide or Attack? \n")
        prison3()


def fight1():
    time.sleep(2)
    print("You attack the man, the man turns too you and you are now in a clinch \n")
    time.sleep(2)
    print("the man reaches for his butcher knife \n")
    time.sleep(2)
    print("you grab his hand to try to stop him \n")
    time.sleep(2)
    print("the man is stronger than you and pushes you of \n")
    time.sleep(2)
    print("you fall backwards in the corner of the room on the floor there is a small sword \n")
    time.sleep(2)
    print("do you grab the sword ? \n")
    time.sleep(2)
    print("Yes / No \n")
    choice()

    """
    checks if player choose to pick up the sword
    """


def choice():
    answer_3_1 = input("> \n").lower().strip()
    time.sleep(2)

    # player choose to pick up sword of leave it.

    if "yes" in answer_3_1:
        SWORD = 1

    elif "no" in answer_3_1:
        SWORD = 0

    else:
        print(REQUIRED)
        print("Yes / No \n")
        choice()

    if SWORD > 0:
        print("You grab the sword and point it at the man \n")
        time.sleep(2)
        print("the man runs in full force and the sword pierces him \n")
        time.sleep(2)
        print("the man falls down on the ground and screams \n")
        time.sleep(2)
        print("GET OUT OF HERE! \n")
        time.sleep(2)
        win()
    else:
        print("you dident pick up the sword and are now defenseless \n")
        time.sleep(2)
        print("the man makes quit work of you and you... \n")
        time.sleep(2)
        print("....... \n")
        time.sleep(4)
        print("DIE \n")
        play_again1()


# Asks player if they want to play again when game is lost.


def play_again1():
    print("Do you want to play again ? \n")
    time.sleep(1)
    print("Yes / No \n")

    play_again = input("> \n").lower().strip()

    if "yes" in play_again:
        start()

    elif "no" in play_again:
        print("See you some other time! \n")

    else:
        print(REQUIRED)
        play_again1()

# if player wins the game


def win():
    time.sleep(2)
    print("you made it \n")
    time.sleep(2)
    print("you have escaped the man \n")
    time.sleep(2)
    print("for now.......... \n")
    time.sleep(2)
    print("TO BE CONTINUED. \n")
    play_again1()

    """
    Calls the start function
    """


if __name__ == "__main__":
    start()
