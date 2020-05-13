from board import Board
from view import View
from solver import Solver

b =   ' 3     1 '
b +=  '  5  3  8'
b +=  '  76 2   '

b +=  '      38 '
b +=  '   58  9 '
b +=  '9   1   2'

b +=  '  3  78  '
b +=  '   2   51'
b +=  ' 26  1  9'

board = Board(b)
view = View(board)
view.print()

solver = Solver(board, view)
solver.solve()