import PySimpleGUI as sg
from PySimpleGUI import Window
from chess.config import *


def gen_colors() -> list:
    """
    generates a boolean map for the colors of
    the board
    :param colors: where the result is stored
    :return: nothing
    """
    is_white = False
    colors = []

    for i in range(MAX_COLS):
        is_white = not is_white
        row = []

        for j in range(MAX_ROWS):
            row.append('#F0D9B5' if is_white else '#B58863')
            is_white = not is_white

        colors.append(row)

    return colors


def gen_board() -> list:
    """
    generate the initial layout of the chess board

    :return: a board of the appropriate enums
    """

    # 8 x 8 board with enum pieces
    board = [[rookB, knightB, bishopB, queenB, kingB, bishopB, knightB, rookB],
             [pawnB] * 8,
             [empty] * 8,
             [empty] * 8,
             [empty] * 8,
             [empty] * 8,
             [pawnW] * 8,
             [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]

    return board


def set_board(board: list, colors: list):
    """
    set the pieces from board onto a button layout
    :param board:
    :param colors:
    :return: the layout of buttons with a set board
    """
    board_layout = []

    if not colors:
        colors = gen_colors()

    for i in range(MAX_COLS):

        row = []
        for j in range(MAX_ROWS):
            img = assets[board[i][j]]
            button = sg.Button('', image_filename=img, size=(1, 1), image_size=(65, 65), button_color=('white', colors[i][j]), key=(i, j), pad=(0, 0))
            row.append(button)

        board_layout.append(row)

    return board_layout


def highlight_moves(window: Window, moves: list):
    """
    highlight available moves on board

    :param window:
    :param moves:
    :return:
    """
    pass


def draw_board(window: Window, board: list, colors: list):
    """
    update the board with any new moves,
    from window by key and use button.Update(...) to
    modify pieces

    :param window: access to GUI
    :param board: current state of game
    :param colors: original color distribution of board
    :return:
    """

    # loop through and re-draw pieces
    for i in range(MAX_COLS):
        for j in range(MAX_ROWS):
            # access
            img = assets[board[i][j]]
            color = colors[i][j]
            # update button
            element = window.FindElement(key=(i, j))
            element.Update(image_filename=img, image_size=(65, 65), button_color=('white', color))


def highlight_board(window: Window, moves: list, board: list):
    """
    highlight the board to display available moves to user

    :param window: the GUI
    :param moves: current set of available moves
    :param board:
    :param loc:
    :return:
    """

    for move in moves:
        row, col, color = move
        color = 'green' if color == 'MOVE' or color == 'SELECT' else 'red'
        img = assets[board[row][col]]
        element = window.FindElement(key=(row, col))
        element.Update(image_filename=img, image_size=(65, 65), button_color=('white', color))

