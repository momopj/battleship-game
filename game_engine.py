import components

# handles the player's attack on the board
def attack(coordinates, board, battleships):
    row, column = coordinates
    
    # check if coordinates are outside the board
    if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]):
        print("invalid coordinates! outside of the board.")
        return False
    
    # check if the coordinate hits a ship or misses
    ship_type = board[row][column]
    if ship_type is None:
        print("miss!")
        return False
    else:
        print("hit!")
        board[row][column] = None  # mark the hit on the board
        battleships[ship_type] -= 1  # reduce the health of the hit ship
        
        # check if the ship is sunk
        if battleships[ship_type] == 0:
            print("you have sunk the", ship_type)
            return True

# gets user input for attack coordinates
def cli_coordinates_input():
    try:
        x_cor = int(input("please enter an x coordinate: "))
        y_cor = int(input("please enter a y coordinate: "))
        return x_cor, y_cor
    except ValueError:
        print("invalid input! please enter numeric coordinates.")
        return cli_coordinates_input()

# main game loop for battleships
def simple_game_loop():
    print("hello! welcome to the world of battleships!")
    
    # get the board size from the player
    try:
        board_size = int(input("please enter the size of the board: "))
        if board_size <= 0:
            raise ValueError("board size must be greater than 0.")
    except ValueError:
        print("invalid input. using default board size of 10.")
        board_size = 10
    
    # create ships, initialize the board, and place ships
    ships = components.create_battleships()
    board = components.initialise_board(board_size)
    default_board = components.place_battleships(board, ships)
    
    game_won = False
    ships_sunk = 0
    
    # loop until all ships are sunk
    while not game_won:
        if attack(cli_coordinates_input(), default_board, ships):
            ships_sunk += 1
            if ships_sunk == len(ships):  # check if all ships are sunk
                game_won = True
    
    print("congratulations! you have won the game!")

# entry point for the program
if __name__ == "__main__":
    simple_game_loop()



