from chess.config import *
from chess.AI import MinMaxPlayer

BLACK = 'BLACK'
WHITE = 'WHITE'

# basic starting set up
SAMPLE_BOARD_1 = [[rookB, knightB, bishopB, queenB, kingB, bishopB, knightB, rookB],
                  [pawnB] * 8,
                  [empty] * 8,
                  [empty] * 8,
                  [empty] * 8,
                  [empty] * 8,
                  [pawnW] * 8,
                  [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]


engine = MinMaxPlayer()

move = engine.find_best_move(SAMPLE_BOARD_1, BLACK)
print(move)
