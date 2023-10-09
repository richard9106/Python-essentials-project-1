"""
Tic tac toe Game the list game zone hepl us to know 
what position the player choose 
"""
game_zone = [" · "," · "," · ",
             " · "," · "," · ",
             " · "," · "," · ",]

runin_game = True

def print_game_zone(patron):
    """
    print the game board in to the terminal
    """
    print (patron[0] + "|" + patron[1] + "|" + patron[2] )
    print ("___________")
    print (patron[3] + "|" + patron[4] + "|" + patron[5] )
    print ("___________")
    print (patron[6] + "|" + patron[7] + "|" + patron[8] )
    
# start the game with message asking name player
def start_game():
    """
    This function show the rules an ask for name player
    """
    print ("Welcome to tic tac toe\n ")
    print ("In turns, each one places their pieces.")
    print ("The first person to make a row with their three pieces wins\n ")
    player_name = input("Please Enter your Name ")

    print ("Hi "+ player_name + " Please choose a number from 1 to 9")
    print ("the board starts from the upper left corner\n ")

    return player_name

# take player input
def player_choose(patron):
    """
    We put the player choose in a var and compare
    if a right number o it's not already used
    """       
    position = int(input("please select your number (1-9)"))
    print (position)

    if position >= 1 and position <= 9 and patron[position - 1] == " · ":
        patron[position-1] = "X"
    else:
        print ("The Number in not correct or that position is used")



#check for win or tie

# switch the player

# check for win or tie agaion
user = start_game()
while runin_game:
    print_game_zone(game_zone)
    player_choose(game_zone)
