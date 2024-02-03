import unittest

from run import Run


class TestSolver(unittest.TestCase):

    def test_process_oneliner_with_valid_string(self):
        """
        Test that when run with oneliner with valid string
        """
        oneliner = "3,0,0,2,0,8,7,0,0,0,5,0,0,9,6,8,3,2,0,8,0,7,0,0,0,0,6,4,1,0,0,0,0,0,7,8,0,2,0,0,7,4,5,0,0,7,0,3,1,8,5,4,0,0,0,0,2,5,3,1,0,0,4,0,3,1,6,4,0,0,5,0,0,0,9,0,0,0,6,1,0"
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
        self.assertEqual((True, expected), Run().process_oneliner(oneliner))

    def test_process_oneliner_with_invalid_string(self):
        """
        Test that when run with oneliner with invalid string, not enough rows
        """
        oneliner = "3,0,0,2"
        self.assertRaisesRegex(
            RuntimeError,
            "Your oneliner input is not valid, you don't have 9 rows!",
            lambda: Run().process_oneliner(oneliner),
        )

    def test_process_oneliner_with_invalid_string(self):
        """
        Test that when run with oneliner with invalid string, not enough digits in a row
        """
        oneliner = "3,0,0,2,0,8,7,0,0,0,5,0,0,9,6,8,3,2,0,8,0,7,0,0,0,0,6,4,1,0,0,0,0,0,7,8,0,2,0,0,7,4,5,0,0,7,0,3,1,8,5,4,0,0,0,0,2,5,3,1,0,0,4,0,3,1,6,4,0,0,5,0,0,0,9,0,0,0"
        self.assertRaisesRegex(
            RuntimeError,
            "Your oneliner input is not valid, a row doesn't have 9 digits!",
            lambda: Run().process_oneliner(oneliner),
        )
