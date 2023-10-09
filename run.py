"""
Tic tac toe Game the list game zone hepl us to know 
what position the player choose 
"""
game_zone = [" · "," · "," · ",
             " · "," · "," · ",
             " · "," · "," · ",]

def print_game_zone(game_zone):
    """
    print the game board in to the terminal
    """
    print (game_zone[0] + "|" + game_zone[1] + "|" + game_zone[2] )
    print ("___________")
    print (game_zone[3] + "|" + game_zone[4] + "|" + game_zone[5] )
    print ("___________")
    print (game_zone[6] + "|" + game_zone[7] + "|" + game_zone[8] )
    
# start the game with message asking name player
def start_game():
    """
    This function show the rules an ask for name player
    """
    print ("Welcome to tic tac toe\n ")
    print ("In turns, each one places their pieces.")
    print ("The first person to make a row with their three pieces wins\n ")
    player_name = input("Please Enter your Name ")


# take player input

#check for win or tie

# switch the player

# check for win or tie agaion

start_game()
print_game_zone(game_zone)
