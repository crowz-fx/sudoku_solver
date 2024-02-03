from solver import Solver


class Run:
    """
    Wrapper class to handle the mid-level processing into the solve function.
    One main reason for the split is for testability, kind of would be
    integration tests across classes
    """

    def __init__(self) -> None:
        """"""
        pass

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

        return Solver().solve(board), board
