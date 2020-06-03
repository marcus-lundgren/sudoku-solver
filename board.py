from collections import Counter
from square import Square

class Board:
    def __init__(self, board_string: str):
        # Check that we the given string contains correct
        # amout of characters.
        if len(board_string) != 9 * 9:
            raise ValueError('The given board string is of incorrect length.')

        self.squares = self.create_board(board_string)

        # Verify that the starting point is valid.
        if not self.is_board_valid():
            raise ValueError('The given board string does not result in a valid starting point.')

    def create_board(self, board_string: str):
        return [Square(c) for c in board_string]

    def is_set(self, x, y):
        return self._get_square(x, y).is_set()

    def set_square(self, x, y, value):
        is_valid = self.is_valid(x, y, value)
        self._get_square(x, y).set_value(value)
        return is_valid

    def is_valid(self, x, y, value: int) -> bool:
        # Check the row
        row = self.get_row(y)
        if any([s.get_value() == value for s in row]):
            return False

        # Check the column
        col = self.get_column(x)
        if any([s.get_value() == value for s in col]):
            return False

        # Check the square of squares
        sos = self.get_square_of_squares(x, y)
        if any([s.get_value() == value for s in sos]):
            return False

        # If we got this far, then the value is valid!
        return True

    def clear_square(self, x: int, y: int):
        self._get_square(x, y).set_value(None)

    def get_row(self, row_num: int):
        return self.squares[9 * row_num : 9 * (row_num + 1)]

    def get_column(self, col_num: int):
        return self.squares[col_num :: 9]

    def _is_valid_square_range(self, squares):
        counter = Counter([s.get_value() for s in squares if s.get_value() is not None])
        items = counter.items()
        return all([v == 1 for k, v in items])

    def get_square_of_squares(self, x, y):
        square_row_start = int(y / 3) * 3
        square_col_start = int(x / 3) * 3
        for row_num in range(square_row_start, square_row_start + 3):
            for col_num in range(square_col_start, square_col_start + 3):
                yield self._get_square(col_num, row_num)

    def _get_square(self, x, y):
        return self.squares[x + y * 9]

    def is_board_valid(self):
        # Check the rows and columns
        if not all([self._is_valid_square_range(self.get_row(i)) and self._is_valid_square_range(self.get_column(i)) for i in range(0, 9)]):
            return False

        # Check squares of squares
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                sos = self.get_square_of_squares(x, y)
                if not self._is_valid_square_range(sos):
                    return False

        return True
