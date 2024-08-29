ROWS = 6
COLUMNS = 6
INITIAL_AMMO = 10
INITIAL_SHIPS = 4


def get_username():
    username = str(input("\nPlease enter your username: "))
    return username


def instructions():
    print(f"\nHello {get_username()}, welcome to Battleships!")

    print("\nYour objective is to find and destroy all the hidden ships on the map!\n")

    print(f"""\nHow To Play:
    \nYou have {INITIAL_AMMO} ammunitions and there are {INITIAL_SHIPS} hidden ships on the map.""")

    print("In order to hit them, you must guess the coordinates of their locations. For example:")

    print("For the first row and first column, you would guess row 1 and column 1.")

    print("Good luck!\n")