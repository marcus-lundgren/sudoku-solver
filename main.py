from board import Board
from view import View
from solver import Solver

b =   '   9 3   '
b +=  ' 5 2  84 '
b +=  '3    4   '

b +=  '    3 5 1'
b +=  '78 5     '
b +=  '     6 94'

b +=  '9        '
b +=  ' 641   7 '
b +=  '    2765 '

board = Board(b)
view = View(board)
view.print()

solver = Solver(board, view, visualize_steps = True)
solver.solve()
