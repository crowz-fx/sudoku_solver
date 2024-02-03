"""
    Copyright (C) 2024  Lui Crowie (@crowz-fx)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


class Solver:
    """
    Powerhouse of the application, the actual brains of solving the
    puzzles; either supplied or generated
    """

    def __init__(self) -> None:
        """"""

    def find_next_cell_to_solve(self, board):
        """Method to find the next cell in the board to solve

        Parameters
        ----------
        board : list[list[int]]
            Representation of the board in list of lists, 0's are for unsolved

        Return
        ------
        tuple
            ([0-8], [0-8]) or (None, None) if no cells that are empty
        """
        for row in range(0, 9):
            for column in range(0, 9):
                if board[row][column] == 0:
                    return (row, column)

        # We couldn't find an empty cell, return None, None
        return (None, None)

    def solve(self, board):
        """The money shot, the actual solve function to solve a sudoku puzzle

        This works through backtracking, try a new value, does it fit, if yes then
        mutate the board and continue

        Parameters
        ----------
        board : list[list[int]]
            Representation of the board in list of lists, 0's are for unsolved

        Return
        ------
        bool
            True/False based on what that guess results in or if the board
            has been solved
        """
        row, column = self.find_next_cell_to_solve(board)

        if row is None or column is None:
            # There is no more cells, it's complete?!
            return True

        # We have found a spot to put a guess, now make a guess between valid sudoku values 1-9
        for guess in range(1, 10):

            # If the guess is a valid value and doesn't break the rules, set it and continue
            if self.check_guess_is_valid(board, row, column, guess):

                board[row][column] = guess

                # Recursively call solve() until it's solved
                if self.solve(board):
                    return True

            # This guess wasn't the one, set back to default value, and backtrack
            board[row][column] = 0

        # Hmm, looks like this is unsolvable, go back up the chain
        return False

    def check_guess_is_valid(self, board, row, column, guess):
        """Method to take the guess and validate it against the row, the column and the 3x3
        square grid (sudoku rules duh)

        Parameters
        ----------
        board : list[list[int]]
            Representation of the board in list of lists, 0's are for unsolved
        row : int
            Value between 0-8
        column : int
            Value between 0-8
        guess : int
            Value generated that may or may not be valid

        Return
        ------
        bool
            True - if guess is valid within the rules, valid
            False - value exists or breaks the rules, not valid
        """
        if guess in board[row]:
            return False

        # Validate the guess doesn't exist in the row or any row at this column
        if guess in [board[range_row][column] for range_row in range(9)]:
            return False

        # Validate the 3x3 grid, final rule
        #   1. There are 3 "grids" or "chunks", 0, 1 and 2
        #   2. Reduce the row/column value into one of these "chunks" using modulo
        #   3. Go through the grid (all 9 values) and check guess doesn't exist already
        #     a. if not ==> Valid, return True
        #     b. if does ==> Not valid, return False
        row_grid = (row // 3) * 3
        column_grid = (column // 3) * 3

        for grid_row in range(row_grid, row_grid + 3):
            for grid_column in range(column_grid, column_grid + 3):
                if guess == board[grid_row][grid_column]:
                    return False

        # We still haven't matched the guess, so it's valid
        return True
