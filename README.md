
# battleships game

## introduction
this is a simple command-line battleships game where the player competes against an ai opponent. the player places ships on a board and takes turns attacking the ai's ships until one side wins.

---

## how to play

1. **setup the board**
   - when the game starts, you will be prompted to enter the size of the board (e.g., 10 for a 10x10 board).
   - if you enter an invalid size, the game will default to a 10x10 board.

2. **ship placement**
   - ships are placed on the board. the exact method of placement depends on the logic in `components.place_battleships()`.

3. **gameplay**
   - you will be asked to enter x and y coordinates to attack the ai's board.
   - if you hit a ship, you will see "hit!", and if you miss, you will see "miss!".
   - if you sink a ship, you will be notified (e.g., "you have sunk the battleship").
   - the ai will then take its turn, and you will be notified if it hits your ships.

4. **win condition**
   - you win if you sink all the ai's ships before it sinks yours.
   
---

## file structure

```
📁 battleships_game
  ├── components.py       # handles board, ship creation, and placement logic
  ├── game_engine.py     # handles player attack logic, ship sinking, and win conditions
  ├── mp_game_engine.py  # manages ai logic and ai move generation
  ├── main.py           # main entry point for the game
  ├── README.md         # instructions and information about the game (this file)
```

---

## requirements
- python 3.6 or higher

no additional libraries are required as the game runs on the command line.

---

## how to run
1. open a terminal or command prompt.
2. navigate to the folder where the game files are stored.
3. run the following command:

```
python main.py
```

---

## controls
- enter x and y coordinates (separated by input prompts) to attack the ai's board.

example:
```
please enter an x coordinate: 3
please enter a y coordinate: 5
```

---

## example gameplay
```
hello! welcome to the world of battleships!
please enter the size of the board: 10
it's your turn! enter your attack coordinates
please enter an x coordinate: 3
please enter a y coordinate: 5
hit!
you have sunk the patrol boat!
it's the ai's turn!
the ai hit your ship!
```

---

## key functions

### **attack(coordinates, board, battleships)**
- takes player coordinates and checks if it's a hit or miss.
- updates the board and tracks ship damage.
- returns true if a ship is sunk.

### **cli_coordinates_input()**
- prompts the player to enter attack coordinates.
- validates input to ensure it is numeric.

### **simple_game_loop()**
- main game loop where player and ai take turns attacking.
- tracks the win condition and announces the winner.

---

## known issues
- input validation only checks for numeric input, not board boundaries.
- ai moves may be predictable if `random` is not seeded properly.
- **faulty logic in main.py**:
  - the `process_attack` function does not return a response to the user, causing the game to crash or hang.
  - no logic to end the game when all ships are sunk, meaning the game could continue indefinitely.
  - player and ai boards are not properly updated, and the ai does not track player ship positions correctly.

---

## possible improvements
- improve the ai to make smarter moves (like targeting nearby coordinates after a hit).
- allow the player to manually place their ships.
- add a graphical user interface (gui) using tkinter or a web-based solution.
- add difficulty levels for the ai.
- fix the issues in `main.py` to ensure proper game logic, player interaction, and responses.

---

## credits
- developed by Muhammed Panjwani

---

## license
this game is released under the mit license. feel free to modify and share it.



