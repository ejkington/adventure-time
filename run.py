import time
import random

"""
Start of game asking players if they want too play.
if no the game ends with string printed
(Thats too bad, hope too see you another day.)
if yes players is asked to state their name and the game continues.
if the input is not yes or no,
player is asked too try again and returned and asked the question again
"""
# Grabable object

sword = 0

#Cutting down on duplication
required = ("Wrong input try again \n")


def start():
    print("Hello and welcome to Morbidus castle")
    time.sleep(2)
    print("Are you ready too play? \n yes or no")

    answer_1_1 = input(">").lower()

    if "yes" in answer_1_1:
        print("Great now please state you name.")
        name = input()
        time.sleep(2)
        print("Hello\n" + name)
        time.sleep(2)
        prison()

    elif "no" in answer_1_1:
        print("Thats too bad, hope too see you another day.")

    else:
        print(required)
        time.sleep(2)
        start()


"""
First scene players are asked if too wait or struggle
if players input is wait game continues
if players input is struggle game continues
if wrong input player is sent back to start of prison 1
"""


def prison():
    print("You wake up in a dark room your hands and feets are tied to a bed")
    time.sleep(2)
    print("you dont remember how you got there")
    time.sleep(2)
    print("you hear sounds of foot steps comming closer.")
    time.sleep(2)
    print("What do you do?")
    time.sleep(2)
    print("Try too struggle too get your hands free.")
    time.sleep(2)
    print("Lay still and wait.")
    time.sleep(2)
    print("Wait or Struggle?")
    time.sleep(2)
    prison2()

# second prison scene player is asked to struggle or to wait
# if wrong input player is asked to try again and sent back to input field


def prison2():

    answer_2_1 = input(">").lower()

    # checks for players input in second scene
    # if wrong input player gets sent
    # back to start of prison2 function.

    if "struggle" in answer_2_1:
        time.sleep(2)
        print("You take all the streangth you have in your body to try too get lose")
        time.sleep(2)
        print("After a short struggle you get your hands free and can get your feets free")
        time.sleep(2)
        print("They sounds getting closer and the door opens")
        time.sleep(2)
        print("What do you do next?")
        time.sleep(2)
        print("Hide or attack?")
        time.sleep(2)
        prison3()

    elif "wait" in answer_2_1:
        time.sleep(2)
        print("You here the footsteps get to the room, you hear keys")
        time.sleep(2)
        print("the doors opens a man enters the room")
        time.sleep(2)
        print("the man goes up to you, hes clothes is covered in blood")
        time.sleep(2)
        print("he takes a hold of your arm and takes out a butchers knife")
        time.sleep(2)
        print("What do you do?")
        print("")

    else:
        print(required)
        print("wait or struggle?")
        prison2()

# third scene prison players is asked to attack or to hide
# if wrong input player is asked to try again and sent back to input field


def prison3():

    answer_2_2 = input(">").lower()

    if "attack" in answer_2_2:
        fight1()

    elif "hide" in answer_2_2:
        print("The man is sees you hiding he takes out a butchers knife")
        time.sleep(2)
        print("and chops of your head.")
        time.sleep(2)
        print("You die instantly and with no pain.")
        time.sleep(2)
        print("would you like to play again?")
        time.sleep(2)
        print("Yes / No")
        time.sleep(2)
        play_again1()

    else:
        print(required)
        print("Hide or Attack?")
        prison3()


def fight1():
    time.sleep(2)
    print("You attack the man, the man turns too you and you are now in a clinch")
    time.sleep(2)
    print("the man reaches for his butcher knife")
    time.sleep(2)
    print("you grab his hand to try to stop him")
    time.sleep(2)
    print("the man is stronger than you and pushes you of")
    time.sleep(2)
    print("you fall backwards in the corner of the room on the floor there is a small sword")
    time.sleep(2)
    print("do you grab the sword ?")
    time.sleep(2)
    print("Yes / No")
    choice()
    

def choice():
    answer_3_1 = input(">").lower()
    time.sleep(2)
    
    # player choose to pick up sword of leave it.
    
    if "yes" in answer_3_1:
        sword = 1
        fight2()
    
    elif "no" in answer_3_1:
        sword = 0
        fight2()
    else:
        print(required)
        print("Yes / No")
        choice()


def fight2():
    
    if sword > 0:
        print("You grab the word and point it at the man")
        time.sleep(2)
        print("the man runs in full force and the sword pierces him to the bottom")
        time.sleep(2)
        print("the man falls down on the ground and wispers")
        time.sleep(2)
        print("GET OUT OF HERE!")
        time.sleep(2)
        win()
    else:
        print("you dident pick up the sword and are now defenseless")
        time.sleep(2)
        print("the man makes quit work of your life and you...")
        time.sleep(2)
        print("DIE")
        play_again1()

# Asks player if they want to play again when game is lost.


def play_again1():

    play_again = input(">").lower()

    if "yes" in play_again:
        start()

    elif "no" in play_again:
        print("See you some other time!")

    else:
        print(required)
        play_again1()
        
# if player wins the game


def win():
    print("You won the game!")
    time.sleep(2)
    print("have a cookie")
    play_again1()
 
    
    """
    Calls the start function
    """


start()
