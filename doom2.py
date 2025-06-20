# Michelle Yoon
# version: Nov1, Nov2, Nov.3rd 2023
# Program features: 
# 1. Rule of the game
#    a. Living room: player has to pick up a ball of string
#    b. Attic: pick a piece of cheese and drop the ball of string down the hole. ( when the ball of string is dropped to the bedroom, the black Tom cat will leave and the mouse will come out.)
#    c. Bedroom: feed the cheese to the mouse then the mouse will fertilize the pot. 
#    d. Livingroom: observe the pot again, player will notice there is a plant growing.==game won!
# four functions are used. Three are the locations (living room, attic, and bed room). One is the start function. This program runs with one while loop that is in the start function and each functions run with various 'if' branches.
# 2. limitations: this program has a lot of bodies of words repeated. This lowers the readability of the code. It doesn't tell if the player have finished all the tasks that satisfy the condition to win the game. Player has to check the pot by itself.


# Constants for room names
LIVING_ROOM = "living room"  # Using various strings tend to make errors. The program is still running but the player cannot move from functions (locations) to functions(locations). Which shows that the program doesn't return the parameters.
ATTIC = "attic"              # To fix this problem, Global constants are used in this program.
BEDROOM = "bedroom"

# Constants for game state
POT_DRY = "dry"
POT_FERTILIZED = "fertilized"
STRING_NOT_PICKED = "not picked"
STRING_PICKED = "picked"
STRING_DROPPED = "dropped"
CHEESE_NOT_PICKED = "not picked"
CHEESE_PICKED = "picked"



# Define room functions
def living_room(current_room, pot, stringBall, cheese):                  # if-elif-else branches are used to show various conditions.
    # Display room description and options                               # Since options are shown and disappeard according to the game status, branches were needed to print out options selectively. 
    if stringBall == STRING_NOT_PICKED:
        print("You are in the living room.")
        print("(a) Examine the pot of soil")
        print("(b) Go up the stairs to the attic")
        print("(c) Enter the dark entranceway to the bedroom")
        print("(d) Pick up the ball of string")
    else:
        stringBall == STRING_PICKED
        print("You are in the living room.")
        print("(a) Examine the pot of soil")
        print("(b) Go up the stairs to the attic")
        print("(c) Enter the dark entranceway to the bedroom")
        
    

    # Get player's selection
    selection = input("Select your action: ")
    print()
        
    if (selection == "a"):
        if (pot == POT_DRY):
            print("The pot of soil looks dry.")
        elif (pot == POT_FERTILIZED):
            # print("A vine has grown from the pot, leading to paradise. You win the game!")
             current_room = "won"  #this is the point where the while loop ends. (game ends)
    elif (selection == "b"):
        current_room = ATTIC # the switch of the location
    elif (selection == "c"):
         current_room = BEDROOM  # the switch of the location
    elif (selection == "d"):
        if (stringBall == STRING_NOT_PICKED): # This condition is added to print out the proper options.  As the condition got complicated, even the stringBall was picked, the options included "4. Pick up the ball of string"
            stringBall = STRING_PICKED        # adding this branch made the program clear what condition the game is currently in and return the variables
            print("You picked up the ball of string.")
        else:
            print("Invalid input. Please try again.")
    print()

    return current_room, pot, stringBall, cheese

def attic(current_room, pot, stringBall, cheese):
    # Display room description and options
    if (stringBall != STRING_DROPPED) and (stringBall == STRING_PICKED): #
        print("You are in the attic.")
        print("(a) Pick up cheese and try to drop it down the hole")
        print("(b) Pick up cheese and keep it")
        print("(c) Drop the ball of string down the hole")
        print("(d) Go down the stairs to the living room")

    elif (stringBall == STRING_DROPPED) or (stringBall != STRING_PICKED): # these two conditions are in the same line because when in both conditions, "3. Drop the ball of string down the hole". shouldn't be shown.
        print("You are in the attic.")
        print("(a) Pick up cheese and try to drop it down the hole")
        print("(b) Pick up cheese and keep it")
        print("(d) Go down the stairs to the living room")
        

    # Get player's selection
    selection = input("Select your action: ")
    print()

    if (selection == "a"):
        print("The cheese is too big to fit down the hole.")
    elif (selection == "b"):
        cheese = CHEESE_PICKED
        print("You picked up the cheese.")
    elif (selection == "c"):
         if (stringBall != STRING_DROPPED): # This condition is added to print out the proper options.  As the condition got complicated, even the stringBall was picked, the options included "3. Drop the ball of string down the hole".
            stringBall = STRING_DROPPED     # adding this branch made the program clear what condition the game is currently on and return the values.
         print("The ball went down to the bedroom.")
         print("Tom cat takes the ball and leaves the room")
         print("Once Tom cat is gone, the mouse comes out of the mouse hole.")
         print("You have to feed this mouse with the cheese.")
         print("The mouse should be out by now.")
    elif (selection == "d"):
        print("(d) Go down the stairs to the living room")
        current_room = LIVING_ROOM
    else:
        print("Invalid input. Please try again.")
    print()
    return current_room, pot, stringBall, cheese

def bedroom(current_room, pot, stringBall, cheese):
    # Display room description and options
    print("You are in the bedroom where Tom cat and mouse live.")
    print("Black Tom cat likes to look into the mouse hole.")
    if (stringBall == STRING_PICKED):
        print("(a) Use the string to play with the cat")
        print("(c) Go through the dark entranceway to the living room")
    elif (stringBall == STRING_DROPPED) and (cheese == CHEESE_PICKED): #(stringBall == STRING_PICKED) wasn't included because the program didn't pass the parameter "cheese == CHEESE_PICKED"
        print("(b) Feed cheese to the mouse")                          #before this, the program interpreted STRING_PICKED and STRING_DROPPED as  independent actions while they are in fact dependent. STING_PICKED can be done alone but STRING_DROPPED can happen only after STRING_PICKED.
        print("(c) Go through the dark entranceway to the living room")  
   
    else:
        (cheese != CHEESE_PICKED)           # when neither the stringBall is dropped nor picked and the cheese also isn't picked, there is nothing you can do in the bedroom. 
        print("(c) Go through the dark entranceway to the living room")  
    

    # Get player's selection
    selection = input("Select your action: ")
    print()

    if (selection == "a") and (stringBall == STRING_PICKED):               #and is used to show all kinds of conditions.
        print("The cat briefly plays with the string but then returns to watch the mouse hole.")
    elif selection == "b": # cheese == CHEESE_PICKED
        print("You fed the cheese to the mouse.")
        pot = POT_FERTILIZED
        print("The mouse fertilized the pot in the living room and came back to the bed room.")
        print("You can feed the mouse as much as you want.")
        
    elif (selection == "c"):
        current_room = LIVING_ROOM
    else:
        print("Invalid input. Please try again.")
    print()

    return current_room, pot, stringBall, cheese

def start():
    current_room = LIVING_ROOM
    pot = POT_DRY
    stringBall = STRING_NOT_PICKED
    cheese = CHEESE_NOT_PICKED
    # Initialize game state
    stringBall = "not picked"
    pot = "dry"
    cheese = "not picked"
    current_room = "living room"
    while (current_room != "won"):  #this is the condition of the while loop.
        if current_room == LIVING_ROOM:
            current_room, pot, stringBall, cheese = living_room(current_room, pot, stringBall, cheese)  # all of the parameters are used as a return values
        elif current_room == ATTIC:
            current_room, pot, stringBall, cheese = attic(current_room, pot, stringBall, cheese)
        elif current_room == BEDROOM:
            current_room, pot, stringBall, cheese = bedroom(current_room, pot, stringBall, cheese)

    print("Congratulations! There is a magic beanstalk growing.")
    print("It carries you up to paradise. You have won the game!")

# Start the game
start()
