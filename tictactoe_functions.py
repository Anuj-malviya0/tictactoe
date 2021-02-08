#step 1
'''
here board is in a form of list and this function displays it in the form of tic
tac toe board
'''
def print_board(board):
    print('\n'*10)
    print(board[7]+" | ",board[8]+" | ",board[9])
    print("--|----|---")
    print(board[4]+" | ",board[5]+" | ",board[6])
    print("--|----|---")
    print(board[1]+" | ",board[2]+" | ",board[3])
#step 2
'''
this functiom is not taht important but it displays the at initial stage so that
playear can get familiar with the board  
'''
def show():
    print ("The board setup looks like this \n")
    
    print("1"+" | ","2"+" | ","3")
    print("--|----|---")
    print("4"+" | ","5"+" | ","6")
    print("--|----|---")
    print("7"+" | ","8"+" | ","9")

#step 3
'''
this function takes input from user for the marker of player 1 andreturns the
marker in tuple format
    (player1, player2)
'''
def player_input():  
    marker = " "
    while marker != "X" and marker != "O":
        marker = input("player1 enter your marker ").upper()        
    if marker == "X":
        return ("X","O")
    else:
        return ("O","X")


#step 4
'''
this function asks the user for their move and places their marker on the desired
position 
'''
def place_marker(board,marker,position):
    board[position] = marker

#step 5
'''
this function checks the win scenarios for both the players 
'''
def win_check(board,mark):
    return ((board[1] == mark and board [2] == mark and board[3] == mark) or #row
    (board[4] == mark and board [5] == mark and board[6] == mark) or #row
    (board[7] == mark and board [8] == mark and board[9] == mark) or #row
    (board[1] == mark and board [4] == mark and board[7] == mark) or #column   
    (board[2] == mark and board [5] == mark and board[8] == mark) or #column
    (board[3] == mark and board [6] == mark and board[9] == mark) or #column
    (board[1] == mark and board [5] == mark and board[9] == mark) or #diagonal
    (board[3] == mark and board [5] == mark and board[7] == mark))  #diagonal

#step 6
'''
this function uses random module to select which player will go first 
'''
import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'player1'
    if flip == 1:
        return 'player2'

#step 7
'''
this function checks that a particular position is free or not 
'''
def space_check(board,position):
    return board[position] == " "
#step 8
'''
this function uses the sapce_check function to check weather the board is full
or not 
'''
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#step 9
'''
this function checks that the position enters by player is valid or not 
'''
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("enter the position: (1 ,9)"))
    return position
#step 10
'''
this function asks palyers that they want to play again or not after end of game 
'''
def replay():
    choice = input("play again Yes or No ")
    return choice == 'Yes'
