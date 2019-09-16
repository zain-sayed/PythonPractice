from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('----------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('----------')
    print(board[1]+' | '+board[2]+' | '+board[3])

def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input("Player 1, choose 'X or 'O ")
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position]=marker
    
def win_check(board, mark):
    if (board[1]==mark and board[2]==mark and board[3]==mark) or (board[4]==mark and board[5]==mark and board[6]==mark) or (board[7]==mark and board[8]==mark and board[9]==mark):
        return True
    elif (board[7]==mark and board[4]==mark and board[1]==mark) or (board[8]==mark and board[5]==mark and board[2]==mark) or (board[9]==mark and board[6]==mark and board[3]==mark):
        return True
    elif (board[7]==mark and board[5]==mark and board[3]==mark) or (board[1]==mark and board[5]==mark and board[9]==mark):
        return True
    else:
        return False
    
import random

def choose_first():
    x = random.randint(1,2)
    if x==1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    print(position)
    if board[position]=='X' or board[position]=='O':
        return False
    else:
        return True

def full_board_check(board):
    if ' ' in board:
        return False
    else:
        return True
    
def player_choice(board):
    position=int(input("Enter Position: "))
    if space_check(board,position):
        return position

def replay():
    
    choice= input('Enter yes or no: ')
    if choice=='yes':
        return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    Board = [' '] * 10
    player1, player2 = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(Board)
            position = player_choice(Board)
            place_marker(Board, player1, position)

            if win_check(Board, player1):
                display_board(Board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(Board)
            position = player_choice(Board)
            place_marker(Board, player2, position)

            if win_check(Board, player2):
                display_board(Board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
        