from board import display_board,player_input,place_marker,win_check,choose_first,space_check,full_board_check,player_choice,replay

# Initially create a list with blank elements, this will be used to form 3*3 board representation
board = [" " for _ in range(10)]

print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(F" {turn} will go first")

    game_on = input("Shall we start the game(Yes/No):").strip().lower() == 'yes'

    if game_on:
        print('Starting game...')
    else:
        print('Exiting game')
        break
        
    while game_on:
        if turn == 'Player 1':
            display_board(board)
            pos = player_choice(board,turn)
            place_marker(board, player1_marker, pos)

            if win_check(board,player1_marker):
                display_board(board)
                print('Player 1 has won the game')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("It's a draw")
                break
            else:
                turn = "Player 2"
        else:
            display_board(board)
            pos= player_choice(board,turn)
            place_marker(board, player2_marker, pos)

            if win_check(board,player2_marker):
                display_board(board)
                print('Player 2 has won the game')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print("It's a draw")
                break
            else:
                turn = "Player 1"

    if not replay():
        print("Thanks for playing Tic Tac Toe!")
        break