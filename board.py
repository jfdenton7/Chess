import PySimpleGUI as sg
from chess.config import *
from chess.gui_helpers import gen_colors, gen_board, set_board, draw_board, highlight_board
from chess.move_generator import gen_moves, valid_move
from chess.controller import Controller


board = gen_board()
colors = gen_colors()
layout = set_board(board, colors)

window = sg.Window('Chess', layout)

controller = Controller(window, colors)


while True:
    # event will be read as key for button!
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    if type(event) is tuple:

        row, col = event

        # IF selecting empty square, wait for correct input
        while board[row][col] == empty:
            event, _ = window.read()
            row, col = event

        moves = gen_moves(board, event)
        moves.append((*event, 'MOVE'))
        controller.select(board, event, moves)

        # now access the TO location, store when valid
        event, _ = window.read()
        while not valid_move(event, moves):
            event, _ = window.read()

        controller.select(board, event, moves)

        # perform AI's turn


window.close()

