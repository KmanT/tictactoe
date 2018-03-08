print("Tic-Tac-Toe!")

first_check = True #True = X | False = O
game_over = False
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def marker_set(first_check): #Default is True
    if first_check == True:
        return 'X'
    else:
        return 'O'

def display_board(board):
    print(' 1_____2_____3')
    for row in board:
        print(row)
    pass
    # print('|'+board[0][0]+'|____|'+board[0][1]+'|____|'+board[0][2]+'|')
    # print('|'+board[1][0] + '|____|' + board[1][1] + '|____|' + board[1][2]+'|')
    # print('|'+board[2][0] + '|____|' + board[2][1] + '|____|' + board[2][2]+'|')

display_board(board)

def empty_check(position): #Returns false when the position is filled with an X or O
    if position == 'X' or position == 'O':
        return False
    else:
        return True

def player_change(first_check): #Changes players from X to O or vice versa
    if first_check == True:
        return False
    else:
        return True

def position_check(position, row):
    if position[0] == row:
        return True


def player_input(first_check, board):
    print('The current marker is: ' + marker_set(first_check))
    print("Enter the spot you want to mark off. ex: 'a1', or 'c3'.")
    position = input('pos:')
    marker = marker_set(first_check)
    row = -1
    column = int(position[1]) - 1
    if position[0] == 'a':
        row = 0
    elif position[0] == 'b':
        row = 1
    elif position[0] == 'c':
        row = 2
    else:
        row = -1

    if row >= 0 and row < 3 and column >= 0 and column < 3:
        if empty_check(board[row][column]) == True:
            board[row][column] = marker
        else:
            print("That position is filled. Choose another position.")
    elif row < 0 or row > 2:
        print("Choose a through c for a row.")
    elif column < 0 or column > 2:
        print("Choose numbers 1-3 for your column")

    display_board(board)

def win_check(board):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X': #first row
        return True
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        return True
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X': #second row
        return True
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        return True
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X': #third row
        return True
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        return True
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X': #first column
        return True
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        return True
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X': #second column
        return True
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        return True
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X': #third column
        return True
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        return True
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X': # \ diagonal
        return True
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X': # / diagonal
        return True
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return True
    else:
        return False

def full_check(board):
    if board[0:][0:] == ' ':
        return False
    else:
        True

while game_over == False:
    player_input(first_check, board)
    first_check = player_change(first_check)
    game_over = win_check(board)

first_check = player_change(first_check)

print('Player ' + marker_set(first_check) + ' is the winner!')
