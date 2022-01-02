### Live site

• https://adventuretimems3.herokuapp.com/

### Github repo

• https://github.com/ejkington/adventure-time

# Morbidus castle

This is a text based adventure based in python using the template provided by codeinstitute,
the game is a horror/action text adventure set in a dungeon / prison,

The game is build so that players can take on the challange of surviving and gets to make their own path thru the game based on their choices
the games output will change.

## Target audience

Anyone who enjoys a simple text based adventure,


## Features

The game is 100% text based made with python. and is intended to get players to interact and have som fun
the choices the player makes has impact on how the story is driven forward, and if the player makes the wrong choices they are punished.
After the player has made the wrong choice and the game ends there is an option to choose to play again from the start, and with each playtru the player can step by step get closer to the goal and win the game.


![Startscreen](#)
## User stories

### As a developer:

• I want to provide the user with a simple but enjoyable game

• I want to create an immersive story causing the user to feel weight to each choice being made.

• I want to provide the user with clear gameplay instructions.
 

### As a new user:

• I want to understand how the game works 

• I want the game to set the scene drawing me into the story

• I want the choices being made to feel like they have consequences

• I want the game to have a compelling story

• I want the game to establish a clear win or lose protocol, in the form of survival or death

• Once the game is completed, I want an option to play again

### Existing features

if elif else: statments, this is the chooices that players will take, one choice will trigger the if statment and another the elif statment, the else statment is provided for correct input validation, 
if wrong input is provided by the player it will trigger the else statment and asks them to try again until a correct input is provided,

all chooices have clear indications on what input has to made to proggress in the story.

Between every print statement there is a time.sleep(2) that gives the player a little breathing room in between text,
of 2 seconds

## Features to be added  

•	The option for the user to save their outcome which can be carried over to later sequels

•	Add more choices and more content,

•  More complex system for items and grabable objects (inventory for player) (more stuff to interact with in the game)

## How to play

The game begins with instructions to the user to simply survive, followed by the question if they want to proceed with the game. 

## Functions

The game will progress with use of functions. Functions of individual chapters will trigger story progression. Giving the user opportunity to interact with objects. Each function will end when the user is faced  with another choice to make to continue the story.

## Choices

Each choice will consist of two options representing two different paths the user can take.
Once the story comes to an end whether it be successful or not the user will be asked whether they would like to play again. 
Selecting yes restarts the game. 

## Invalid input checks

During each choice if the user’s input is invalid, they will be prompted to try again

## Technologies used

•	Python

•	Heroku

•	GitHub

•	Gitpod


## Testing

### Functionality testing

I have manually tested this project by doing the following:

•	Played all possible choices and outcomes to ensure all functions work correctly.

•	Given invalid options.

•	Tested in my local terminal and Heroku terminal.

## User stories testing

### As developer:

• I want to provide the user with a simple but enjoyable game

The simple mechanics of the game allow the user to shape the story by typing their answers when prompted 

• I want to provide the user with clear gameplay instructions

The user is prompted when and what to input to progress the story


### As a new user:

• I want to understand how the game works 

The user is prompted when and what to input to progress the story

• I want the game to effectively set the scene

• Once the game is completed, I want an option to play again
   
## Issues during development

• Mainly misspelling or calling a function before it exists,

• Had proplems implenting grabbable objects (SWORD) before i read up on how to solve it.


### Bugs found on PEP8

•	Unwanted white spaces

•	Incorrect indentation

•	Incorrect line spaces between functions

•	Too many characters on one line

### Adding and commiting files

To add files to the repository take the following steps

In the command line type -
        git add .  
        git commit -m "This is being committed"
        git push

To add all new files or modified file use " ."  - To add a single file use the pathway to the file eg .index.html  or assets/css/style.css
When committing make sure your comments are clear about what changes have been made. 
Pushing will send your work to the repository

### Deployment 

The project was deployed with the following steps

* Logged into git hub
* Clicked the "Settings" button in the menu above the Repository.
* Scroll down the Settings page to the "GitHub Pages" Section.
* Under "Source", click the dropdown called "None" and then select "Master Branch".
* The page will automatically refresh, and a link displaced.  It may take some time for the link to show the website.
* If the page will not load go down to "template" under the "source" and select a template. 
* Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

## Deployment Heorku

The project was deployed using Code Institutes mock terminal for Heroku

Deployment steps:

•	Fork or clone this repository.

•	Ensure the Profile is in place.

•	requirements.txt can be left empty as this project does not use any external libraries

•	Create a new app in Heroku

•	Select "New" and "Create new app"

•	Name the new app and click "Create new app"

•	In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list)

•	Whilst still in "Settings", click "Reveal Config Vars" and input the folloing. KEY: PORT, VALUE: 8000. Nothing else is needed here as this project does not have any sensitive files

•	Click on "Deploy" and select your deploy method and repository

•	Click "Connect" on selected repository.

•	Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section

•	Heroku will now deploy the site

### Live site

• https://adventuretimems3.herokuapp.com/

### Github repo

• https://github.com/ejkington/adventure-time

### Design and content inspiration

•	My roleplaying friends and the adventure we are curently playing

## Thanks

Special thank you to roleplaying Gamemaster Niklas Björk for comming up with the basis for my adventure
    
