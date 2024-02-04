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

import signal
from pprint import pprint

from args import Args
from run import Run
from file import FileUtils


args = Args.process()

if __name__ == "__main__":
    # Nasty but when ctrl+c on cmdline then kill the whole thing
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    if hasattr(args, "gui"):
        print(f"GUI - [{args.gui}]")
        from gui import Gui

        gui = Gui(ui_file_name="qt_gui.ui")

        gui.load()
        gui.run()
    else:
        result = False
        final_board = []
        output = args.output

        if hasattr(args, "oneliner"):
            print(f"OneLiner=[{args.oneliner}], Output=[{output}]")
            result, final_board = Run().process_oneliner(args.oneliner)

        elif hasattr(args, "file"):
            print(f"File=[{args.file}], Output=[{output}]")
            result, final_board = Run().process_file(args.file)

        print(f"Solved? - {result}")
        if output == "file":
            file_contents = []
            file = "output.txt"

            for board_row in final_board:
                file_contents.append(",".join(map(str, board_row)))
                file_contents.append("\n")

            FileUtils.write_file(file, file_contents)
            print(f"Output written to file [{file}]")
        else:
            pprint(final_board)
