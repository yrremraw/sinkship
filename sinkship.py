######################################
#    simple sink ship (2 players)    #
#           (1*1 size ship)          #
#   you can define game board size   #
#            = yrremraw =            #
######################################

from random import randint

# print game board
def print_board(board):
    for row in board:
        print " ".join(row)
        
# random ship position        
def random_row(board):
    return randint(0,len(board)-1)
def random_col(board):
    return randint(0,len(board[0])-1)
    
# create game board
board = []
board_size = int(raw_input("Enter board size: "))
for x in range(board_size):
    board.append(["O"]*board_size)    
print_board(board)
# random ship position
ship_row = random_row(board)
ship_col = random_col(board)

#print ship_row, ship_col

# game start
turn = 1
player1 = True # player1:True, player2:False
while True:
    print "Turn: ", turn
    if turn % 2 != 0:
        print "PLAYER1 turn"
        player1 = True
    else:
        print "PLAYER2 turn"
        player1 = False
    # guess from 0 to board length
    guess_row = int(raw_input("Guess Row: "))-1
    guess_col = int(raw_input("Guess Col: "))-1
    
    # if player guessed right
    if guess_row == ship_row and guess_col == ship_col:
        print "Congrats! You sunk my ship."
        if player1:
            print "PLAYER1 win!"
        else:
            print "PLAYER2 win!"
        break
    # if player guessed wrong
    else:
        # position out of board
        if guess_row not in range(board_size) or guess_col not in range(board_size):
            print "That position isn't even in the ocean"
        # already guessed position
        elif board[guess_row][guess_col] == "X":
            print "You already guessed this position"
        # wrong position
        else:
            "haha! You missed my ship!"
            board[guess_row][guess_col] = "X"
            print_board(board)    
    turn += 1
