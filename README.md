# chess-solver

## About

I needed a tool where I can analyse a batch of PGN games even, with positons only ,
and run Stockfish or any other UCI engine and give me the solution of the mating or 
best move problem. Then I could feed it to any Chess GUI and play thru with hidden moves easily.

 Set MAX_PLY,ANALYSE_FROM_START_POSITION and ENGINE_PATH in the code to your personal setting

## Installation

Requires modules: 
		phyton-chess 1.999 or newer
          chess 1.5.0 or newer
A UCI chess engine of your choice!

Is recommended that you use Python 3 and pip3. 

### Install requirements

`pip3 install -r requirements.txt --user`



## Launching Application
phyton3 solver.py game.pgn output.pgn