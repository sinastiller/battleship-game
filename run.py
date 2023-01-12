"""
Importing the randint function from the random module
"""
import random

# Declaring of Constant Variables
# Declares the different lengths of the five ships
SHIPS = [2, 3, 3, 4, 5]
# Declares two empty game boards
USER_BOARD = [["-"] * 8 for x in range(8)]
COMP_BOARD = [["-"] * 8 for x in range(8)]
# Declares two boards for the guesses of the user and the computer
USER_BOARD_GUESS = [["-"] * 8 for x in range(8)]
COMP_BOARD_GUESS = [["-"] * 8 for x in range(8)]
# Converting letter to numbers for the grid
GRID = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

# Creating the board with numbers for columns and letters for rows


def create_board(board):
    print(" ", " ".join("12345678"))
    print(" ================")
    for letter, row in zip("ABCDEFGH", board):
        print(letter, " ".join(row))

# Positioning the ships on board, randomly for computer and for user through input


def position_ships(board):
    # looping through the different ship types
    for length_of_ships in SHIPS:
        # while looping,ships can not lay over each other
        while True:
            if board == COMP_BOARD:
                direction = random.choice(["Horizontal", "Vertical"])
                row = random.randint(0, 7)
                column = random.randint(0, 7)
                # Checking to see if ships do not leave the size of the grid
                if ship_fits(length_of_ships, direction, row, column):

# Checks to see if ships do not leave the grid


def ship_fits(length_of_ships, direction, row, column):
    if direction == "Horizontal":
        if column + length_of_ships > 8:
            return False
        else:
            return True
    else:
        if row + length_of_ships > 8:
            return False
        else:
            return True

# Checks to see if ships do not cross over each other


def ships_cross(length_of_ships, direction, row, column, board):
    if direction == "horizontal":
        for x in range(column, column + length_of_ships):
            if board[row][x] == "O":
                return True
    else:
        for x in range(row, row + length_of_ships):
            if board[column][x] == "O":
                return True
    return False