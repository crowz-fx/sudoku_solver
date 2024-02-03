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

from argparse import ArgumentParser


class Args:
    """
    Program execution argument handling
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def process():
        """Validate and process application execution arguments

        @staticmethod

        Returns
        -------
        Namespace
            Processed arguments (basically a dict)
        """
        parser = ArgumentParser(
            description="Sudoku Solver - input or generate a puzzle and then have it be automagically solved!"
        )
        subparsers = parser.add_subparsers(title="Modes")

        gui_parser = subparsers.add_parser("gui", help="use the PyQt GUI")
        gui_parser.set_defaults(gui=True)

        headless_parser = subparsers.add_parser(
            "headless", help="run solely in command prompt"
        )

        subparsers = headless_parser.add_subparsers(title="Headless", required=True)
        headless_parser.add_argument(
            "-o",
            "--output",
            dest="output",
            help="if headless, output to stdout or file",
            metavar="<stdout|file>",
            required=False,
            default="stdout",
            choices=("stdout", "file"),
        )

        headless_oneliner_parser = subparsers.add_parser(
            "oneliner", help="input puzzle as oneliner on command line"
        )
        headless_oneliner_parser.add_argument(
            "oneliner",
            help="puzzle onliner in csv format, 0 = unknown",
            metavar="0,1,9,3,0...",
        )

        headless_file_parser = subparsers.add_parser(
            "file", help="input puzzle as file"
        )
        headless_file_parser.add_argument(
            "file",
            help="path to file that contains puzzle",
            metavar="puzzle.txt",
        )

        return parser.parse_args()
