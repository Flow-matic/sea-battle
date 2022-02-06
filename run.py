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

