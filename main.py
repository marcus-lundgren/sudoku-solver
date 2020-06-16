from board import Board
from view import View
from solver import Solver
import curses


def main(stdscr: curses.window):
    b =  '4 9      '
    b += '       2 '
    b += '18 7   6 '

    b += '7   6    '
    b += ' 9     3 '
    b += '    23  6'

    b += '  3      '
    b += '  2   5 3'
    b += '   9 7  4'

    board = Board(b)
    view = View(board, stdscr)

    solver = Solver(board, view)
    solver.solve()


curses.wrapper(main)
