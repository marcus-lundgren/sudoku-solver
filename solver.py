import time
import typing
from board import Board
from view import View

class Solver:
    def __init__(self, board: Board, view: View, step_sleep: typing.Optional[float] = 0.001):
        self.board = board
        self.view = view
        self.step_sleep = step_sleep

    def solve(self):
        self.view.print_grid()

        # Calculate a list of non invalid values based on the starting state of the board.
        for y in range(0, 9):
            for x in range(0, 9):
                for i in range(1, 10):
                    s = self.board.get_square(x, y)
                    # This square has a solution already as it was provided in the starting state.
                    if s.get_value() is not None:
                        continue

                    # Add the value if it is valid given the starting state of the board.
                    if self.board.is_valid(x, y, i):
                        s.add_valid_value(i)

        if self._solver(0, 0):
            self.view.print_win()
        else:
            self.view.print_loss()

    def _solver(self, x: int, y: int) -> bool:
        is_on_last_index = x is None

        # If we are on the last square index, then all of the squares are correct!
        if is_on_last_index:
            return True

        new_x, new_y = self._get_next_index(x, y)

        # The value is known. Continue with the next coordinate
        if self.board.is_set(x, y):
            return self._solver(new_x, new_y)

        s = self.board.get_square(x, y)
        for i in s.valid_values:
            is_valid_placement = self.board.set_square(x, y, i)

            self.view.print_square(x, y, i)

            # Sleep for the configured amount of time
            if self.step_sleep is not None:
                time.sleep(self.step_sleep)

            # We found a valid guess for the current square.
            if is_valid_placement:
                if not self._solver(new_x, new_y):
                    # We couldn't find the solution with the current value.
                    self.board.clear_square(x, y)
                    self.view.print_square(x, y, None)
                    continue
                else:
                    # We found a solution!
                    return True

            # The currently guessed value can't yield a solution.
            self.board.clear_square(x, y)
            self.view.print_square(x, y, None)

        # We couldn't find the solution given the state of the previous guesses.
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
