print('Welcome to TIC TAC TOE')

while True:
    # Reset Game
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    players = player_input();
    
    # Choose Player
    player = choose_first()
    
    ready = input('Are you ready to play (Y or N) ?').upper() == 'Y'
    
    while ready:
        
        choice = 0
        
        if player == 'Player 1':
            # Display Board
            display_board(board)
            
            print(player + ' is playing')
            # Choose
            choice = player_choice(board)
            # Update Board
            place_marker(board, players[0], choice)
            display_board(board)
            
            # Check if win or board is full
            if win_check(board, players[0]):
                print('Player 1 WIN!')
                break
            elif full_board_check(board):
                print('TIE!')
                break
                
            player = 'Player 2'
        
        else:
            # Display Board
            display_board(board)
            
            print(player + ' is playing')
            # Choose
            choice = player_choice(board)
            # Update Board
            place_marker(board, players[1], choice)
            display_board(board)
            
            # Check if win or board is full
            if win_check(board, players[1]):
                print('Player 2 WIN!')
                break
            elif full_board_check(board):
                print('TIE!')
                break
                
            player = 'Player 1'
    
    if not replay():
        break