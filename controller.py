from PySimpleGUI import Window
from chess.gui_helpers import highlight_board, draw_board
from chess.config import *


class Controller:
    """
    logical controller for the game of chess

    TODO: consolidate logical components
    TODO: attach AI component
    TODO: create checkmate feature
    TODO: create win screen
    TODO: attach options (separate window or adjacent)

    TODO !!! FIX QUEEN MOVE LIST
    """

    def __init__(self, window: Window, colors: list):
        """
        Controller is used to handle piece selection,
        de-selection, and moving

        :param window: used in updating the GUI
        """

        self.piece = None
        self.move_from = None
        # init GUI and original color pattern
        self.window = window
        self.colors = colors

    def select(self, board, loc, moves):
        """
        user select a square on the board will not be empty

        :param board: current state of game
        :param loc: the position the user selected
        :param moves: the possible moves the piece can perform
        :return: None
        """
        if not self.piece:
            self.__select_from(board, loc, moves)
        else:
            self.__select_to(board, loc)

    def deselect(self):
        self.piece = None
        self.move_from = None

    def __select_from(self, board, loc, moves):
        """
        occurs for when selection is choosing a piece

        :param board: the state of the game
        :param loc: the location of the piece selected
        :param moves: the moves this piece can perform
        :return: None
        """
        # FROM location, generate moves
        self.move_from = loc
        row, col = self.move_from
        self.piece = board[row][col]

        highlight_board(self.window, moves, board)

        return

    def __select_to(self, board, loc):
        """
        occurs for when selection is to move the piece
        to a location

        :param board: the current state of the game
        :param loc: the location to move the piece to
        :return: None
        """

        if loc == self.move_from:
            self.deselect()
            draw_board(self.window, board, self.colors)
            return

        row, col = loc
        board[row][col] = self.piece

        row, col = self.move_from
        board[row][col] = empty
        # UPDATE GUI:
        draw_board(self.window, board, self.colors)

        # move done, de-select
        self.deselect()
