# Michelle Yoon
# UCID : 30189382
# Tutorial 8
# overall features: user gets to choose a starting pattern among the 7 options. 6 options are the precreated patterns and 7th option is a file where user has to input. If user chooses the precreated pattern, the program will execute the corresponding def function and return "oldWorld".
#                           The program then counts the number of the neighborhoods around the critter (returns 'counts') and apply the rules of 'birth and death' for the 'new world'  in apply_rules function (retern newWorld).
#                           Finally program executes display function, printing both 'old world' and 'new world'. Every new turn, new world of the previous turn has to be the old world. Data has to be copied.
#                           If the user selected 7th option, the program will prompt the user to insert the file name. after that, instead of corresponding def function like above fileRead function will read the text file. The rest is same as the above,
#
# program limitations: 1. Only the first line of the input file is shown.
#                                 2. Debugging statements do not show the coordinates of the each critters.
#                                3. new world is not shown in the turn 0
# program version: 12. 06. 2023. (12th draft)

SIZE = 10  #constant

# startingPattern()
#prompting user to choose the starting pattern. If the user choose to open a existing text file, the program executes readFile function.
#If not, program executes the corresponding functions.
# input function used. retrun corresponding functions.
# the pattern chosen by the user will be the "old world"

def startingPattern():
    print("6 starting patterns")
    print("(a) oneEmpty")
    print("(b) twoSingleCritter")
    print("(c) threeSingleBirth")
    print("(d) fourthSimpleBirth")
    print("(e) fifthCreateListEdgeCases")
    print("(f) sixthComplexCases")
    print("(g) input file")
    choice = input("Choose your starting pattern= ")
    

    if choice == "a":
        return oneEmpty()
    elif choice == "b":
        return twoSingleCritter()
    elif choice == "c":
        return threeSingleBirth()
    elif choice == "d":
        return fourthSimpleBirth()
    elif choice == "e":
        return fifthCreateListEdgeCases()
    elif choice == "f":
        return sixthComplexCases()
    elif choice == "g":
        return fileRead()


# function executed when the user choose "a"
# retrun value: oldWorld list
def oneEmpty():
    startingPattern = "one empty"
    oldWorld = []
    oldWorld = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(oldWorld)

# function executed when the user choose "b"
# retrun value: oldWorld list
def twoSingleCritter():
    oldWorld = []
    oldWorld = [
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(oldWorld)

# function executed when the user choose "c"
# retrun value: oldWorld list
def threeSingleBirth():
    oldWorld = []
    oldWorld = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " ","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(oldWorld)

# function executed when the user choose "d"
# retrun value: oldWorld list
def fourthSimpleBirth():
    oldWorld = []
    oldWorld = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", "*","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " ","*", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(oldWorld)

# function executed when the user choose "e"
# retrun value: oldWorld list
def fifthCreateListEdgeCases():
    oldWorld = []
    oldWorld = [
     ["*"," ", "*"," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", "*", " "],
     ["*","*", " "," ", " ", " ", " ", " ", " ", "*"]
    ]
    return(oldWorld)

# function executed when the user choose "f"
# retrun value: oldWorld list
def sixthComplexCases():
    oldWorld = []
    oldWorld = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", "*", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", "*", " ", " ", " ", " "],
     [" "," ", " ","*", "*", "*", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(oldWorld)

# fileRead()
# reads the text file user inserts.
# While True loop used to prompt the user until they  enter a valid name of file.
# if the fileis empty, it displays that it is an empty file
# return values: grades, numRows, maxColumns
def fileRead():
    while True:
        try:
            filename = input("Enter the name of the input file: ")
            with open(filename, "r") as inputfile:
                lines = inputfile.readlines()

                if not lines:
                    print("%s is an empty file" % filename)
                    continue

                oldWorld = [list(line.strip()) for line in lines]  #reads each line from the lines list, strips any leading or trailing whitespace  and converts the resulting string into a list of characters.

                maxColumns = max(len(row) for row in oldWorld)
                
                oldWorld_list = []
                for row in oldWorld:
                    new_row = row + [" "] * (maxColumns - len(row))
                    oldWorld_list.append(new_row)
                    
                numRows = len(oldWorld)

                return oldWorld, numRows, maxColumns

    

        except IOError:
                print("Problem reading from file %s" % filename)






# count_live_neighbors()
# count the number of neighbors around the critter.
# this function lets the program know how the new world should look like
# i , j used to locate critters ( coordinates)
# return value: count 
def count_live_neighbors(world, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (0 <= row + i < SIZE) and (0 <= col + j < SIZE) and (world[row + i][col + j] == "*"):
                count = count +  1
    return count

#apply_rules()
#this function applys the rule of 'birth and death' to the old world list and make a new list ( it doesn't print yet)
#rules of 'birth and death'
# 1) if there are 3 neighbors in old world, birth happens according to the corresponding location in the new world.
# 2) if there are zero or one neighbors in old world, the critter is considered as "lonely", which ends up death.
#     if there are more than 4 neighbors in old world, the world is over crowded, which also ends up in death.
# 3) if there are 2 or 3 neighbors in old world, the  critter survives and live in the new world.
# r and c is in the range of 0 to 10
# debugging statement is only shown when the user types "d" or else, they aren't shown.
#returns newWorld.  This passes newWorld parameter to the display function and print.
def apply_rules(oldWorld, selection):
    newWorld = [[" " for _ in range(SIZE)] for _ in range(SIZE)]

    for r in range(SIZE):
        for c in range(SIZE):
            live_neighbors = count_live_neighbors(oldWorld, r, c)

            if oldWorld[r][c] == " ":
                # Rule for birth: Empty square with exactly three neighbors
                if live_neighbors == 3:
                    newWorld[r][c] = "*"
                    if (selection == "d"):
                        debugOn = True
                        print( "# Debugging: There are three neighbors in the old world. So a birth occurs in the corresponding loaction in the new world.")
            elif newWorld[r][c] == " ":  # No birth or death
                if (selection == "d"):
                    debugOn = True
                    print("# Debugging: Critter continues to live in the corresponding location because there are 3 neighbors")

            elif oldWorld[r][c] == "*":
                # Rules for death: Critter too lonely or overpopulated
                if live_neighbors < 2 or live_neighbors > 3:
                    newWorld[r][c] = " "  # Death
                    if (selection == "d"):
                        debugOn = True
                        print("# Debugging: Death occurs because critter was too lonely ( zero or one neighbors in the old world) or critter has been over crowded ( has four or more neighbors in the old world)")
            else:
                # Rule for survival: Critter with 2 or 3 neighbors
                newWorld[r][c] = "*"
                if (selection == "d"):
                     debugOn = True
                     print("# Debugging: Critter continues to live in the corresponding location because there are either 2 or 3 neighbors")

    return (newWorld)


#display()
# this function prints the output in the way programmer wanted.
# i and r are used in the range of 0 to 10. Since this program should print 10 X 10 2D list, this range sets the boundary of the output.
# "Turn #%d" %turn" shows the current turn. it gets bigger every time. turn= turn +1
#copy data from oldWorld to newWorld. Every turn, data newWorld  from the previous turn becomes data of oldWorld
# return value: none

def display(turn, oldWorld, newWorld):        # Displays a row at a time of each list
    currentRow = 0
    currentColumn = 0
    print("Turn #%d" %turn)
    print("BEFORE\t\t\tAFTER")
    
    for r in range (SIZE):
        # Row of dashes before each row of old and new list
        # (Dashes for old list)
        for i in range (SIZE): 
            print("%s" %(" -"), end="")
        print("#\t",end="")
        # (Dashes for new list)
        for i in range (SIZE): 
            print("%s" %(" -"), end="")
        print()

        # Display one row of old world list
        for c in range (SIZE):
            # Display: A vertical bar and then element (old list)
                #while (currentRow < numRows) and (currentColumn <numRows): #
                    print("|%s" %(oldWorld[r][c]), end = "")
        # Separate the lists with a number sign and a tab
        print("", end = "#\t")    
      # Display one row of new world list
        for c in range (SIZE):
            # Display: A vertical bar and then element (new list)
            #while (currentRow < numRows) and (currentColumn <numRows): #
                print("|%s" %(newWorld[r][c]), end = "")
        print("|")

    # Row of dashes after end of last row (old world list)
    for i in range (SIZE): 
        print("%s" %(" -"), end="")
    print("#\t",end="")

    # Row of dashes after end of each row (new world list)
    for i in range (SIZE): 
        print("%s" %(" -"), end="")
    print()

#start()
# starting execution point
# used while loop so that the program runs until the user wants to end by entering "q" or "Q".
# return value = selection

def start():
    running = True
    oldWorld = startingPattern()
    newWorld = [[" " for _ in range(SIZE)] for _ in range(SIZE)] # set the boundary of output
    turn = 0
    debugOn = False # set as a local variable. (default)
    
    display(turn, oldWorld, newWorld)
    while running:
        selection =input("Press 'q' or 'Q' to quit. If not, just hit enter=")  #need to add functions to end this loop
        if (selection == "q") or (selection == "Q"):
            running = False
        if (selection == "d"):
            debugOn = True # when the user types "d", the debugging statements will be shown in the next turn.
        turn = turn + 1   # shows how many turns there were so far
        newWorld = apply_rules(oldWorld, selection)
        display(turn, oldWorld, newWorld)
        oldWorld = newWorld
    return selection

start()



