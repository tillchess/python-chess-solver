"""
Chess Solver

A python script that can analyze games in the pgn file with any UCI chess engine,
annotate games and positions.

 Set MAX_PLY,ANALYSE_FROM_START_POSITION and ENGINE_PATH in the code to your personal setting

 USAGE:
 phyton3 solver.py game.pgn output.pgn

Requires modules: phyton-chess 1.999 or newer
          chess 1.5.0 or newer
"""


__author__ = 'tillchess'
__script_name__ = 'Chess Solver'

import chess
import chess.engine
import chess.pgn
import sys


# Constants

MAX_TIME_SEC = 1
MAX_PLY = 2
ENGINE_PATH="./sf13" 
ANALYSE_FROM_START_POSITION=False

        
def solve_game(game, fromEnd,maxPly):
     #Go to the end of the game and create a chess.Board() from it:
    if fromEnd:
        game = game.end()
         
    board = game.board()

    node=game

    ply=1  
    
    while not board.is_game_over():
     result = engine.play(board, chess.engine.Limit(time=MAX_TIME_SEC),ponder=False)
     board.push(result.move)
     node = node.add_variation(result.move) # Add game node
     if ply>maxPly: 
         break;
     ply+=1
 
    return node.root()
    
##########

arguments = sys.argv
pgnfilename = str(arguments[1])
pgnfilename_out = str(arguments[2])

engine = chess.engine.SimpleEngine.popen_uci(ENGINE_PATH) #give correct address of your engine here
engine.configure({"Threads": 4, "Hash": 128})
counter=1
#Read pgn file:
with open(pgnfilename) as pgn:
    #go thru games
   for game in iter(lambda: chess.pgn.read_game(pgn), None):
       print("Analysing game no. ",counter)
       counter+=1
       final_game=solve_game(game,ANALYSE_FROM_START_POSITION,MAX_PLY)
       with open(pgnfilename_out, 'a+') as f:
            f.write(str(final_game)+ "\n\n")
    
engine.quit()
    
    


