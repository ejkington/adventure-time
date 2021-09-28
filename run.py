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
    print("Are you ready too play? please use yes or no ")
    
    answer_1 = input(">").lower()
   
    if "y" in answer_1:
        print("Great now please state you name. ")
        name = input()
        print("Hello " + name)
        prison()
    
    elif "n" in answer_1:
        print("Thats too bad, hope too see you another day.")
        
    else:
        print("Wrong input try again! ")
        return start()


def prison():
    print("You wake up in a dark room your hand and feets are tied to a bed ")
    print("you dont remember how you got there but you feel a sharp pain in your head ")
    print("you hear sounds of foot steps comming closer. ")
    print("What do you do? ")
    print("Try too struggle too get your hands free. ")
    print("Lay still and wait. ")
    print("Please type Wait or Struggle ")
    
    answer_2 = input(">").lower()
    
    if "struggle" in answer_2:
        print("You take all the streangth you have in your body to try too get lose ")
        print("After a short struggle you get your hands free and can get your feets free ")
        print("What do you do next? ")
        print("")
        
    elif "wait" in answer_2:
        print("You here the footsteps get to the room, you hear keys ")
        print("the doors opens and a entity enters the room ")
        print("the entity is a man and goes up to you, hes clothes is covered in blood ")
        print("he takes a hold of your arm and takes out a butchers knife ")
        print("What do you do? ")
        print("")
        
    else:
        print("Wrong input try again ")
        return prison()

"""
Calls the start function
"""

start()