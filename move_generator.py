# builds all functions for game logic, such as moves for each piece
from chess.config import *


def gen_moves(board: list, loc: tuple) -> list:
    """
    given a piece from the board, generate a list of possible moves.

    :param board: current state of game
    :param loc: the location of the piece, should be a tuple
    :return: a list of the possible moves as (x, y) locations on board
    """

    moves = []
    row, col = loc
    piece = board[row][col]

    if piece == pawnW or piece == pawnB:

        __gen_moves_pawn(moves, loc, board)
        # special function due to diagonal attacks
        __gen_attacks_pawn(moves, loc, board)

    elif piece == rookW or piece == rookB:

        __gen_moves_rook(moves, loc, board)

    elif piece == knightW or piece == knightB:

        __gen_moves_knight(moves, loc, board)

    elif piece == bishopW or piece == bishopB:

        __gen_moves_bishop(moves, loc, board)

    elif piece == queenW or piece == queenB:

        __gen_moves_queen(moves, loc, board)

    elif piece == kingW or piece == kingB:

        __gen_moves_king(moves, loc, board)

    return moves


def __gen_moves_king(moves, loc, board):
    """
    generate all possible moves for king

    :param moves:
    :param loc:
    :param board:
    :return:
    """

    # TODO needs check for nearby kings (cannot attack a king)
    row, col = loc
    piece = board[row][col]

    possible = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    for move in possible:
        if bounded(move):
            if not occupied(move, board):
                moves.append((*move, MOVE))
            else:
                if opposing(piece, move, board):
                    moves.append((*move, ATTACK))


def __gen_moves_queen(moves, loc, board):
    """
    generate possible moves for queen

    :param moves: list of moves
    :param loc: starting location
    :param board: current state of game
    :return: None
    """

    __gen_moves_rook(moves, loc, board)
    __gen_moves_bishop(moves, loc, board)
    __gen_moves_king(moves, loc, board)

    # remove duplicates from moves
    no_dupes = list(set(moves))
    moves.clear()
    moves.extend(no_dupes)


def __gen_moves_bishop(moves, loc, board):
    """
    generate possible moves for bishop

    :param moves: list of moves
    :param loc: starting location
    :param board: state of game
    :return: None
    """
    directions = [lambda r, c, i: (r - i, c - i),
                  lambda r, c, i: (r - i, c + i),
                  lambda r, c, i: (r + i, c - i),
                  lambda r, c, i: (r + i, c + i)]

    row, col = loc
    piece = board[row][col]
    for direction in directions:

        i = 1
        move = direction(row, col, i)
        while bounded(move):
            if not occupied(move, board):
                moves.append((*move, MOVE))
            else:
                if opposing(piece, move, board):
                    moves.append((*move, ATTACK))
                break

            # UPDATE
            i = i + 1
            move = direction(row, col, i)


def __gen_moves_knight(moves, loc, board):
    """
    generate all moves and attacks for the knight which
    follow the given T pattern, 8 possible moves

    :param moves: current move list
    :param loc:  current location of knight
    :param board: the state of the board
    :return: None
    """
    row, col = loc
    piece = board[row][col]

    possible = [(row + 2, col - 1), (row + 2, col + 1),
                (row - 2, col - 1), (row - 2, col + 1),
                (row - 1, col - 2), (row + 1, col + 2),
                (row - 1, col + 2), (row + 1, col - 2)]

    for move in possible:
        if bounded(move):

            if not occupied(move, board):
                moves.append((*move, MOVE))
            else:
                if opposing(piece, move, board):
                    moves.append((*move, ATTACK))
                # else same team, cannot attack

    # DONE


def __gen_moves_pawn(moves, loc, board):
    """
    generate moves for pawn

    :param moves: list of moves to be added to
    :param loc: starting location of pawn
    :param board: state of game
    :return: None
    """
    row, col = loc
    piece = board[row][col]

    # is starting, two moves possible
    # special: pawn takes diagonally, need board
    if piece == pawnW:

        up = (row - 1, col)
        if bounded(up) and not occupied(up, board):
            moves.append((*up, MOVE))

        if row == 6:
            up = (row - 2, col)
            if bounded(up) and not occupied(up, board):
                moves.append((*up, MOVE))

    # else we have a black pawn, moving down the board
    else:
        down = (row + 1, col)
        if bounded(down) and not occupied(down, board):
            moves.append((*down, MOVE))

        if row == 1:
            down = (row + 2, col)
            if bounded(down) and not occupied(down, board):
                moves.append((*down, MOVE))


def __gen_moves_rook(moves, loc, board):
    """
    generate all possible moves and attacks
    for the rook

    :param moves: list to be modified
    :param loc: starting location of piece
    :param board: state of game
    :return: None
    """
    row, col = loc
    piece = board[row][col]

    directions = [lambda r, c, i: (r + i, c),
                  lambda r, c, i: (r - i, c),
                  lambda r, c, i: (r, c + i),
                  lambda r, c, i: (r, c - i)]

    for direction in directions:

        i = 1
        move = direction(row, col, i)
        while bounded(move):

            if not occupied(move, board):
                moves.append((*move, MOVE))
            else:
                if opposing(piece, move, board):
                    moves.append((*move, ATTACK))
                # hit a 'wall', stop searching this path
                break

            # UPDATE
            i = i + 1
            move = direction(row, col, i)


def __gen_attacks_pawn(moves, loc, board):
    """
    generate all attacks for a pawn at loc,
    if possible, add to current moves

    :param board: state of game
    :param loc: starting location of piece
    :param moves: moves to add to
    :return: None
    """
    row, col = loc
    piece = board[row][col]

    # white pawn
    if piece == pawnW:
        left_move = (row - 1, col - 1)
        right_move = (row - 1, col + 1)
    # else black pawn
    else:
        left_move = (row + 1, col - 1)
        right_move = (row + 1, col + 1)

    if bounded(left_move) and occupied(left_move, board) and opposing(piece, left_move, board):
        moves.append((*left_move, ATTACK))

    if bounded(right_move) and occupied(right_move, board) and opposing(piece, right_move, board):
        moves.append((*right_move, ATTACK))


def occupied(loc, board):
    """
    checks if a position on the board is occupied

    :param loc: location to check
    :param board: current game state
    :return: whether the location on the board is occupied by a piece
    """
    row, col = loc
    return not board[row][col] == empty


def opposing(piece, loc, board):
    """
    checks if a piece's color opposes the piece's color at location on board,
    assuming location is non-empty

    :param piece: 'this' piece the player selected
    :param loc: the location of the piece to check
    :param board: the state of the board
    :return: whether 'this' piece is the enemy of the other
    """
    row, col = loc
    color_from = 'WHITE' if 'WHITE' in piece else 'BLACK'
    color_to = 'WHITE' if 'WHITE' in board[row][col] else 'BLACK'

    return not color_from == color_to


def bounded(loc):
    """
    checks if location adheres to bounds of board

    :param loc: location to check
    :return: whether in bounds i.e. (0 <= x, y < 8)
    """
    row, col = loc
    # YOU CAN CHAIN COMPARISONS!!! OMG 0.0
    return MAX_ROWS > row >= 0 and MAX_COLS > col >= 0


def valid_move(loc: tuple, moves: list):
    """
    verify a move is valid

    :param loc:
    :param moves:
    :return:
    """

    return (*loc, 'MOVE') in moves or (*loc, 'ATTACK') in moves





