# sudoku-solver
A simple solver for Sudoku written in Python.

## Introduction
sudoku-solver is capable of solving any given Sudoko board. It could also, with some modfications, be used in order to create Sudoku boards as well.

## Requirements

* Python 3 (developed/tested with 3.8)

As the `clear` command is used in order to clear the contents in the terminal between frames, it runs on Linux et al. Modify this to the equivalent to your platform if needed.

## How to use it
sudoku-solver runs in the terminal. Python 3 (developed/tested on 3.8) is required to run the program.

Before running the program, a desired board to solve can be set in the `main.py` file. It can then be started by issuing the following command:

    $ python3 /path/to/main.py

The solving progress will be visualized in the terminal with a hardcoded sleep pause between each action/frame. If this kind of time delaying eye candy isn't needed, commenting out the two lines regarding sleep and view printing in `solver.py` will significantly speed up the execution.

If a solution is found, a screen showing the starting of state and solution will be displayed:

    -------------------------
    |   3   |       |   1   |
    |     5 |     3 |     8 |
    |     7 | 6   2 |       |
    -------------------------
    |       |       | 3 8   |
    |       | 5 8   |   9   |
    | 9     |   1   |     2 |
    -------------------------
    |     3 |     7 | 8     |
    |       | 2     |   5 1 |
    |   2 6 |     1 |     9 |
    -------------------------
    
    Solution found!
    
    -------------------------
    | 6 3 9 | 8 4 5 | 2 1 7 |
    | 2 4 5 | 1 7 3 | 9 6 8 |
    | 1 8 7 | 6 9 2 | 5 4 3 |
    -------------------------
    | 4 6 1 | 7 2 9 | 3 8 5 |
    | 3 7 2 | 5 8 4 | 1 9 6 |
    | 9 5 8 | 3 1 6 | 4 7 2 |
    -------------------------
    | 5 1 3 | 9 6 7 | 8 2 4 |
    | 7 9 4 | 2 3 8 | 6 5 1 |
    | 8 2 6 | 4 5 1 | 7 3 9 |
    -------------------------
