# Morbidus castle

This is a text based adventure based in python using the template provided by codeinstitute,
the game is a horror/action text adventure set in a dungeon / prison,

The game is build so that players can take on the challange of surviving and gets to make their own path thru the game based on their choices
the games output will change.

## Features

The game is 100% text based made with python. and is intended to get players to interact and have som fun
the choices the player makes has impact on how the story is driven forward, and if the player makes the wrong choices they are punished.
After the player has made the wrong choice and the game ends there is an option to choose to play again from the start, and with each playtru the player can step by step get closer to the goal and win the game.


### Existing features

if elif else: statments, this is the chooices that players will take, one choice will trigger the if statment and another the elif statment, the else statment is provided for correct input validation, 
if wrong input is provided by the player it will trigger the else statment and asks them to try again until a correct input is provided,

all chooices have clear indications on what input has to made to proggress in the story.

Between every print statement there is a time.sleep(2) that gives the player a little breathing room in between text,
of 2 seconds

![Image of start of game]

- __Start of game__

- The start gives player a welcome message and ask if they want to play,
- if player chooses yes the game continues and asks the player to state their name, and a greating if Hello + name is printed,
- if no the message "Thats too bad, hope too see you another day" is printed and the game stops,
- if the player provides wrong input the message "Wrong input try again" is printed and the player gets sent back to start of game again.

![Image of prison scene]

- __First_prison__

- The first scene is printed
- "You wake up in a dark room your hands and feets are tied to a bed"
   "you dont remember how you got there"
   "you hear sounds of foot steps comming closer.
   "What do you do?
   "Try too struggle too get your hands free.
   "Lay still and wait.
   
   "Wait or Struggle?". this is the next choice for the player
   in between every print statment there is a time.sleep that gives the player sometime to read the text before the next line of text is provided.
   after the scene has been printed the game continues with 
   prison2 function
   
   ![Image of prison2 scene]
   
   - __Prison2__
   
   the scene starts with and input from the player 
   Wait or Struggle
   
   
   if struggle 
        "You take all the streangth you have in your body to try too get lose"
        "After a short struggle you get your hands free and can get your feets free"
        "They sounds getting closer and the door opens.
        "What do you do next?"
        "Hide or attack?"
       
   elif wait
       "You here the footsteps get to the room, you hear keys"
       "the doors opens a man enters the room"
       "the man goes up to you, hes clothes is covered in blood"
       "he takes a hold of your arm and takes out a butchers knife"
       "What do you do?"
       "NOT FINISHED YET!"
   
   else:
        "Wrong input try again"
        and players gets asked the question again. until correct input is provided.
   
    
