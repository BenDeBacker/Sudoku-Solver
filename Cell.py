class Cell(object):
    """A cell in the sudoku"""

    def __init__(self, value, constant, possibleNumbers=None):
        self.value = value
        self.constant = constant
        self.possibleNumbers = possibleNumbers

    def __eq__(self, other):
        if not isinstance(other, Cell):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.value == other.value and self.constant == other.constant

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value * 13)

