from unittest import TestCase
from chess.config import *
from chess.move_generator import gen_moves


# basic starting set up
SAMPLE_BOARD_1 = [[rookB, knightB, bishopB, queenB, kingB, bishopB, knightB, rookB],
             [pawnB] * 8,
             [empty] * 8,
             [empty] * 8,
             [empty] * 8,
             [empty] * 8,
             [pawnW] * 8,
             [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]

# more complex pawn set
SAMPLE_BOARD_2 = [[rookB, empty, bishopB, queenB, kingB, bishopB, knightB, rookB],
                  [pawnB, pawnB, empty, pawnB, pawnB, empty, pawnB, pawnB],
                  [empty, empty, empty, empty, empty, empty, empty, empty],
                  [knightB, empty, pawnB, empty, empty, pawnB, empty, empty],
                  [empty, empty, empty, empty, empty, pawnW, empty, empty],
                  [empty, empty, empty, empty, empty, empty, empty, empty],
                  [pawnW, pawnW, pawnW, pawnW, pawnW, empty, pawnW, pawnW],
                  [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]

# simple rook set with block
SAMPLE_BOARD_3 = [[rookB, empty, bishopB, queenB, kingB, bishopB, knightB, rookB],
                  [empty, pawnB, empty, pawnB, pawnB, empty, pawnB, pawnB],
                  [pawnB, empty, empty, empty, empty, empty, empty, empty],
                  [knightB, empty, pawnB, empty, empty, pawnB, empty, empty],
                  [empty, empty, empty, empty, empty, pawnW, empty, empty],
                  [empty, empty, empty, empty, empty, empty, empty, empty],
                  [pawnW, pawnW, pawnW, pawnW, pawnW, empty, pawnW, pawnW],
                  [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]

# more complex rook set
SAMPLE_BOARD_4 = [[empty, empty, bishopB, queenB, kingB, bishopB, knightB, rookB],
                  [empty, pawnB, empty, pawnB, pawnB, empty, pawnB, pawnB],
                  [empty, empty, empty, empty, empty, empty, empty, empty],
                  [pawnB, empty, pawnB, rookB, empty, pawnB, empty, empty],
                  [empty, empty, empty, empty, empty, pawnW, empty, empty],
                  [empty, knightB, empty, empty, empty, empty, empty, empty],
                  [pawnW, pawnW, pawnW, pawnW, pawnW, empty, pawnW, pawnW],
                  [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]

# simple knight case
SAMPLE_BOARD_5 = [[rookB, empty, bishopB, queenB, kingB, bishopB, knightB, rookB],
                  [pawnB, pawnB, empty, pawnB, pawnB, empty, pawnB, pawnB],
                  [knightB, empty, empty, empty, empty, empty, empty, empty],
                  [empty, empty, pawnB, empty, empty, pawnB, empty, empty],
                  [empty, empty, empty, empty, empty, pawnW, empty, empty],
                  [empty, empty, empty, empty, empty, empty, empty, empty],
                  [pawnW, pawnW, pawnW, pawnW, pawnW, empty, pawnW, pawnW],
                  [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]

# complex knight case
SAMPLE_BOARD_6 = [[rookB, empty, bishopB, queenB, kingB, bishopB, empty, rookB],
                  [pawnB, pawnB, empty, pawnB, pawnB, empty, pawnB, pawnB],
                  [knightB, empty, empty, empty, empty, empty, empty, empty],
                  [empty, empty, pawnB, empty, empty, pawnB, empty, empty],
                  [empty, empty, empty, empty, knightB, pawnW, empty, empty],
                  [empty, empty, empty, empty, empty, empty, empty, empty],
                  [pawnW, pawnW, pawnW, pawnW, pawnW, empty, pawnW, pawnW],
                  [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]


# simple bishop case
SAMPLE_BOARD_7 = [[rookB, empty, bishopB, queenB, kingB, bishopB, knightB, rookB],
                  [pawnB, pawnB, empty, empty, pawnB, empty, pawnB, pawnB],
                  [empty, empty, empty, pawnB, empty, empty, empty, empty],
                  [knightB, empty, pawnB, empty, empty, pawnB, empty, empty],
                  [empty, empty, empty, empty, empty, pawnW, empty, empty],
                  [empty, empty, empty, empty, empty, empty, empty, empty],
                  [pawnW, pawnW, pawnW, pawnW, pawnW, empty, pawnW, pawnW],
                  [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]

# complex bishop case and simple queen case
SAMPLE_BOARD_8 = [[rookB, empty, empty, queenB, kingB, bishopB, knightB, rookB],
                  [pawnB, pawnB, empty, empty, pawnB, empty, pawnB, pawnB],
                  [empty, empty, empty, pawnB, bishopB, empty, empty, empty],
                  [knightB, empty, pawnB, empty, empty, pawnB, empty, empty],
                  [empty, empty, empty, empty, empty, pawnW, empty, empty],
                  [empty, empty, empty, empty, empty, empty, empty, empty],
                  [pawnW, pawnW, pawnW, pawnW, pawnW, empty, pawnW, pawnW],
                  [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]

# complex queen case and simple king case
SAMPLE_BOARD_9 = [[rookB, empty, empty, empty, kingB, bishopB, knightB, rookB],
                  [pawnB, pawnB, empty, empty, pawnB, empty, pawnB, pawnB],
                  [empty, empty, empty, pawnB, bishopB, empty, empty, empty],
                  [knightB, empty, pawnB, queenB, empty, pawnB, empty, empty],
                  [empty, empty, empty, empty, empty, pawnW, empty, empty],
                  [empty, empty, empty, empty, empty, empty, empty, empty],
                  [pawnW, pawnW, pawnW, pawnW, pawnW, empty, pawnW, pawnW],
                  [rookW, knightW, bishopW, queenW, kingW, bishopW, knightW, rookW]]


class TestGenMovesPawn(TestCase):

    def setUp(self) -> None:
        pass

    def test_starting_board(self):

        for i in range(MAX_ROWS):
            res = gen_moves(SAMPLE_BOARD_1, (1, i))
            self.assertIn((2, i, 'MOVE'), res)
            self.assertIn((3, i, 'MOVE'), res)

    def test_mid_game_board_basic(self):
        # using pawn at location (3, 2)
        res = gen_moves(SAMPLE_BOARD_2, (3, 2))
        self.assertIn((4, 2, 'MOVE'), res)

    def test_mid_game_board_blocked(self):
        # using pawn at location (3 , 5)
        res = gen_moves(SAMPLE_BOARD_2, (3, 5))
        # no moves possible
        self.assertEqual(0, len(res))

    def test_mid_game_board_diagonal_attack(self):
        pass  # TODO


class TestGenMovesRook(TestCase):

    def setUp(self) -> None:
        pass

    def test_starting_board(self):
        # should have no moves available
        res = gen_moves(SAMPLE_BOARD_1, (0, 0))
        self.assertEqual(0, len(res))

    def test_simple_rook_set(self):
        res = gen_moves(SAMPLE_BOARD_3, (0, 0))
        self.assertEqual(2, len(res))

    def test_complex_rook_set(self):
        res = gen_moves(SAMPLE_BOARD_4, (3, 3))
        self.assertEqual(5, len(res))
        self.assertIn((6, 3, 'ATTACK'), res)

    def test_edge_case(self):
        pass  # TODO


class TestGenMovesKnight(TestCase):

    def setUp(self) -> None:
        pass

    def test_starting_board(self):
        # two moves
        res = gen_moves(SAMPLE_BOARD_1, (0, 1))
        self.assertEqual(2, len(res))
        self.assertIn((2, 0, 'MOVE'), res)

    def test_simple_knight(self):
        res = gen_moves(SAMPLE_BOARD_5, (2, 0))
        self.assertEqual(3, len(res))

    def test_complex_knight(self):
        res = gen_moves(SAMPLE_BOARD_6, (4, 4))
        self.assertEqual(7, len(res))
        self.assertIn((6, 3, 'ATTACK'), res)

    def test_edge_case(self):
        pass  # TODO


class TestGenMovesBishop(TestCase):

    def setUp(self) -> None:
        pass

    def test_starting_board(self):
        res = gen_moves(SAMPLE_BOARD_1, (0, 2))
        self.assertEqual(0, len(res))

    def test_simple_bishop(self):
        res = gen_moves(SAMPLE_BOARD_7, (0, 2))
        self.assertEqual(2, len(res))

    def test_complex_bishop(self):
        res = gen_moves(SAMPLE_BOARD_8, (2, 4))
        self.assertEqual(7, len(res))

    def test_edge_case(self):
        pass  # TODO


class TestGenMovesQueen(TestCase):

    def setUp(self) -> None:
        pass

    def test_starting_board(self):
        res = gen_moves(SAMPLE_BOARD_1, (0, 3))
        self.assertEqual(0, len(res))

    def test_simple_queen(self):
        res = gen_moves(SAMPLE_BOARD_8, (0, 3))
        self.assertEqual(5, len(res))

    def test_complex_queen(self):
        res = gen_moves(SAMPLE_BOARD_9, (3, 3))
        self.assertEqual(11, len(res))

    def test_edge_case(self):
        pass  # TODO


class TestGenMovesKing(TestCase):

    def setUp(self) -> None:
        pass

    def test_starting_board(self):
        res = gen_moves(SAMPLE_BOARD_1, (0, 4))
        self.assertEqual(0, len(res))

    def test_simple_king(self):
        res = gen_moves(SAMPLE_BOARD_9, (0, 4))
        self.assertEqual(2, len(res))

    def test_complex_king(self):
        pass

    def test_edge_case(self):
        pass  # TODO

    def test_near_king(self):
        pass  # TODO

