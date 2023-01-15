| FEATURE | EXPECTED OUTCOME| ACTION | RESULT |
| -------------              | -------------                                | ------------- | ------------- |
| Print(LENGTH_OF_SHIPS) | Prints List including numbers | print into terminal | prints: [2, 3, 3, 4, 5] |
| Print(USER_BOARD) | Prints List containg eight Lists including eight "-"   | print into terminal | prints: [['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-']]|
| print(GRID) | Prints dictionary including key(letters): value(numbers) pairs | print to terminal | prints: {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}|
| create_board(COMP_BOARD)| Prints computer board containing the rows(with letters) and columns(with numbers) | Print to terminal | Prints empty board to terminal |


- Traceback (most recent call last):
    File "C:\Users\Sina\PycharmProjects\BattleShip\main.py", line 190, in <module>
      position_ships(USER_BOARD)
    File "C:\Users\Sina\PycharmProjects\BattleShip\main.py", line 56, in position_ships
      if not ships_cross(board, length_of_ships, direction, row, column):
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\Sina\PycharmProjects\BattleShip\main.py", line 91, in ships_cross
      for i in range(row, row, length_of_ships):
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  TypeError: 'list' object cannot be interpreted as an integer


- fixing input_user() by checking if position_ship() is TRUE
- fixing Type/Key Errors by adding an else-satement to raise error
