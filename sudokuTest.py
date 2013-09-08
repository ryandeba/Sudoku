from sudoku import *
import unittest

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_setIndexToValue(self):
        self.board.setIndexToValue(5, '9')
        self.assertEqual(self.board.getValueAtIndex(5), '9')

    def test_getValueAtIndex(self):
        self.board = Board('123456789')
        self.assertEqual(self.board.getValueAtIndex(3), '4')

    def test_getUnsolvedIndex(self):
        self.board = Board(list('123056789') * 9)
        self.assertEqual(self.board.getUnsolvedIndexes(), [3, 12, 21, 30, 39, 48, 57, 66, 75])

    def test_convertToValidValue(self):
        self.assertEqual(self.board.convertToValidValue('0'), '0')
        self.assertEqual(self.board.convertToValidValue(0), '0')
        self.assertEqual(self.board.convertToValidValue(''), '0')
        self.assertEqual(self.board.convertToValidValue('.'), '0')
        self.assertEqual(self.board.convertToValidValue('4'), '4')
        self.assertEqual(self.board.convertToValidValue(4), '4')

if __name__ == '__main__':
    unittest.main()
