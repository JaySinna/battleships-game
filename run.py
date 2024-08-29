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


def create_random_ship():
    return random.randrange(ROWS), random.randrange(COLUMNS)


def play_game():
    game_board = [['.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.']]

    for i in game_board:
        print(*i)


instructions()


play_game()