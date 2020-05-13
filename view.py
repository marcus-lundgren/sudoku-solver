import copy
from board import Board

class View:
    def __init__(self, board: Board):
        self.board = board
        # Make a copy of the original board. It is needed in order to
        # print the outcome screens.
        self.original_board = copy.deepcopy(board)

    def clear_screen(self):
        import os
        os.system('clear')

    def print(self):
        self.clear_screen()
        self._print(self.board)

    def _print(self, board: Board):
        vertical_separator_line = '-' * 25
        print(vertical_separator_line)
        for y in range(0, 9):
            # The vertical separator line
            if y != 0 and y % 3 == 0:
                print(vertical_separator_line)

            row = "| "
            squares = board.get_row(y)
            for x, s in enumerate(squares):
                # The horizontal separator
                if x != 0 and x % 3 == 0:
                    row += '| '

                if s.is_set():
                    row += str(s.get_value())
                else:
                    row += ' '

                row += ' '
            print(row + '|')
        print(vertical_separator_line)

    def print_win(self):
        self.clear_screen()
        self._print(self.original_board)
        print('')
        print('Solution found!')
        print('')
        self._print(self.board)

    def print_loss(self):
        self.clear_screen()
        self.print(self.original_board)
        print('')
        print('No solution found =(')