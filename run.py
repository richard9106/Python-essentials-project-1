"""
Tic tac toe Game the list game zone hepl us to know 
what position the player choose 
"""
from random import randint
RUNINGAME = True
game_zone = [" · "," · "," · ",
             " · "," · "," · ",
             " · "," · "," · ",]
"""
controls in the game if runing
"""


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
    player_name = input("Please Enter your Name\n ")

    print ("Hi "+ player_name + " Please choose a number from 1 to 9")
    print ("the board starts from the upper left corner\n ")

    return player_name

# take player input
def player_choose(patron):
    """
    We put the player choose in a var and compare
    if a right number o it's not already used
    """
    correct = True
    while correct:
        try:
            position = int(input("\n please select your number (1-9)"))
            while not(position >= 1 and position <= 9 and patron[position - 1] == " · "):
                print ("must put a number between 1 and 9")
                position = int(input("\nplease select your number (1-9)"))

            patron[position-1] = " X "
            correct = False
        except ValueError :
            print ("This is a string you must put a number between 1 and 9")

   

    

def pc_choose(patron):
    """
    Generate a random number between 0 and 8
    and add tho the board
    """
    po_position = randint(0,8)
    while patron[po_position] ==" X " or patron[po_position] == " O ":
        po_position = randint(0,8)

    patron[po_position] = " O "

#check for win or tie
def chek_board(patron,player):
    """
    Check if the player or the machine has won
    """

    if player == " X ":#check player "x"
        if (patron[0] ==" X " and patron[1] ==" X " and patron[2] ==" X ") or (patron[3] ==" X " and patron[4] ==" X " and patron[5] ==" X ") or ( patron[6] ==" X " and patron[7] ==" X " and patron[8] ==" X "):
            print ("You win")
            return False
        elif (patron[0] ==" X " and patron[3] ==" X " and patron[6] ==" X ") or (patron[1] ==" X " and patron[4] ==" X " and patron[7] ==" X ") or ( patron[2] ==" X " and patron[5] ==" X " and patron[8] ==" X "):
            print ("You win")
            return False
        elif (patron[0] ==" X " and patron[4] ==" X " and patron[8] ==" X ") or (patron[2] ==" X " and patron[4] ==" X " and patron[6] ==" X "):
            print ("You win")
            return False
    elif player == " O ": #check player "o"
        if (patron[0] ==" O " and patron[1] ==" O " and patron[2] ==" O ") or (patron[3] ==" O " and patron[4] ==" O " and patron[5] ==" O ") or ( patron[6] ==" O " and patron[7] ==" O " and patron[8] ==" O "):
            print ("You Loseeee....")
            return False
        elif (patron[0] ==" O " and patron[3] ==" O " and patron[6] ==" O ") or (patron[1] ==" O " and patron[4] ==" O " and patron[7] ==" O ") or ( patron[2] ==" O " and patron[5] ==" O " and patron[8] ==" O "):
            print ("You Loseeee....")
            return False
        elif (patron[0] ==" O " and patron[4] ==" O " and patron[8] ==" O ") or (patron[2] ==" O " and patron[4] ==" O " and patron[6] ==" O "):
            print ("You loseeee.....")
            return False
    
    return True
# switch the player

# check for win or tie agaion
start_game()
while RUNINGAME:
    print_game_zone(game_zone)
    player_choose(game_zone)
    if not chek_board(game_zone," X "):
        print_game_zone(game_zone)
        break
    else:
        pass
    pc_choose(game_zone)
    if not chek_board(game_zone," O "):
        break
    else:
        pass
        
