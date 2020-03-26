board = [["  ", "  ", "  "], ["  ", "  ", "  "], ["  ", "  ", "  "]]

def get_board():
    print board[0]
    print board[1]
    print board[2]
    print

def valid_move(row, col):
    return row >= 0 and row < 3 and col >= 0 and col < 3 and board[row][col] == "  "

def player_1moves():

    player1_call = "Player 1, your turn. Where would you like to place your %s? Enter in this format: row,column \n" % player_1

    player1_move = raw_input(player1_call)

# Checks validity by calling the valid_move function, whereas the player_2moves() function checks validity another way

    while not valid_move(int(player1_move[0]) - 1, int(player1_move[2]) - 1):
        print "Please enter a valid move!"
        player1_move = raw_input(player1_call)

    while len(player1_move) != 3:
        print "Please enter your choice in the row,column format. No spaces!"
        player1_move = raw_input(player1_call)

    if len(player1_move) == 3:
        while player1_move[1] != ",":
            print "Please enter your choice in the row,column format. Don't forget the comma!"
            player1_move = raw_input(player1_call)

    row = int(player1_move[0]) - 1
    column = int(player1_move[2]) - 1
    board[row][column] = player_1
    get_board()
    print


def player_2moves():

    player2_call = "Player 2, your turn. Where would you like to place your %s? Enter in this format: row,column \n" % player_2

    player2_move = raw_input(player2_call)

    while len(player2_move) != 3:
        print "Please enter your choice in the row,column format. No spaces!"
        player2_move = raw_input(player2_call)

    while int(player2_move[0]) - 1 >= 3 or int(player2_move[2]) - 1 >= 3:
        print "This choice is outside the range of the tic tac toe board. Your selection for row and column should range between 1 and 3"
        player2_move = raw_input(player2_call)

    while int(player2_move[0]) - 1 < 0 or int(player2_move[2]) - 1 < 0:
        print "This choice is outside the range of the tic tac toe board. Your selection for row and column should range between 1 and 3"
        player2_move = raw_input(player2_call)

    while len(board[int(player2_move[0]) - 1][int(player2_move[2]) - 1]) == 1:
        print "This spot has been taken. Please try another spot"
        player2_move = raw_input(player2_call)

    if len(player2_move) == 3:
        while player2_move[1] != ",":
            print "Please enter your choice in the row,column format. Don't forget the comma!"
            player2_move = raw_input(player2_call)

    row = int(player2_move[0]) - 1
    column = int(player2_move[2]) - 1
    board[row][column] = player_2
    get_board()
    print

def check_3_in_a_row():

    #Player 1
    winner = False
    return winner
    
    player1_wins = "Congrats, player 1! You have won the game (:"

    if board[0][0] == player_1 and board[0][1] == player_1 and board[0][2] == player_1:
        print player1_wins
        winner = True
        return winner

    if board[1][0] == player_1 and board[1][1] == player_1 and board[1][2] == player_1:
        print player1_wins
        winner = True
        return winner

    if board[2][0] == player_1 and board[2][1] == player_1 and board[2][2] == player_1:
        print player1_wins
        winner = True
        return winner

    if board[0][0] == player_1 and board[0][1] == player_1 and board[0][2] == player_1:
        print player1_wins
        winner = True
        return winner

    if board[0][1] == player_1 and board[1][1] == player_1 and board[2][1] == player_1:
        print player1_wins
        winner = True
        return winner

    if board[0][2] == player_1 and board[1][2] == player_1 and board[2][2] == player_1:
        print player1_wins
        winner = True
        return winner

    if board[0][0] == player_1 and board[1][1] == player_1 and board[2][2] == player_1:
        print player1_wins
        winner = True
        return winner

    if board[0][2] == player_1 and board[1][1] == player_1 and board[2][0] == player_1:
        print player1_wins
        winner = True
        return winner

    #Player 2

    player2_wins = "Congrats, player 2! You have won the game (:"
    
    if board[0][0] == player_2 and board[0][1] == player_2 and board[0][2] == player_2:
        print player2_wins
        winner = True
        return winner

    if board[1][0] == player_2 and board[1][1] == player_2 and board[1][2] == player_2:
        print player2_wins
        winner = True
        return winner

    if board[2][0] == player_2 and board[2][1] == player_2 and board[2][2] == player_2:
        print player2_wins
        winner = True
        return winner

    if board[0][0] == player_2 and board[0][1] == player_2 and board[0][2] == player_2:
        print player2_wins
        winner = True
        return winner

    if board[0][1] == player_2 and board[1][1] == player_2 and board[2][1] == player_2:
        print player2_wins
        winner = True
        return winner

    if board[0][2] == player_2 and board[1][2] == player_2 and board[2][2] == player_2:
        print player2_wins
        winner = True
        return winner

    if board[0][0] == player_2 and board[1][1] == player_2 and board[2][2] == player_2:
        print player2_wins
        winner = True
        return winner

    if board[0][2] == player_2 and board[1][1] == player_2 and board[2][0] == player_2:
        print player2_wins
        winner = True
        return winner


# Game Begins

get_board()

player_1 = raw_input("Player 1, would you like to be X or O? \n")

while player_1 != "X" and player_1 != "O" and player_1 != "x" and player_1 != "o":
    player_1 = " "
    print "You can only choose X or O. Please try again."
    player_1 = raw_input("Player 1, would you like to be X or O? ")
    print

if player_1 == "X" or player_1 == "x":
    player_1 = "X"
    player_2 = "O"
    print "\nPlayer 2, you will be O\n"
else:
    player_1 = "O"
    player_2 = "X"
    print "\nPlayer 2, you will be X\n"


player_1moves()
player_2moves()

player_1moves()
player_2moves()

player_1moves()


while check_3_in_a_row() == False:
    player_2moves()
    if check_3_in_a_row() == False:
        player_1moves()

print "Game over"

