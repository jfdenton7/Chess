from chess.config import *
from chess.move_generator import gen_moves
from copy import deepcopy


class MinMaxPlayer:
    """
    pattern: selects moved based on cost function and
    depth search (provided by user)

    TODO allow recognition of checkmate
    TODO add positioning values
    TODO consolidate find best move with find best path!

    """
    def __init__(self, depth=3):
        """
        Create a Min-Max AI

        :param depth: the depth searched by tree (default 4)
        """
        self.depth = depth
        self.calculations = 0
        self.states = []
        self.best_moves = []

    def find_best_move(self, board, player):
        """
        find the best move given on a board

        guarantees board left un-modified

        :param board: the state of the game
        :param player: player's colors, use 'WHITE' or 'BLACK'
        :return: ((x1, y1), (x2, y2)) as move from : to as tuple
        """

        _board = deepcopy(board)
        pieces = MinMaxPlayer.__find_pieces(_board, player)

        for piece in pieces:

            moves = gen_moves(_board, piece)

            for move in moves:
                # splice out type
                move = move[:2]
                state = deepcopy(_board)
                MinMaxPlayer.__move_piece(state, piece, move)
                score = MinMaxPlayer.__calculate_strength(state, player)

                self.states.append((state, (piece, move), score))

        # search the set of moves that leads to the best outcome! only modifying score
        # second iteration, swap player
        player = MinMaxPlayer.__swap_player(player)
        max_score = NEG_INF
        best_move = None

        for path in self.states:
            board, move, score = path
            score = self.__find_best_path(player, board, score, 0)
            # if the score is higher, then that is the better move
            print('calculated score for move: {} is {}'.format(move, score))
            if score > max_score:
                best_move = move
                max_score = score

        print(f'total moves performed is: {self.calculations}')

        return best_move

    def __find_best_path(self, player, board, prev_score, depth):
        """
        find the best move following

        :param player: who the AI is playing
        :param board: the state of the game
        :return: the max score possible from this board
        """
        states = []
        max_score = prev_score
        pieces = MinMaxPlayer.__find_pieces(board, player)

        for piece in pieces:
            moves = gen_moves(board, piece)

            for move in moves:
                # splice out type
                move = move[:2]
                state = deepcopy(board)
                MinMaxPlayer.__move_piece(state, piece, move)
                score = MinMaxPlayer.__calculate_strength(state, player) + prev_score
                self.calculations += 1

                if score > max_score:
                    max_score = score

                states.append((state, score))

        depth += 1

        # finished processing? stop and return
        if depth >= self.depth:
            return max_score

        # remove worst moves
        # MinMaxPlayer.__pop_min(states)

        # swap over to other perspective
        player = MinMaxPlayer.__swap_player(player)

        # recursively call on all subsequent results
        for state in states:
            board, score = state
            max_score = max(self.__find_best_path(player, board, score, depth), max_score)

        # would return none following this line FIXME !!!
        return max_score

    @staticmethod
    def __pop_min(states: list):
        """
        removes all but maximum score in list

        [(board, score), (...), ....]

        :param states: holds game states and relative scores
        :return: None (modifies DS)
        """
        if len(states) < 1:
            return

        # init max score
        _, max_score = states[0]

        for state in states:
            _, score = state
            if score > max_score:
                max_score = score

        for state in states:
            _, score = state
            if score < max_score:
                states.remove(state)

    @staticmethod
    def __swap_player(player):
        """

        :param player:
        :return:
        """
        if player == 'WHITE':
            return 'BLACK'
        return 'WHITE'

    def __max(self) -> tuple:
        """
        grab the max or the first occurrence of the max
        based on the score of the move.

        :return: the 'best' given move
        """
        maxim = self.states[0]
        for i in range(1, len(self.states)):
            temp = self.states[i]
            if temp[2] > maxim[2]:
                maxim = self.states[i]
        return maxim

    @staticmethod
    def __find_pieces(board, player):
        """
        generate the coordinates of all pieces on the board
        which match 'player'

        :param board: state of the game
        :param player: either 'WHITE' or 'BLACK'
        :return: all such locations
        """
        pieces = []

        for i in range(MAX_ROWS):
            for j in range(MAX_COLS):
                piece = board[i][j]
                if player in piece:
                    pieces.append((i, j))

        return pieces

    @staticmethod
    def __count_pieces(board):
        """
        count total pieces of each player

        :param board: state of the game
        :return: total counts of pieces
        """
        count = {
            pawnW: 0,
            rookW: 0,
            knightW: 0,
            bishopW: 0,
            queenW: 0,
            kingW: 0,

            pawnB: 0,
            rookB: 0,
            knightB: 0,
            bishopB: 0,
            queenB: 0,
            kingB: 0
        }

        for i in range(MAX_ROWS):
            # mutually exclusive event, ignores EMPTY
            for piece in board[i]:
                if 'BLACK' in piece:
                    count[piece] = count[piece] + 1
                if 'WHITE' in piece:
                    count[piece] = count[piece] + 1

        return count

    @staticmethod
    def __move_piece(board, loc_from, loc_to):
        """
        move a piece on the board

        :param board: the current state of the game
        :param loc_from: moving from....
        :param loc_to: moving to...
        :return: None (only modifies board state)
        """

        row, col = loc_from
        piece = board[row][col]
        board[row][col] = empty

        row, col = loc_to
        board[row][col] = piece

    @staticmethod
    def __calculate_strength(board, player):
        """
        calculate the current strength of the 'player' based
        on game state given by 'board'

        :param board: the state of the game
        :param player: the player
        :return:
        """
        count = MinMaxPlayer.__count_pieces(board)

        total_white = PAWN * count[pawnW] + ROOK * count[rookW] + \
            KNIGHT * count[knightW] + BISHOP * count[bishopW] + \
            QUEEN * count[queenW] + \
            KING * count[knightW]

        total_black = PAWN * count[pawnB] + ROOK * count[rookB] + \
            KNIGHT * count[knightB] + BISHOP * count[bishopB] + \
            QUEEN * count[queenB] + \
            KING * count[knightB]

        if player == 'WHITE':
            return total_white - total_black

        return total_black - total_white


class EvolvingPlayer:

    def __init__(self):
        """
        player randomly generated probability vector

        TODO
        """
        pass

    def __gen_piece_val(self):
        """
        generate piece valuations (randomly)

        :return:
        """
        pass

    def __gen_pos_val(self):
        """
        generate positional values for a given piece (randomly)

        :return:
        """
        pass

    def __gen_opening_val(self):
        """
        generate starting move list (randomly)

        :return:
        """
        pass

    def __mutate(self, mutation, delta):
        """
        given valuation, change by no more than delta

        :return:
        """
        pass
