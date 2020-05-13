from square import Square

class Board:
    def __init__(self, board_string):
        if len(board_string) != 9 * 9:
            print("No good board string")
            return
        self.squares = self.create_board(board_string)

    def create_board(self, board_string: str):
        squares = []
        for c in board_string:
            squares.append(Square(c))
        return squares

    def is_set(self, x, y):
        return self.squares[x + y * 9].is_set()

    def set_square(self, x, y, value):
        is_valid = self.is_valid(x, y, value)
        self.squares[x + y * 9].set_value(value)
        return is_valid

    def is_valid(self, x, y, value: int) -> bool:
        # Check the row
        row = self.get_row(y)
        for s in row:
            # print(f"ROW - {s.get_value()} == {value} ??")
            if s.get_value() == value:
                return False

        # Check the column
        col = self.get_column(x)
        for s in col:
            # print(f"COL - {s.get_value()} == {value} ??")
            if s.get_value() == value:
                return False

        # Check the square of squares
        square_row_start = int(y / 3) * 3
        square_col_start = int(x / 3) * 3
        for row_num in range(square_row_start, square_row_start + 3):
            row = self.get_row(row_num)
            for index, s in enumerate(row):
                if index < square_col_start or square_col_start + 2 < index:
                    continue

                # print(f"SS - {s.get_value()} == {value} ??")

                if s.get_value() == value:
                    return False

        # If we got this far, then the value is valid!
        return True

    def clear_square(self, x: int, y: int):
        self.squares[x + y * 9].set_value(None)

    def get_row(self, row_num: int):
        return self.squares[9 * row_num : 9 * (row_num + 1)]

    def get_column(self, col_num: int):
        return self.squares[col_num :: 9]