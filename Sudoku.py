from Cell import Cell


class Sudoku(object):

    def __init__(self, field=None):
        self.field = None
        if(field != None):
            self.createCopy(field)

    def __eq__(self, other):
        if not isinstance(other, Sudoku):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.field == other.field

    def createCopy(self, field):
        self.field = [[Cell(0, False) for col in range(len(field))] for row in range(len(field))]
        for y in range(len(field)):
            for x in range(len(field[y])):
                self.field[y][x] = Cell(field[y][x].value, field[y][x].constant)

    def __str__(self):
        sudokuString = ""
        for row in range(len(self.field)):
            sudokuString += "\n"
            for col in range(len(self.field[row])):
                if self.field[row][col].constant:
                    sudokuString += "[" + str(self.field[row][col].value) + "], "
                else:
                    sudokuString += " " + str(self.field[row][col].value) + " , "

        return sudokuString

    def __hash__(self):
        return hash(str(self.field))
