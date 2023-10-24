"""
Tic tac toe Game the list game_zone hepl us to know
what position the player choose and the const RUNINGAME help us
to know when the game it's over
"""
from random import randint
RUNINGAME = True
game_zone = [" · ", " · ", " · ", " · ", " · ", " · ", " · ", " · ", " · "]
"""
#controls in the game if runing
"""


def print_game_zone(patron):
    """
    print the game board in to the terminal
    """
    print(patron[0] + "|" + patron[1] + "|" + patron[2])
    print("___________")
    print(patron[3] + "|" + patron[4] + "|" + patron[5])
    print("___________")
    print(patron[6] + "|" + patron[7] + "|" + patron[8])


# start the game with message asking name player
def start_game():
    """
    This function show the rules an ask for name player
    """
    print("----------------------------------")
    print("WELCOME TO TIC TAC TOE!!!!\n ")
    print("In turns, each player will places their pieces.")
    print("The first person to line up their three pieces")
    print("in any direction wins\n ")
    player_name = input("Please Enter your Name\n ")
    print("----------------------------------")
    print("Hi " + player_name + " Now we will decide who it's going to start\n")
    print("Keep in mind that the board starts in the top left corner\n ")
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
            position = int(input("\nplease select your number (1-9)"))
            while not (position >= 1 and position <= 9 and patron[position - 1] == " · "):
                print("The position it's used or the number it's not between 1 and 9")
                position = int(input("\nselect your number (1-9)\n "))
            patron[position-1] = " X "
            correct = False
        except ValueError:
            print("This is a string you must put a number between 1 and 9")


# The computer select a random position
def pc_choose(patron):
    """
    Generate a random number between 0 and 8
    and add tho the board
    """
    po_position = randint(0, 8)
    while patron[po_position] == " X " or patron[po_position] == " O ":
        po_position = randint(0, 8)

    patron[po_position] = " O "
    print(f"\nThe Pc has select position {po_position + 1}")


#select a random number between 1 and 2
def random_number():
    """
    generate a random number between 1 and 2
    """
    number = randint(1, 2)
    return number


# Check for win
def chek_board(patron, player):
    """
    Check if the player or the machine has won
    cheking the rows, columns and diagonals
    """
    rows = [[patron[0], patron[1], patron[2]],
            [patron[3], patron[4], patron[5]],
            [patron[6], patron[7], patron[8]]]
    columns = [[patron[0], patron[3], patron[6]],
            [patron[1], patron[4], patron[7]],
            [patron[2], patron[5], patron[8]]]
    diag = [[patron[0], patron[4], patron[8]],
            [patron[2], patron[4], patron[6]]]
    winner = False
    for i in range(3):
        current_row = rows[i]
        if all(j == player for j in current_row):
            print(f"The player with the {player} has won")
            winner=True
            break
    for i in range(3):
        current_column = columns[i]
        if all(j == player for j in current_column):
            print(f"The player with the {player} has won")
            winner=True
            break
    for i in range(2):
        current_diag = diag[i]
        if all(j == player for j in current_diag):
            print(f"The player with the {player} has won")
            winner=True
            break
    return winner


#the user start first
def user_start_firts(who):
    """
    The user it's the first to play
    """
    print (f"Congrats {who} you start first\n")
    print_game_zone(game_zone)
    while RUNINGAME:
        player_choose(game_zone)  # ask the player for a number
        if chek_board(game_zone, " X "):  # check if we win
            print_game_zone(game_zone)
            break
        print_game_zone(game_zone)
        if check_tie(game_zone):  # check if tie
            break
        pc_choose(game_zone)
        if chek_board(game_zone, " O "):  # check if the pc wins
            print_game_zone(game_zone)
            break
        print_game_zone(game_zone)
        if check_tie(game_zone):  # check if tie
            break

#the user start first
def pc_start_firts(who):
    """
    The user it's the first to play
    """
    print (f"Ups.. {who} the PC start first\n")
    while RUNINGAME:
        pc_choose(game_zone)
        if chek_board(game_zone, " O "):  # check if the pc wins
            print_game_zone(game_zone)
            break
        if check_tie(game_zone):  # check if tie
            break
        print_game_zone(game_zone)
        player_choose(game_zone)  # ask the player for a number
        if chek_board(game_zone, " X "):  # check if we win
            print_game_zone(game_zone)
            break
        print_game_zone(game_zone)
        if check_tie(game_zone):  # check if tie
            break


# Check for Tie
def check_tie(board):
    """
    check if there no any other . in the board
    if no body wins show it's a tie
    """
    if " · " not in board:
        print("THIS IS A TIE......")
        return True

    return False


user = start_game()
who_starts = random_number()
if who_starts == 1:
    user_start_firts(user)
else:
    pc_start_firts(user)
    