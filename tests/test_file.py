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

import unittest

from file import FileUtils


class TestFileUtils(unittest.TestCase):

    def test_read_file_with_valid_file(self):
        """
        test that when run with valid file, it reads
        """
        file_name = "tests/test_file_read.txt"
        self.assertEqual(["cheese"], FileUtils.read_file(file_name))

    def test_read_file_with_file_not_found(self):
        """
        test that when run with file that doesn't exist, raises error
        """
        file_name = "tests/test_file_cheeeeeeeese.txt"
        self.assertRaisesRegex(
            FileNotFoundError,
            f"No such file or directory: '{file_name}'",
            lambda: FileUtils.read_file(file_name),
        )

    def test_write_file_with_contents(self):
        """
        test that when run with valid contents, file is written
        """
        file_name = "tests/test_file_output.txt"
        file_contents = ["chicken"]

        FileUtils.write_file(file_name, file_contents)

        self.assertEqual(file_contents, FileUtils().read_file(file_name))
