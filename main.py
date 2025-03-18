from flask import Flask, render_template, jsonify, request
import components  # handles board, ship setup, and placement logic
import mp_game_engine  # handles ai logic and ai moves
import game_engine  # handles player attack logic and win conditions

# create the flask app
game = Flask(__name__)

# global variables to store the game state
player_boards = {}  # stores the player board for the game
board_sizes = {}  # stores the board size for the game
played_coordinates = {}  # stores the ai's played coordinates

# route for handling ship placement (get and post)
@game.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    global player_boards, board_sizes
    
    # welcome message
    print("hello! welcome to the world of battleships!")
    
    try:
        # get board size from the user
        board_size = int(input("please enter the size of the board: "))
        if board_size <= 0:
            raise ValueError("board size must be greater than 0.")
    except ValueError:
        # use default board size if input is invalid
        print("invalid input. using default board size of 10.")
        board_size = 10
    
    if request.method == 'GET':
        # store the board size
        board_sizes['game'] = board_size
        
        # get ship configurations from the components module
        ships = components.create_battleships()
        
        # render the placement screen
        return render_template('placement.html', ships=ships, board_size=board_size)

    if request.method == 'POST':
        # handle the ship placement data from the post request
        data = request.get_json()
        print(f"received ship placements: {data}")

        # get the board size from stored board sizes
        board_size = board_sizes.get('game', 10)

        # initialize the player's board and place the ships on it
        player_board = components.initialise_board(board_size)
        player_board = components.place_battleships(player_board, data, 'custom')

        # store the player's board in the global dictionary
        player_boards['game'] = player_board
        
        # respond with a success message
        return jsonify({'message': 'board setup successful'}), 400


# route for the main game screen
@game.route('/', methods=['GET'])
def root():
    global player_boards
    
    # get the player's board
    player_board = player_boards.get('game', [])
    
    # render the main game screen with the player's board
    return render_template('main.html', player_board=player_board)


# route for handling attacks
@game.route('/attack', methods=['GET'])
def process_attack():
    global player_boards, played_coordinates
    
    # get the attack coordinates from the request
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    coordinates = (x, y)
    
    # get the player's board and board size
    player_board = player_boards.get('game', [])
    board_size = board_sizes.get('game', 10)
    
    # handle the player's attack
    hit = game_engine.attack(coordinates, player_board, components.create_battleships())
    
    # generate the ai's attack
    if 'game' not in played_coordinates:
        played_coordinates['game'] = set()
    ai_coordinates = mp_game_engine.generate_attack(player_board, played_coordinates['game'])
    played_coordinates['game'].add(ai_coordinates)
    
    # store the player's updated board
    player_boards['game'] = player_board


# run the flask app
if __name__ == "__main__":
    game.run(debug=True)





