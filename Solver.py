import math

from Cell import Cell
from Sudoku import Sudoku

fieldSize = 4
sudokuInitial = Sudoku([[Cell(0, False) for col in range(fieldSize)] for row in range(fieldSize)])
sudoku = Sudoku()
rec = 0
counter = (fieldSize**2) - fieldSize
failedStates = set()


def init():
    global sudoku
    fillSudoku()
    sudoku = Sudoku(sudokuInitial.field)
    print(str(sudoku))
    solve()
    #printSudoku()
    #print("done: " + str(rec))


def fillSudoku():
    sudokuInitial.field[0][2] = Cell(1, True)
    sudokuInitial.field[1][0] = Cell(4, True)
    sudokuInitial.field[2][3] = Cell(2, True)
    sudokuInitial.field[3][1] = Cell(3, True)

    # 6x6
    # sudokuInitial.field[0][0] = Cell(6, True)
    # sudokuInitial.field[0][1] = Cell(4, True)
    # sudokuInitial.field[0][3] = Cell(2, True)
    #
    # sudokuInitial.field[1][1] = Cell(5, True)
    # sudokuInitial.field[1][2] = Cell(1, True)
    #
    # sudokuInitial.field[2][0] = Cell(3, True)
    # sudokuInitial.field[2][1] = Cell(6, True)
    # sudokuInitial.field[2][2] = Cell(4, True)
    # sudokuInitial.field[2][5] = Cell(2, True)
    #
    # sudokuInitial.field[3][0] = Cell(5, True)
    # sudokuInitial.field[3][3] = Cell(4, True)
    # sudokuInitial.field[3][4] = Cell(3, True)
    # sudokuInitial.field[3][5] = Cell(6, True)
    #
    # sudokuInitial.field[4][3] = Cell(6, True)
    # sudokuInitial.field[4][4] = Cell(4, True)
    #
    # sudokuInitial.field[5][2] = Cell(6, True)
    # sudokuInitial.field[5][4] = Cell(2, True)
    # sudokuInitial.field[5][5] = Cell(5, True)



    # Medium sudoku
    # sudokuInitial.field[0][0] = Cell(2, True)
    # sudokuInitial.field[0][4] = Cell(1, True)
    # sudokuInitial.field[1][1] = Cell(6, True)
    # sudokuInitial.field[1][6] = Cell(9, True)
    # sudokuInitial.field[1][8] = Cell(3, True)
    # sudokuInitial.field[2][3] = Cell(6, True)
    # sudokuInitial.field[2][5] = Cell(9, True)
    # sudokuInitial.field[2][6] = Cell(7, True)
    # sudokuInitial.field[2][7] = Cell(5, True)
    # sudokuInitial.field[3][2] = Cell(5, True)
    # sudokuInitial.field[3][8] = Cell(4, True)
    # sudokuInitial.field[4][0] = Cell(1, True)
    # sudokuInitial.field[4][1] = Cell(2, True)
    # sudokuInitial.field[4][7] = Cell(8, True)
    # sudokuInitial.field[4][8] = Cell(7, True)
    # sudokuInitial.field[5][0] = Cell(8, True)
    # sudokuInitial.field[5][6] = Cell(5, True)
    # sudokuInitial.field[6][1] = Cell(9, True)
    # sudokuInitial.field[6][2] = Cell(7, True)
    # sudokuInitial.field[6][3] = Cell(3, True)
    # sudokuInitial.field[6][5] = Cell(8, True)
    # sudokuInitial.field[7][0] = Cell(3, True)
    # sudokuInitial.field[7][2] = Cell(2, True)
    # sudokuInitial.field[7][7] = Cell(6, True)
    # sudokuInitial.field[8][4] = Cell(2, True)
    # sudokuInitial.field[8][8] = Cell(9, True)

    # HARD SUDOKU
    # sudoku[0][0] = Cell(8, True)
    # sudoku[1][2] = Cell(3, True)
    # sudoku[1][3] = Cell(6, True)
    # sudoku[2][1] = Cell(7, True)
    # sudoku[2][4] = Cell(9, True)
    # sudoku[2][6] = Cell(2, True)
    # sudoku[3][1] = Cell(5, True)
    # sudoku[3][5] = Cell(7, True)
    # sudoku[4][4] = Cell(4, True)
    # sudoku[4][5] = Cell(5, True)
    # sudoku[4][6] = Cell(7, True)
    # sudoku[5][3] = Cell(1, True)
    # sudoku[5][7] = Cell(3, True)
    # sudoku[6][2] = Cell(1, True)
    # sudoku[6][7] = Cell(6, True)
    # sudoku[6][8] = Cell(8, True)
    # sudoku[7][2] = Cell(8, True)
    # sudoku[7][3] = Cell(5, True)
    # sudoku[7][7] = Cell(1, True)
    # sudoku[8][1] = Cell(9, True)
    # sudoku[8][6] = Cell(4, True)


def solve():
    global counter
    # solveRecursive(0, 0, 1, False)
    #solveRecursivePart2(1, 0, 0)
    # counter-=1
    for i in range(1, fieldSize+1):
        for y in range(fieldSize):
            for x in range(fieldSize):
                if counter != 0: solveRecursive(i, x, y)

    print("Doneeeee")

def solveRecursive(value, x, y):
    global counter

    if counter == 0:
        print(str(sudoku))
        return True

    if sudoku.field[y][x].value != 0: return False

    if sudoku.field[y][x].constant or isNumberInBlock(value, x, y) or isNumberInCol(value, x) or isNumberInRow(value, y):
        sudokuFailed = Sudoku(sudoku.field)
        failedStates.add(sudokuFailed)
        #print("added to failed states")
        return False

    sudoku.field[y][x] = Cell(value, False)
    counter -= 1
    for i in range(1, fieldSize+1):
        for y2 in range(fieldSize):
            for x2 in range(fieldSize):
                if solveRecursive(i, x2, y2): return True
    sudoku.field[y][x] = Cell(0, False)
    counter += 1
    return False



def getPosibleNumbersRandom(x, y):
    return getPossibleNumbers(x, y)


def getPossibleNumbers(x, y):
    possibleNumbers = []
    for n in range(1, fieldSize + 1):
        if not isNumberInBlock(n, x, y) and not isNumberInCol(n, x) and not isNumberInRow(n, y):
            possibleNumbers.append(n)
    return possibleNumbers


def isNumberInBlock(n, x, y):
    blockSize = int(math.sqrt(fieldSize))
    startRow = int((math.floor(y / blockSize)) * blockSize)
    startColl = int((math.floor(x / blockSize)) * blockSize)

    for i in range(blockSize):
        for t in range(blockSize):
            if sudoku.field[startRow + i][startColl + t].value == n: return True;
    return False


def isNumberInRow(n, y):
    rowToCheck = map(lambda elem: elem.value, sudoku.field[y])
    return (n in list(rowToCheck))


def isNumberInCol(n, x):
    rowToCheck = map(lambda elem: elem[x].value, sudoku.field)
    return (n in list(rowToCheck))

init()
