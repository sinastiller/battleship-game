"""
importing libaries
"""
import random
import sys
from time import sleep

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


def print_fast(word):
    """
    Prints output fast.
    """
    for character in word:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.02)


def print_slow(word):
    """
    Prints output slow.
    """
    for character in word:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.04)


def welcome_message():
    """
    Welcome message to user and instructions for the game.
    """
    print_slow("ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʙᴀᴛᴛʟᴇꜱʜɪᴘ ɢᴀᴍᴇ!\n\n")
    sleep(0.5)

    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'

    while True:
        name = input("\033[1mWhat is your name, Fighter? ")
        if all(char in characters for char in name) and len(name) >= 2:
            break
        print("That's not valid, please enter you name.\n")
        return name
    print_fast("\033[1m\nHere are just some quick rules "
               f"before we start the game, {name}: ")
    print_slow("\033[1m\n\nThe grid consists of 8 rows(A-H) and 8 columns(1-8)"
               ".\n")
    print_slow("\033[1m\nThere are 5 different ship types:\n")
    print_slow("\033[95m      Carrier - 5 in length\n")
    print_slow("\033[36m      Battleship - 4 in length\n")
    print_slow("\033[36m      Cruiser - 4 in length\n")
    print_slow("\033[94m      Submarine - 3 in length\n")
    print_slow("\033[93m      Destroyer - 2 in length\n")
    print_slow("\033[0m\033[1m\nThe computer chooses it's ships randomly.\n\n")
    print_slow(f"\033[1mYou, {name}, will be asked to place your ships, "
               "so choose carefully!\n\n")
    print_slow("\033[1mYou will then take turns trying to destroy each other's"
               " ships.\n\n")
    print_slow("\033[1mWhoever sinks the ships first wins!\n\n")
    sleep(1)
    print_fast(f"\033[1mGood Luck, {name}!\033[0m\n\n")
    sleep(1)


def create_board(board):
    """
    Creates the board with numbers for columns and letters for rows.
    """
    if board == USER_BOARD:
        print("\nPLAYER BOARD")
        print("-" * 17)
    elif board == COMP_BOARD_GUESS:
        print("\nCOMPUTER GUESSED")
        print("-" * 17)
    else:
        print("\nPLAYER GUESSED")
        print("-" * 17)
    print(" ", " ".join("12345678"))
    print("=" * 17)
    for letter, row in zip("ABCDEFGH", board):
        print(letter, " ".join(row))


def position_ships(board):
    """
    positioning the ships on board, randomly for computer and for user through
    manual input
    """
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
                                board[row][i] = "O"
                        else:
                            for i in range(row, row + length_of_ships):
                                board[i][column] = "O"
                        break
            # user's input to place ships
            else:
                position_ship = True
                print_slow("\nPosition your ship with the length of " +
                           str(length_of_ships))
                row, column, direction = input_user(position_ship)
                if ship_fits(length_of_ships, row, column, direction):
                    # Checks to see if ships do not cross over each other
                    if ships_cross(board, row, column, direction,
                                   length_of_ships):
                        print_fast("\nYou have already placed a ship here. "
                                   "Please place in empty field.\n")
                    # ships can be positioned
                    else:
                        if direction == "S":
                            for i in range(column, column + length_of_ships):
                                board[row][i] = "O"
                        elif direction == "D":
                            for i in range(row, row + length_of_ships):
                                board[i][column] = "O"
                        else:
                            break
                        create_board(USER_BOARD)
                        break
                else:
                    print_fast("\nPlease place ship within the grid.\n")


def ship_fits(length_of_ships, row, column, direction):
    """
    Checks to see if ships do not leave the grid
    """
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


def ships_cross(board, row, column, direction, length_of_ships):
    """
    Checks to see if ships do not cross over each other
    """
    if direction == "S":
        for i in range(column, column + length_of_ships):
            if board[row][i] == "O":
                return True
    else:
        for i in range(row, row + length_of_ships):
            if board[i][column] == "O":
                return True
    return False


def input_user(position_ship):
    """
    Asks user to place their ships on the grid
    """
    if position_ship is True:
        # direction positioning
        while True:
            try:
                direction = input("\n\033[1mWould you like to position your "
                                  "ship sideways or downwards?\nEnter the"
                                  " direction of the ship(S for sideways or D "
                                  "for downwards):\033[0m\n").upper()
                if direction == "S" or direction == "D":
                    break
                else:
                    raise KeyError
            except KeyError:
                print_fast("Please enter either S or D.\n")
        # row positioning
        while True:
            try:
                row = input("\n\033[1mWhich row would you like to place your "
                            "ship in?\nPlease enter a letter from A-H:"
                            "\033[0m\n").upper()
                if row in "ABCDEFGH":
                    row = GRID[row]
                    break
                else:
                    raise KeyError
            except KeyError:
                print_fast("Please enter a valid letter from A-H.\n")
        while True:
            try:
                column = input("\n\033[1mWhich column would you like to place "
                               "your ship in?\nPlease enter a number from 1-8:"
                               "\033[0m\n")
                if column in "12345678":
                    column = int(column) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print_fast("Please enter a valid number from 1-8.\n")
        return row, column, direction
    # guessing position of ship:
    else:
        while True:
            try:
                row = input("\033[1mGuess a row where the computer's ship "
                            "might be located?\nPlease enter a letter from "
                            "A-H:\033[0m\n").upper()
                if row in "ABCDEFGH":
                    row = GRID[row]
                    break
                else:
                    raise KeyError
            except KeyError:
                print_fast("Please enter a valid letter from A-H.\n")
        while True:
            try:
                column = input("\n\033[1mGuess a column where the computer's "
                               "ship might be located?\nPlease enter a number "
                               "from 1-8:\033[0m\n")
                if column in "12345678":
                    column = int(column) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print_fast("Please enter a valid number from 1-8.\n")
        return row, column


def hit_ships(board):
    """
    Counts how many ships were hit
    """
    if board == USER_BOARD:
        count = 0
        for row in board:
            for column in row:
                if column == "\033[91mX\033[0m":
                    count += 1
        return count
    else:
        count = 0
        for row in board:
            for column in row:
                if column == "\033[92mX\033[0m":
                    count += 1
        return count


def validate_guess(board):
    """
    checks if a ship was hit or missed and printed on player's and computer's
    board
    """
    if board == USER_BOARD_GUESS:
        # pylint: disable=unbalanced-tuple-unpacking
        row, column = input_user(USER_BOARD_GUESS)
        if board[row][column] == "|":
            validate_guess(board)
        elif board[row][column] == "O":
            validate_guess(board)
        elif COMP_BOARD[row][column] == "O":
            board[row][column] = "\033[92mX\033[0m"
            print_fast("\nYou got a \033[92mhit\033[0m!")
        else:
            board[row][column] = "|"
            print_fast("\nTry again. You missed!")
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "|":
            validate_guess(board)
        elif board[row][column] == "O":
            validate_guess(board)
        elif USER_BOARD[row][column] == "O":
            board[row][column] = "\033[91mX\033[0m"
            print_fast("\nOh no! The computer \033[91mhit\033[0m you!")
        else:
            board[row][column] = "|"
            print_fast("\nLucky, the Computer missed!")


def run_game():
    """
    Starts the game
    """
    start_game = input("\n\033[1mPlease type S to start the game:\033[0m"
                       " ").upper()
    while start_game != "S":
        start_game = input("Please type S to start the game: ").upper()

    position_ships(COMP_BOARD)
    create_board(USER_BOARD)
    position_ships(USER_BOARD)

    while True:
        # player's turn
        while True:
            print_fast("Now it's your turn.\n\n")
            validate_guess(USER_BOARD_GUESS)
            create_board(USER_BOARD_GUESS)
            break
        if hit_ships(USER_BOARD_GUESS) == 17:
            print_slow("Congratulations, you sank all the computer's ships and"
                       " won the game!\n")
            restart_game()
            break
            # computer's turn
        while True:
            validate_guess(COMP_BOARD_GUESS)
            create_board(COMP_BOARD_GUESS)
            break
        if hit_ships(COMP_BOARD_GUESS) == 17:
            print_slow("You lost. The Computer has destroyed all your ships"
                       " and won the battle!")
            restart_game()
            break


def restart_game():
    """
    Asks user if restart is desired.
    """
    restart = input("\n\033[1mWould you like to play again? Enter Y(yes)"
                    "or N(no):\033[0m ").upper()
    while True:
        if restart == "Y":
            print_slow("Please run program again.\n")
            break
        elif restart == "N":
            print.slow("Hope you enjoyed the game. See you next time!")
            break
        else:
            print("Please type Y or N.")
            break


welcome_message()
run_game()
