from tictactoe_functions.py import *
'''
in this block we are arranging the function inside the loops to make the game
work 
'''
while True:
    # inatilizing a blank board (list)
    the_board = [" "] * 10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn +"will go frist")
    #askinf players they ready or not 
    ready = input("ready to play y or n ")
    if ready == "y":
        game_on = True
        show()
    else:
        game_on = False
    while game_on:
        
        if turn  == "player1":
            #show the board 
            print_board(the_board)
            #choose the position
            position = player_choice(the_board)
            #place the marker on the board 
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check(the_board,player1_marker):
                print_board(the_board)
                print(" player1 has won the game")
                game_on = False
            # or check if there is tie
            else:
                if full_board_check(the_board):
                    print_board(the_board)
                    print("Tie game")
                    game_on = False
                else:
                    turn = "player2"

            
        else:
            #show the board 
            print_board(the_board)
            #choose the position
            position = player_choice(the_board)
            #place the marker on the board 
            place_marker(the_board,player2_marker,position)
            #check if they won
            if win_check(the_board,player2_marker):
                print_board(the_board)
                print(" player2 has won the game")
                game_on = False
            #or check if there is tie
            else:
                
                if full_board_check(the_board):
                    print_board(the_board)
                    print("Tie game")
                    game_on = False
                else:
                    turn = "player1"

    if not replay():
        break 



