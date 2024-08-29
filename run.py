import random


ROWS = 6
COLUMNS = 6
INITIAL_AMMO = 10
INITIAL_SHIPS = 4


def get_username():
    """
    Get a username from the user to be used in the welcome
    message, and then return the username.
    """
    username = str(input("\nPlease enter your username: "))
    return username


def instructions():
    """
    Prints instructions for the game to the terminal, using the
    returned username value from the get_username function in the welcome
    message.
    """
    print(f"\nHello {get_username()}, welcome to Battleships!")

    print("\nYour objective is to find and destroy all the hidden ships on the map!\n")

    print(f"""\nHow To Play:
    \nYou have {INITIAL_AMMO} ammunitions and there are {INITIAL_SHIPS} hidden ships on the map.""")

    print("In order to hit them, you must guess the coordinates of their locations. For example:")

    print("For the first row and first column, you would guess row 1 and column 1.")

    print("Good luck!\n")


def create_random_ships():
    """
    Returns random numbers to be used for the rows and columns
    coordinates of the ships.
    """
    return random.randrange(ROWS), random.randrange(COLUMNS)


def play_game():
    """
    Creates the board for the game to be played on, and runs the
    game by asking the user to enter guesses for the ship's coordinates
    in the rows and columns.
    Raises an error message if the user doesn't input a number between 1 and 6.
    Tells the user after each guess whether they have hit or missed the ships,
    and updates the game board to show where they have hit or missed.
    Also lets the user know how many ammunitions they have left, and also how
    many ships remain left to hit.
    Adds 1 ammunition onto the user's remaining ammo whenever they get a hit.
    """
    game_board = [['.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.']]

    for i in game_board:
        print(*i)

    ship1 = create_random_ships()
    ship2 = create_random_ships()
    ship3 = create_random_ships()
    ship4 = create_random_ships()
    ships_left = 4
    ammo = 10

    while ammo:
        try:
            row = int(input(f"\nEnter a row number between 1 and {ROWS}: "))
            column = int(input(f"Enter a column number between 1 and {COLUMNS}: "))
        except ValueError:
            print("ERROR: You can only enter a number")
            continue

        if row not in range(1,7) or column not in range(1, 7):
            print("\nERROR: You must enter a number between 1 and 6")
            continue

        row = row - 1
        column = column - 1


        if game_board[row][column] == "-" or game_board[row][column] == "X":
            print("\nYou have already guessed this coordinate, try another one!\n")
            continue
        elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3 or (row, column) == ship4:
            print("\nHIT! 1 ship down, and you get 1 new ammo!\n")
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("All ships are destroyed, you win!")
        else:
            print("\nMISS!\n")
            game_board[row][column] = "-"
            ammo -= 1
        if ammo == 0 and ships_left > 0:
            print("You have run out of ammo, you lose!\n")


instructions()


play_game()