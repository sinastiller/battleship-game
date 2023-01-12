"""
Importing the randint function from the random module
"""
# import random

# Declaring of Constant Variables
# Declares the different lengths of the five ships
LENGTH_OF_SHIPS = [2, 3, 3, 4, 5]
# Declares two empty game boards
USER_BOARD = [["-"] * 8 for i in range(8)]
COMP_BOARD = [["-"] * 8 for i in range(8)]
# Declares two boards for the guesses of the user and the computer
USER_BOARD_GUESS = [["-"] * 8 for i in range(8)]
COMP_BOARD_GUESS = [["-"] * 8 for i in range(8)]
# Converting letter to numbers for the grid
GRID = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

# Printing the board function


def create_board(board):
    print(" ", " ".join("12345678"))
    for letter, row in zip("ABCDEFGH", board):
        print(letter, " ".join(row))


create_board(COMP_BOARD)
