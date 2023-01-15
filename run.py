"""
importing the random function
"""
import random

# declaring of constant variables
# declares the different lengths of the five ships
SHIPS = [2, 3, 3, 4, 5]
# Declares two empty game boards
USER_BOARD = [["-"] * 8 for i in range(8)]
COMP_BOARD = [["-"] * 8 for i in range(8)]
# declares two boards for the guesses of the user and the computer
USER_BOARD_GUESS = [["-"] * 8 for i in range(8)]
COMP_BOARD_GUESS = [["-"] * 8 for i in range(8)]
# converting letter to numbers for the grid
GRID = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


# creating the board with numbers for columns and letters for rows
def create_board(board):
    if board == COMP_BOARD:
        print("COMPUTER BOARD")
    else:
        print("USER BOARD")
    print(" ", " ".join("12345678"))
    print(" ================")
    for letter, row in zip("ABCDEFGH", board):
        print(letter, " ".join(row))


# positioning the ships on board, randomly for computer and for user through
# manual input
def position_ships(board):
    # looping through the different ship types
    for length_of_ships in SHIPS:
        # while looping,ships can not lay over each other
        while True:
            if board == COMP_BOARD:
                direction = random.choice(["S", "D"])
                row = random.randint(0, 7)
                column = random.randint(0, 7)
                # Checks to see if ships do not leave the grid
                if ship_fits(length_of_ships, row, column, direction):
                    # Checks to see if ships do not cross over each other
                    if not ships_cross(board, row, column, direction,
                                       length_of_ships):
                        # place ship
                        if direction == "S":
                            for i in range(column, column + length_of_ships):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + length_of_ships):
                                board[i][column] = "X"
                        break
            # user's input to place ships
            else:
                position_ship = True
                print("Position your ship with the length of " +
                      str(length_of_ships))
                row, column, direction = input_user(position_ship)
                if ship_fits(length_of_ships, row, column, direction):
                    # Checks to see if ships do not cross over each other
                    if not ships_cross(board, row, column, direction,
                                       length_of_ships):
                        # ships can be positioned
                        if direction == "S":
                            for i in range(column, column + length_of_ships):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + length_of_ships):
                                board[i][column] = "X"
                        create_board(USER_BOARD)
                        break

                    # check if ship fits in board


# Checks to see if ships do not leave the grid
def ship_fits(length_of_ships, row, column, direction):
    if direction == "S":
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
def ships_cross(board, row, column, direction, length_of_ships):
    if direction == "S":
        for i in range(column, column + length_of_ships):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + length_of_ships):
            if board[i][column] == "X":
                return True
    return False


# Asks user to place their ships on the grid
def input_user(position_ship):
    if position_ship is True:
        # direction positioning
        while True:
            try:
                direction = input("Would you like to position your ship "
                                  "sideways or downwards? Please enter the "
                                  "direction of the ship(S for sideways or D "
                                  "for downwards):\n ").upper()
                if direction == "S" or direction == "D":
                    break
            except ValueError:
                print("Please enter either S or D.\n")
        # row positioning
        while True:
            try:
                row = input("Which row would you like to place your ship in? "
                            "Please enter a letter from A-H:\n").upper()
                if row in "ABCDEFGH":
                    row = GRID[row]
                    break
            except KeyError:
                print("Please enter a valid letter from A-H.\n")
        while True:
            try:
                column = input("Which column would you like to place your ship"
                               " in? Please enter a number from 1-8:\n")
                if column in "12345678":
                    column = int(column) - 1
                    break
            except ValueError:
                print("Please enter a valid number from 1-8.\n")
        return row, column, direction
    # guessing position of ship:
    else:
        while True:
            try:
                row = str(input("Guess a row where the computer's ship might"
                                "be located? Please enter a letter from "
                                "A-H:\n")).upper()
                if row in "ABCDEFGH":
                    row = GRID[row]
                    break
            except ValueError:
                print("Please enter a valid letter from A-H.\n")
        while True:
            try:
                column = input("Guess a column where the computer's ship might"
                               " be located? Please enter a number from "
                               "1-8:\n")
                if column in "12345678":
                    column = int(column) - 1
                    break
            except ValueError:
                print("Please enter a valid number from 1-8.\n")
        return row, column


# counts how many ships were hit
def hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


# checks if a ship was hit or missed and printed on player's and computer's
# board
def validate_guess(board):
    if board == USER_BOARD_GUESS:
        row, column = input_user(USER_BOARD_GUESS)
        if board[row][column] == "|":
            validate_guess(board)
        elif board[row][column] == "X":
            validate_guess(board)
        elif COMP_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "|"
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "|":
            validate_guess(board)
        elif board[row][column] == "X":
            validate_guess(board)
        elif USER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "|"


position_ships(COMP_BOARD)
create_board(COMP_BOARD)
create_board(USER_BOARD)
position_ships(USER_BOARD)

while True:
    # player's turn
    while True:
        print("It's your turn. Try and guess to see where the battleships of"
              " the computer are located.")
        create_board(USER_BOARD_GUESS)
        validate_guess(USER_BOARD_GUESS)
        break
    if hit_ships(USER_BOARD_GUESS) == 17:
        print("Congratulations, you sank all the computer's ships and won the "
              "game!")
        break
        # computer's turn
    while True:
        validate_guess(COMP_BOARD_GUESS)
        break
    create_board(COMP_BOARD_GUESS)
    if hit_ships(COMP_BOARD_GUESS) == 17:
        print("You lost. The Computer has guessed all your ships and won the "
              "battle!")
        break
