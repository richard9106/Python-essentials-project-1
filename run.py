"""
Tic tac toe Game the list game zone hepl us to know 
what position the player choose 
"""
from random import randint

game_zone = [" · "," · "," · ",
             " · "," · "," · ",
             " · "," · "," · ",]
"""
controls in the game if runing
"""
runinGame = True

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
    position = int(input("\n please select your number (1-9)"))
    while not(position >= 1 and position <= 9 and patron[position - 1] == " · "):
        print ("The number is not correct or the position it's used")
        position = int(input("\n please select your number (1-9)"))
    patron[position-1] = " X "


def pc_choose(patron):
    """
    Generate a random number between 0 and 8
    and add tho the board
    """
    po_position = randint(0,8)
    while patron[po_position] ==" X " or patron[po_position] == " O ":
        po_position = randint(0,8)

    print (po_position)
    patron[po_position] = " O "

#check for win or tie
def chek_board(patron,player):
    """
    Check if the player or the machine has won
    """
    if player == " X ":
        


    elif player == " O ":

    return False    

# switch the player

# check for win or tie agaion
user = start_game()
while runinGame:
    print_game_zone(game_zone)
    player_choose(game_zone)
    chek_board(game_zone," X ")
    pc_choose(game_zone)
    chek_board(game_zone," O ")
