import random
import json


#function to initialise the board making a an empty matrix of whatever size is passed
def initialise_board(size=10):
    return [[None] * size for _ in range(size)]


#creating the battleships dictionary
def create_battleships(filename="battleships.txt"):
    battleships = {}
    with open(filename, "r") as file:
        lines = file.readlines()
        #reading the file and splitting the lines to add to the dictionary
        for line in lines:
            ship_type, ship_size = line.strip().split(':')
            battleships[ship_type.strip()] = int(ship_size.strip())
    return battleships


#function for placing the battleships gets the board what ships and how to place them
def place_battleships(board, ships={}, placement='simple'):
    #simple placement is the ships being placed in the next available space
    if placement == 'simple':
        row, column = 0, 0
        for ship_type, ship_size in ships.items():
            if column + ship_size > len(board[0]):
                row += 1
                column = 0
            if row >= len(board):
                print("Cannot place", ship_type, "; board is too small.")
                continue
            for i in range(ship_size):
                board[row][column + i] = ship_type
            column += ship_size
        return board
#ships are randomly placed
    elif placement == 'random':
        for ship_type, ship_size in ships.items():
            is_placed = False
            while not is_placed:
                #randomly selects an orientation
                orientation = random.choice(['h', 'v'])
                #horizontal placement
                if orientation == 'h': 
                    row = random.randint(0, len(board) - 1)
                    column = random.randint(0, len(board[row]) - ship_size)
                    if all(column + i < len(board[row]) and board[row][column + i] is None for i in range(ship_size)):#checks if there is space
                        for i in range(ship_size):
                            board[row][column + i] = ship_type
                        is_placed = True
                #vertical placement
                elif orientation == 'v': 
                    row = random.randint(0, len(board) - ship_size)
                    column = random.randint(0, len(board[row]) - 1)
                    if all(row + i < len(board) and board[row + i][column] is None for i in range(ship_size)):
                        for i in range(ship_size):
                            board[row + i][column] = ship_type
                        is_placed = True
        return board
#custom placement from a json file that puts the file in a dictioanry and reads the values for what placement to do
    elif placement == 'custom':
        try:
            with open('placement.json', 'r') as file:
                custom_data = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print("Error loading custom placement file: ", e)
            return board

        for ship_type, custom_placements in custom_data.items():
            row = int(custom_placements[0])
            column = int(custom_placements[1])
            orientation = custom_placements[2]
            ship_size = ships.get(ship_type, 0)
            if orientation == 'h':
                if row < len(board) and column + ship_size <= len(board[row]):
                    if all(board[row][column + i] is None for i in range(ship_size)):
                        for i in range(ship_size):
                            board[row][column + i] = ship_type
            elif orientation == 'v':
                if row + ship_size <= len(board) and column < len(board[row]):
                    if all(board[row + i][column] is None for i in range(ship_size)):
                        for i in range(ship_size):
                            board[row + i][column] = ship_type
        return board















        





    


