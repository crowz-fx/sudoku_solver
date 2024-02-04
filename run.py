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

from solver import Solver
from file import FileUtils


class Run:
    """
    Wrapper class to handle the mid-level processing into the solve function.
    One main reason for the split is for testability, kind of would be
    integration tests across classes
    """

    def __init__(self) -> None:
        """"""
        self.solver = Solver()

    def process_oneliner(self, input):
        """
        Take the input from the oneliner, format into the list[list[int]] format
        required for the board

        Parameters
        ----------
        input : str
          One lone comma seperated string of the puzzle to be solved

        Raises
        ------
        RuntimeError
          If the input is not valid

        Return
        ------
        tuple
          (True/False, list[list[int]]) - Result from solve and where the board
          processing ended (would be complete if solveable)
        """
        input = input.replace(",", "")
        row_length = 9
        board = []

        for i in range(0, len(input), row_length):
            row_squished = input[i : i + row_length]

            temp_row = []
            for digit in row_squished:
                temp_row.append(int(digit))

            board.append(temp_row)

        if len(board) != 9:
            raise RuntimeError(
                "Your oneliner input is not valid, you don't have 9 rows!"
            )

        for row in board:
            if len(row) != 9:
                raise RuntimeError(
                    "Your oneliner input is not valid, a row doesn't have 9 digits!"
                )

        return self.solver.solve(board), board

    def process_file(self, file_name):
        """
        Read the file supplied by user, process the contents into the required format
        for the `solve()` function

        Parameters
        ----------
        file_name : str
            Name of the file that contains the puzzle

        Return
        ------
        tuple
            (True/False, list[list[int]]) - Result from solve and where the board
            processing ended (would be complete if solveable)
        """
        file_contents = FileUtils.read_file(file_name)
        board = []

        for line in file_contents:
            line = line.replace("\n", "")
            board.append(list(map(int, line.split(","))))

        return self.solver.solve(board), board
