from enum import Enum

# constants
MAX_ROWS = 8
MAX_COLS = 8

MOVE = 'MOVE'
ATTACK = 'ATTACK'

pawnW = 'PAWN_WHITE'
pawnB = 'PAWN_BLACK'

rookW = 'ROOK_WHITE'
rookB = 'ROOK_BLACK'

knightW = 'KNIGHT_WHITE'
knightB = 'KNIGHT_BLACK'

bishopW = 'BISHOP_WHITE'
bishopB = 'BISHOP_BLACK'

kingW = 'KING_WHITE'
kingB = 'KING_BLACK'

queenW = 'QUEEN_WHITE'
queenB = 'QUEEN_BLACK'

empty = 'EMPTY'

# all bit assets_deprecated for the board
assets = {
    pawnW: './assets/pawnw.png',
    pawnB: './assets/pawnb.png',

    rookW: './assets/rookw.png',
    rookB: './assets/rookb.png',

    knightW: './assets/knightw.png',
    knightB: './assets/knightb.png',

    bishopW: './assets/bishopw.png',
    bishopB: './assets/bishopb.png',

    kingW: './assets/kingw.png',
    kingB: './assets/kingb.png',

    queenW: './assets/queenw.png',
    queenB: './assets/queenb.png',

    empty: './assets/blank.png'
}

# Point values of pieces
PAWN = 10
KNIGHT = 30
BISHOP = 30
ROOK = 50
QUEEN = 90
KING = 900


NEG_INF = float("-inf")
