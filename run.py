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

# Positioning the ships on board, randomly for computer and for user through
# input


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
                    # Checks to see if ships do not cross over each other
                    if not ships_cross(length_of_ships, direction, row, column, board):
                        # ships can be positioned
                        if direction == "horizontal":
                            for x in range(column, column + length_of_ships):
                                board[row][x] = "O"
                        else:
                            for x in range(row, row + length_of_ships):
                                board[column][x] = "O"
                        break
            # user's input to place ships
            else:
                position_ship = True
                print("Position your ship with the length of " + str(length_of_ships))
                column, row, direction = input_user(position_ship)
                if ship_fits(length_of_ships, direction, row, column):
                    # Checks to see if ships do not cross over each other
                    if not ships_cross(length_of_ships, direction, row, column, board):
                        # ships can be positioned
                        if direction == "horizontal":
                            for x in range(column, column + length_of_ships):
                                board[row][x] = "O"
                        else:
                            for x in range(row, row + length_of_ships):
                                board[column][x] = "O"
                        break

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

# Asks user to place their ships on the grid


def input_user(position_ship):
    if position_ship is True:
        # direction positioning
        while True:
            try:
                direction = input("Would you like to position your ship horizontal or vertical? Please enter the "
                                  "direction of the ship(horizontal or vertical):\n ").lower()
                if direction == "horizontal" or direction == "vertical":
                    break
            except TypeError:
                print("Please enter either horizontal or vertical.\n")
        # column positioning
        while True:
            try:
                column = input("Which column would you like to place your ship in? Please enter a number from 1-8:\n")
                if column in "12345678":
                    column = int(column) - 1
                    break
            except ValueError:
                print("Please enter a valid number from 1-8.\n")
        # row positioning
        while True:
            try:
                row = input("Which row would you like to place your ship in? Please enter a letter from A-H:\n").upper()
                if row in "ABCDEFGH":
                    row = GRID[row]
                    break
            except KeyError:
                print("Please enter a valid letter from A-H.\n")
            return direction, column, row
        # guessing position of ship:
        while True:
            try:
                column = input("Guess a column where the computer's ship might be located? Please enter a number from "
                               "1-8:\n")
                if column in "12345678":
                    column = int(column) - 1
                    break
            except ValueError:
                print("Please enter a valid number from 1-8.\n")
        while True:
            try:
                row = input("Guess a row where the computer's ship might be located? Please enter a letter from A-H:\n").upper()
                if row in "ABCDEFGH":
                    row = GRID[row]
                    break
            except KeyError:
                print("Please enter a valid letter from A-H.\n")
            return column, row
