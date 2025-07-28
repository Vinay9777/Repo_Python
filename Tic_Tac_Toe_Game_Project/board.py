import random

# This function will populate the tic tac toe board in 3*3 board represenation using format strings.
# Populate each blank element of the list to form 3*3 board
def display_board(board):
    print()
    print(F" {board[1]} | {board[2]} | {board[3]}")
    print('---|---|---')
    print(F" {board[4]} | {board[5]} | {board[6]}")
    print('---|---|---')
    print(F" {board[7]} | {board[8]} | {board[9]}")
    print()

def player_input():
    marker = " "

    while marker not in ['X','O']:
        marker = input("Player 1:Do you want to be X or O? ").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if   board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark: 
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    for i in range(1,10):
        if board[i] == ' ':
            return False
            
    return True

def player_choice(board,turn):
    position = 0 
    while position not in range(1,10):
        try:
            position = int(input(F" {turn} enter your next position(1-9): "))
            space_check(board, position)
            if True:
                return position 
                break
        except:
            print("Please enter a valid number between 1 and 9.")

def replay():
    choice = input("Do you want to play again? Enter Yes or No: ").strip().lower()
    return choice == "yes"