import components
import game_engine
import random
import json

players = {}
#generating a random ai attack
def generate_attack(board, played_coordinates):
    size = len(board)
    possible_coordinates = {(row, column) for row in range(size) for column in range(size)}#a store of all the coordinates that can be hit
    if played_coordinates == possible_coordinates:#checking if all the coordinates have been used
        raise RuntimeError("All the possible coordinates have been hit")
    while True:
        #random coordinate selection thats within the matrix
        row = random.randint(0, size - 1)
        column = random.randint(0, size - 1)
        if (row, column) not in played_coordinates:
            played_coordinates.add((row, column))#adding to the used coordinates store for comparison to check 
            return (row, column)
        
def ai_component_game_loop():
    print("Hello! Welcome to Battleships!")
    
    try:
        # getthe board size from the user
        board_size = int(input("Please enter the size of the board: "))
        if board_size <= 0:
            raise ValueError("Board size must be greater than 0.")
    except ValueError:
        #sets default to 10
        print("Invalid input. Using default board size of 10.")
        board_size = 10
    
    board = components.initialise_board(board_size)
    battleships = components.create_battleships()
    
    try:
        #places battleships with custom
        user_placements = components.place_battleships(board, battleships, 'custom')
        #errors if the file isnt found or is placed incorrectly
    except FileNotFoundError:
        print("Error: 'placement.json' file not found.")
        return None
    except json.JSONDecodeError as e:
        print("Error: 'placement.json' file is not properly formatted.", e)
        return None
    
    # placing ships
    ai_placements = components.place_battleships(board, battleships, 'random')
    
    #storing user and ai data
    players['User'] = {'board': user_placements, 'battleships': components.create_battleships()}
    players['AI'] = {'board': ai_placements, 'battleships': components.create_battleships()}

    # Set of coordinates that have been played
    played_coordinates = set()
    game_over = False
    
    # Track the number of ships sunk for both players
    ships_sunk_user = 0
    ships_sunk_ai = 0
    
    while not game_over:
        # User's turn to attack
        print("It's your turn! Enter your attack coordinates")
        coordinates = game_engine.cli_coordinates_input()
        
        # Check if the user's attack hits an AI ship
        if game_engine.attack(coordinates, players['AI']['board'], players['AI']['battleships']):
            print("You hit a ship!")
            ships_sunk_user += 1
            # If all AI ships are sunk the user wins
            if ships_sunk_user == len(players['AI']['battleships']):
                print("You won!")
                game_over = True

        if game_over:
            break

        # AI's turn to attack
        print("It's the AI's turn!")
        ai_coordinates = generate_attack(players['User']['board'], played_coordinates)
        
        # Check if the AI's attack hits a user ship
        if game_engine.attack(ai_coordinates, players['User']['board'], players['User']['battleships']):
            print("The AI hit your ship!")
            ships_sunk_ai += 1
            # If all user ships are sunk the AI wins
            if ships_sunk_ai == len(players['User']['battleships']):
                print("The AI has won!")
                game_over = True

# Run the game loop
if __name__ == "__main__":
    ai_component_game_loop()

    
    
    

    

            