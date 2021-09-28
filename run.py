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
    
    elif "n" in answer_1:
        print("Thats too bad, hope too see you another day.")
        
    else:
        print("Wrong input try again! ")
        return start()


"""
Calls the start function
"""

start()