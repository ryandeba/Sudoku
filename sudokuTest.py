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

	def test_isSolvedReturnsTrueWhenBoardIsSolved(self):
		self.board = Board("123456789456789123789123456231674895875912364694538217317265948542897631968341572")
		self.assertEqual(True, self.board.isSolved())

	def test_isSolvedReturnsFalseWhenBoardIsNotSolved(self):
		self.board = Board()
		self.assertEqual(False, self.board.isSolved())

	def test_getNextUnsolvedIndexAndPossibleValues(self):
		expectedResult = {'index': 0, 'possibleValues': ['1', '2', '3', '4', '5', '6', '7', '8', '9']}
		self.assertEqual(expectedResult, self.board.getNextUnsolvedIndexAndPossibleValues())

	def test_getPossibleValuesForIndex(self):
		self.board = Board('123456789')
		self.assertEqual(list('456789'), self.board.getPossibleValuesForIndex(9))

	def test_areRowsValidReturnsTrueWithBlankBoard(self):
		self.assertEquals(True, self.board.areRowsValid())

	def test_areRowsValidReturnsTrueWithSolvedBoard(self):
		self.board = Board("123456789456789123789123456231674895875912364694538217317265948542897631968341572")
		self.assertEquals(True, self.board.areRowsValid())

	def test_areRowsValidReturnsFalseWithInvalidRows(self):
		self.board = Board("11")
		self.assertEquals(False, self.board.areRowsValid())

    def test_isSolveable(self):
        self.assertEqual(Board().isSolveable(), True)
        self.assertEqual(Board('99').isSolveable(), False)

if __name__ == '__main__':
	unittest.main()
