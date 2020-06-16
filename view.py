import copy
import curses
from board import Board

class View:
    def __init__(self, board: Board, stdscr: curses.window):
        self.board = board
        self.stdscr = stdscr

    def print_grid(self):
        # Clear the screen
        self.stdscr.clear()

        # Hide the cursor
        curses.curs_set(0)

        # Init the colors to be used
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)

        # Print the actual grid
        self.stdscr.vline(0, 0, "|", 13)
        for y in range(1, 4):
            self.stdscr.vline(0, y * 2 * 4, "|", 13)

        self.stdscr.hline(0, 0, "-", 25)
        for x in range(1, 4):
            self.stdscr.hline(x * 4, 0, "-", 25)

        # Print the starting square values. The color used is different
        # from the square values that are guessed.
        for y in range(0, 9):
            for x in range(0, 9):
                self.print_square(x, y, self.board.get_square_value(x, y), 2)

        self.stdscr.refresh()

    def print_square(self, x: int, y: int, v, color_pair = 1):
        sx, sy = self._to_screen_coordinates(x, y)
        vs = " " if v is None else str(v)
        self.stdscr.addstr(sy, sx, vs, curses.color_pair(color_pair))
        self.stdscr.refresh()

    def _print_outcome(self, text: str):
        self.stdscr.addstr(14, 2, text)
        self.stdscr.getkey()

    def print_win(self):
        self._print_outcome("Solution found!")

    def print_loss(self):
        self._print_outcome("No solution found =(")

    def _to_screen_coordinates(self, x, y):
        row_sos = int(y / 3)
        row_in_sos = y % 3
        sy = 1 + row_sos * 4 + row_in_sos

        col_sos = int(x / 3)
        col_in_sos = x % 3
        sx = 2 + col_sos * 8 + col_in_sos * 2

        return sx, sy
