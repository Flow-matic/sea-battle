from random import randint

game_board = []

player_one = {
    "name": "player 1",
    "wins": 0,
}

player_two = {
    "name": "player 2",
    "wins": 0,
}

colors = {
    "reset": "\033[00m",
    "red": "\003[91m",
    "blue": "\003[94m",
    "cyan": "\003[96m",
}


#Building the 5 x 5 board
def build_game_board(board):
    for item in range(5):
        board.append(["0"] * 5)


def show_board(board):
    for row in board:
        print(" ".join(row))


# Defining ships locations
def load_game(board):
    print("WELCOME TO BATTLESHIP!")
    print("find and sink the ship!")
    del board[:]
    build_game_board(board)
    print(colors['blue'])
    show_board(board)
    print(colors['reset'])
    ship_col = randint(1, len(board))
    ship_col = randint(1, len(board[0]))
    return {
        'ship_col': ship_col,
        'ship_row': ship_row,
    }

ship_points = load_game(game_board)


# Players will alternate turns
def player_turns(total_turns):

    if total_turns % 2 == 0:
        total_turns += 1
        return player_one
    
    return player_two


# Allows new game to start
def play_again():

    positive = ["yes", "y"]
    negative = ["no", "n"]

    global ship_points

    

