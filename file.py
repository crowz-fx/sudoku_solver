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

import sys


class FileUtils:
    """
    Collection of file utility functions
    """

    def __init__(self) -> None:
        """"""
        pass

    @staticmethod
    def write_file(file_name, file_contents):
        """Takes contents input and writes out to specified file

        Parameters
        ----------
        file_name : str
          Relative path and name of file to write to
        file_contents : list[str]
          Contents, already formatted to write to file

        Raises
        ------
        Exception
          Generic exception if something unexpected happens like file-system un-writable
        """
        try:
            with open(file_name, "w") as file:
                file.writelines(file_contents)
        except Exception as error:
            print(f"Error occured writing to file [{file_name}]")
            raise

    @staticmethod
    def read_file(file_name, open_mode="r"):
        """Reads the contents of file_name and returns

        Parameters
        ----------
        file_name : str
          Relative path and name of file to read
        open_mode : str
          Attribute for opening the file

        Returns
        -------
        str
          Contents of file

        Raises
        ------
        FileNotFoundError
          If file cant not be found or opened

        """
        try:
            with open(file_name, open_mode) as file:
                file_contents = file.readlines()
            return file_contents
        except FileNotFoundError as error:
            print(f"Dude, where the f is the file [{file_name}]?")
            raise
