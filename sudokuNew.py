class Sudoku:

    VALID_VALUES = list('1,2,3,4,5,6,7,8,9')

    def __init__(self, board = None):
        self.solutions = []
        self.board = ['0'] * 81
        if board == None or len(board) != 81:
            board = '0' * 81
        for i in range(81):
            self.setBoardIndexToValue(i, board[i])

    def __str__(self):
        result = ''
        counter = 0
        for cell in self.board:
            result += cell
            counter += 1
            if counter % 9 == 0:
                result += '\n'
        return result

    def setBoardIndexToValue(self, boardIndex, value):
        self.board[boardIndex] = self.convertToValidValue(value)

    def getValueAtBoardIndex(self, boardIndex):
        return self.board[boardIndex]
        
    def convertToValidValue(self, value):
        return str(value) if str(value) in list('0123456789') else '0'

    def solve(self):
        if self.isSolved():
            return True
        return True

    def isSolved(self):
        return self.areRowsValid() and self.areColumnsValid() and self.areSquaresValid()

    def areRowsValid(self):
        for i in [0,9,18,27,26,45,54,63,72]:
            rowValues = []
            for j in range(9):
                rowValues.append(self.getValueAtBoardIndex(i + j))
            if '0' in rowValues or (len(rowValues) != len(set(rowValues))):
                return False
        return True

    def areColumnsValid(self):
        for i in range(9):
            columnValues = []
            for j in [0,9,18,27,36,45,54,63,72]:
                columnValues.append(self.getValueAtBoardIndex(i + j))
            if '0' in columnValues or (len(columnValues) != len(set(columnValues))):
                return False
        return True

    def areSquaresValid(self):
        for i in [0,3,6,27,30,33,54,57,60]:
            squareValues = []
            for j in [0,1,2,9,10,11,18,19,20]:
                squareValues.append(self.getValueAtBoardIndex(i + j))
            if '0' in squareValues or (len(squareValues) != len(set(squareValues))):
                return False
        return True

    def canBoardIndexContainValue(self, boardIndex, value):
        return True
