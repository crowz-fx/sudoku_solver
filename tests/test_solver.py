import unittest

from solver import Solver


class TestSolver(unittest.TestCase):

    def test_find_next_cell_to_solve_with_no_empties(self):
        """
        Test that when run and there is no empty cells
        """
        board = [
            [4, 3, 8, 1, 2, 7, 5, 9, 6],
            [2, 6, 1, 5, 9, 3, 8, 4, 7],
            [9, 7, 5, 6, 8, 4, 3, 2, 1],
            [7, 2, 4, 8, 3, 9, 1, 6, 5],
            [8, 9, 6, 2, 5, 1, 7, 3, 4],
            [5, 1, 3, 4, 7, 6, 9, 8, 2],
            [1, 8, 7, 3, 4, 2, 6, 5, 9],
            [3, 4, 9, 7, 6, 5, 2, 1, 8],
            [6, 5, 2, 9, 1, 8, 4, 7, 3],
        ]

        self.assertEqual((None, None), Solver().find_next_cell_to_solve(board))

    def test_find_next_cell_to_solve_with_empties(self):
        """
        Test that when run and there is empty cells
        """
        board = [
            [4, 3, 8, 1, 2, 7, 5, 9, 0],
            [2, 6, 1, 5, 9, 3, 8, 4, 7],
            [9, 7, 5, 6, 8, 4, 3, 2, 1],
            [7, 2, 4, 8, 3, 9, 1, 6, 5],
            [8, 9, 6, 0, 5, 1, 7, 3, 4],
            [5, 1, 3, 4, 7, 6, 9, 8, 2],
            [1, 0, 7, 3, 4, 2, 6, 5, 9],
            [3, 4, 9, 7, 6, 5, 2, 1, 8],
            [6, 5, 2, 9, 1, 8, 4, 7, 3],
        ]

        self.assertEqual((0, 8), Solver().find_next_cell_to_solve(board))

    def test_check_guess_is_valid_with_valid(self):
        """
        Test that when run and the guess is valid
        """
        board = [
            [4, 3, 8, 0, 2, 7, 5, 9, 6],
            [2, 6, 1, 5, 9, 3, 8, 4, 7],
            [9, 7, 5, 6, 8, 4, 3, 2, 1],
            [7, 2, 4, 8, 3, 9, 1, 6, 5],
            [8, 9, 6, 2, 5, 1, 7, 3, 4],
            [5, 1, 3, 4, 7, 6, 9, 8, 2],
            [1, 8, 7, 3, 4, 2, 6, 5, 9],
            [3, 4, 9, 7, 6, 5, 2, 1, 8],
            [6, 5, 2, 9, 1, 8, 4, 7, 3],
        ]

        self.assertEqual(True, Solver().check_guess_is_valid(board, 0, 3, 1))

    def test_check_guess_is_valid_with_invalid(self):
        """
        Test that when run and the guess is not valid
        """
        board = [
            [4, 3, 8, 0, 2, 7, 5, 9, 6],
            [2, 6, 1, 5, 9, 3, 8, 4, 7],
            [9, 7, 5, 6, 8, 4, 3, 2, 1],
            [7, 2, 4, 8, 3, 9, 1, 6, 5],
            [8, 9, 6, 2, 5, 1, 7, 3, 4],
            [5, 1, 3, 4, 7, 6, 9, 8, 2],
            [1, 8, 7, 3, 4, 2, 6, 5, 9],
            [3, 4, 9, 7, 6, 5, 2, 1, 8],
            [6, 5, 2, 9, 1, 8, 4, 7, 3],
        ]

        self.assertEqual(False, Solver().check_guess_is_valid(board, 0, 3, 9))

    def test_solve_with_insolvable(self):
        """
        Test solve that cannot be solved
        """
        board = [
            [3, 3, 0, 8, 1, 8, 5, 9, 6],
            [2, 6, 1, 5, 9, 3, 8, 4, 7],
            [9, 7, 5, 6, 8, 4, 3, 2, 1],
            [7, 2, 4, 8, 3, 9, 1, 6, 5],
            [8, 9, 0, 2, 5, 1, 7, 3, 4],
            [5, 1, 9, 4, 7, 6, 9, 8, 2],
            [1, 8, 7, 3, 4, 2, 6, 5, 9],
            [3, 4, 9, 7, 6, 5, 2, 1, 8],
            [6, 5, 0, 9, 1, 8, 4, 7, 3],
        ]

        self.assertEqual(False, Solver().solve(board))

    def test_solve_with_solvable_master(self):
        """
        Test solve with an master level puzzle
        """
        board = [
            [4, 3, 8, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 7],
            [0, 0, 5, 0, 0, 0, 0, 2, 1],
            [0, 0, 0, 8, 3, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 3, 0],
            [5, 0, 0, 4, 0, 0, 0, 8, 0],
            [0, 0, 0, 0, 0, 2, 6, 0, 9],
            [0, 4, 0, 0, 0, 5, 0, 0, 0],
            [6, 0, 0, 0, 1, 0, 0, 0, 0],
        ]

        expected = [
            [4, 3, 8, 1, 2, 7, 5, 9, 6],
            [2, 6, 1, 5, 9, 3, 8, 4, 7],
            [9, 7, 5, 6, 8, 4, 3, 2, 1],
            [7, 2, 4, 8, 3, 9, 1, 6, 5],
            [8, 9, 6, 2, 5, 1, 7, 3, 4],
            [5, 1, 3, 4, 7, 6, 9, 8, 2],
            [1, 8, 7, 3, 4, 2, 6, 5, 9],
            [3, 4, 9, 7, 6, 5, 2, 1, 8],
            [6, 5, 2, 9, 1, 8, 4, 7, 3],
        ]
        Solver().solve(board)
        self.assertEqual(board, expected)

    def test_solve_with_solvable_expert(self):
        """
        Test solve with an expert level puzzle
        """
        board = [
            [4, 9, 6, 0, 0, 0, 0, 0, 0],
            [0, 0, 8, 0, 9, 0, 7, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 6, 0],
            [5, 0, 0, 2, 0, 0, 0, 4, 0],
            [0, 0, 0, 0, 0, 8, 2, 0, 0],
            [8, 0, 0, 0, 0, 5, 6, 0, 0],
            [0, 6, 2, 0, 1, 0, 0, 0, 0],
            [0, 0, 5, 0, 6, 0, 0, 9, 0],
            [0, 7, 0, 0, 0, 9, 0, 0, 0],
        ]

        expected = [
            [4, 9, 6, 7, 5, 1, 8, 2, 3],
            [2, 1, 8, 6, 9, 3, 7, 5, 4],
            [7, 5, 3, 4, 8, 2, 1, 6, 9],
            [5, 3, 1, 2, 7, 6, 9, 4, 8],
            [6, 4, 9, 1, 3, 8, 2, 7, 5],
            [8, 2, 7, 9, 4, 5, 6, 3, 1],
            [9, 6, 2, 5, 1, 4, 3, 8, 7],
            [1, 8, 5, 3, 6, 7, 4, 9, 2],
            [3, 7, 4, 8, 2, 9, 5, 1, 6],
        ]
        Solver().solve(board)
        self.assertEqual(board, expected)

    def test_solve_with_solvable_hard(self):
        """
        Test solve with an hard level puzzle
        """
        board = [
            [3, 0, 0, 0, 9, 0, 0, 6, 0],
            [7, 0, 0, 8, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [9, 0, 0, 0, 7, 0, 8, 0, 0],
            [0, 0, 0, 0, 5, 0, 4, 0, 0],
            [5, 7, 0, 0, 6, 0, 0, 0, 1],
            [1, 0, 0, 2, 0, 0, 3, 0, 0],
            [0, 0, 3, 9, 0, 0, 0, 0, 4],
            [0, 4, 5, 0, 0, 0, 0, 0, 0],
        ]

        expected = [
            [3, 1, 8, 5, 9, 4, 2, 6, 7],
            [7, 5, 6, 8, 2, 3, 1, 4, 9],
            [4, 2, 9, 6, 1, 7, 5, 3, 8],
            [9, 3, 1, 4, 7, 2, 8, 5, 6],
            [6, 8, 2, 1, 5, 9, 4, 7, 3],
            [5, 7, 4, 3, 6, 8, 9, 2, 1],
            [1, 9, 7, 2, 4, 6, 3, 8, 5],
            [2, 6, 3, 9, 8, 5, 7, 1, 4],
            [8, 4, 5, 7, 3, 1, 6, 9, 2],
        ]
        Solver().solve(board)
        self.assertEqual(board, expected)

    def test_solve_with_solvable_medium(self):
        """
        Test solve with an medium level puzzle
        """
        board = [
            [0, 0, 0, 4, 0, 6, 0, 0, 2],
            [8, 0, 0, 0, 5, 3, 1, 9, 0],
            [9, 0, 6, 0, 0, 8, 0, 0, 0],
            [6, 7, 0, 1, 8, 0, 0, 0, 9],
            [1, 0, 0, 0, 0, 0, 3, 7, 0],
            [0, 0, 8, 0, 0, 0, 5, 0, 0],
            [0, 8, 0, 0, 4, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 9, 0, 0, 0, 6, 1, 0],
        ]

        expected = [
            [5, 1, 7, 4, 9, 6, 8, 3, 2],
            [8, 2, 4, 7, 5, 3, 1, 9, 6],
            [9, 3, 6, 2, 1, 8, 7, 4, 5],
            [6, 7, 3, 1, 8, 5, 4, 2, 9],
            [1, 4, 5, 9, 6, 2, 3, 7, 8],
            [2, 9, 8, 3, 7, 4, 5, 6, 1],
            [3, 8, 1, 6, 4, 9, 2, 5, 7],
            [7, 6, 2, 5, 3, 1, 9, 8, 4],
            [4, 5, 9, 8, 2, 7, 6, 1, 3],
        ]
        Solver().solve(board)
        self.assertEqual(board, expected)

    def test_solve_with_solvable_easy(self):
        """
        Test solve with an easy level puzzle
        """
        board = [
            [3, 0, 0, 2, 0, 8, 7, 0, 0],
            [0, 5, 0, 0, 9, 6, 8, 3, 2],
            [0, 8, 0, 7, 0, 0, 0, 0, 6],
            [4, 1, 0, 0, 0, 0, 0, 7, 8],
            [0, 2, 0, 0, 7, 4, 5, 0, 0],
            [7, 0, 3, 1, 8, 5, 4, 0, 0],
            [0, 0, 2, 5, 3, 1, 0, 0, 4],
            [0, 3, 1, 6, 4, 0, 0, 5, 0],
            [0, 0, 9, 0, 0, 0, 6, 1, 0],
        ]

        expected = [
            [3, 9, 6, 2, 1, 8, 7, 4, 5],
            [1, 5, 7, 4, 9, 6, 8, 3, 2],
            [2, 8, 4, 7, 5, 3, 1, 9, 6],
            [4, 1, 5, 9, 6, 2, 3, 7, 8],
            [9, 2, 8, 3, 7, 4, 5, 6, 1],
            [7, 6, 3, 1, 8, 5, 4, 2, 9],
            [6, 7, 2, 5, 3, 1, 9, 8, 4],
            [8, 3, 1, 6, 4, 9, 2, 5, 7],
            [5, 4, 9, 8, 2, 7, 6, 1, 3],
        ]
        Solver().solve(board)
        self.assertEqual(board, expected)


if __name__ == "__main__":
    unittest.main()
