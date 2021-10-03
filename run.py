import time

"""
Start of game asking players if they want too play.
if no the game ends with string printed 
(Thats too bad, hope too see you another day.)
if yes players is asked to state their name and the game continues.
if the input is not yes or no, 
player is asked too try again and returned and asked the question again
"""


def start():
    print("Hello and welcome to Morbidus castle ")
    time.sleep(2)
    print("Are you ready too play? \n yes or no ")
    
    answer_1_1 = input(">").lower()
   
    if "yes" in answer_1_1:
        print("Great now please state you name. ")
        name = input()
        time.sleep(2)
        print("Hello " + name)
        time.sleep(2)
        prison()
    
    elif "no" in answer_1_1:
        print("Thats too bad, hope too see you another day.")
        
    else:
        print("Wrong input try again! ")
        time.sleep(2)
        return start()

"""
First scene players are asked if too wait or struggle 
if players input is wait game continues
if players input is struggle game continues
if wrong input player is sent back to start of prison 1
"""


def prison():
    print("You wake up in a dark room your hands and feets are tied to a bed ")
    time.sleep(2)
    print("you dont remember how you got there but you feel a sharp pain in your head ")
    time.sleep(2)
    print("you hear sounds of foot steps comming closer. ")
    time.sleep(2)
    print("What do you do? ")
    time.sleep(2)
    print("Try too struggle too get your hands free. ")
    time.sleep(2)
    print("Lay still and wait. ")
    time.sleep(2)
    print("Wait or Struggle? ")
    time.sleep(2)
    prison2()

# second prison scene


def prison2():
    
    answer_2_1 = input(">").lower()
    
    # checks for players input.
    
    if "struggle" in answer_2_1:
        time.sleep(2)
        print("You take all the streangth you have in your body to try too get lose ")
        time.sleep(2)
        print("After a short struggle you get your hands free and can get your feets free ")
        time.sleep(2)
        print("They sounds getting closer and the door opens ")
        time.sleep(2)
        print("What do you do next? ")
        time.sleep(2)
        print("Hide or attack? ")
        time.sleep(2)
        prison3()
    
    elif "wait" in answer_2_1:
        time.sleep(2)
        print("You here the footsteps get to the room, you hear keys ")
        time.sleep(2)
        print("the doors opens a man enters the room ")
        time.sleep(2)
        print("the man goes up to you, hes clothes is covered in blood ")
        time.sleep(2)
        print("he takes a hold of your arm and takes out a butchers knife ")
        time.sleep(2)
        print("What do you do? ")
        print("")
        
    else:
        print("Wrong input try again ")
        time.sleep(2)
        print("wait or struggle? ")
        return prison2()

# third scene prison


def prison3():
    
    answer_2_2 = input(">").lower()
        
    if "attack" in answer_2_2:
        fight_1()
    
    elif "hide" in answer_2_2:
        print("The man is not dumb and sees you hiding he takes out his butchers knife and chops of your head")
        time.sleep(2)
        print("You die instantly and with no pain. ")
        time.sleep(2)
        print("would you like to play again? ")
        time.sleep(2)
        print("Yes / No")
        time.sleep(2)
        play_again()
        
    else:
        print("Wrong input try again! ")
        print("Hide or Attack? ")
        return prison3()
        

# Asks player if they want to play again when game is lost.


def play_again():
    
    play_again = input(">").lower()
        
    if "yes" in play_again:
        return start()
        
    elif "no" in play_again:
        print("See you some other time! ")
            
    else:
        print("Wrong input try again! ")
        time.sleep(2)
        return play_again()




"""
Calls the start function
"""

start()