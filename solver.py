import time
from board import Board
from view import View

class Solver:
    def __init__(self, board: Board, view: View):
        self.board = board
        self.view = view

    def solve(self):
        if self._solver(0, 0):
            self.view.print_win()
        else:
            self.view.print_loss()

    def _solver(self, x: int, y: int):
        is_on_last_index = x == None

        # If we are on the last square index,
        # then all of the squares are correct!
        if is_on_last_index:
            return True

        new_x, new_y = self._get_next_index(x, y)

        if self.board.is_set(x, y):
            return self._solver(new_x, new_y)

        for i in range(1, 10, 1):
            is_valid_placement = self.board.set_square(x, y, i)

            # Uncomment these lines to skip displaying the steps.
            # Will make the solving significantly much faster.
            time.sleep(0.0005)
            self.view.print()

            if is_valid_placement:
                if not self._solver(new_x, new_y):
                    self.board.clear_square(x, y)
                    continue
                else:
                    return True

            self.board.clear_square(x, y)

        return False

    @staticmethod
    def _get_next_index(x: int, y: int) -> tuple:
        # Still on the same row
        if x < 8:
            return x + 1, y

        # New row is needed
        if y < 8:
            return 0, y + 1

        # We're out of bounds, return invalid location
        return None, None
