from argparse import ArgumentParser

parser = ArgumentParser(
    description="Sudoku Solver - input or generate a puzzle and then have it be automagically solved!"
)
subparsers = parser.add_subparsers(title="Modes")

gui_parser = subparsers.add_parser("gui", help="use the PyQt GUI")
gui_parser.set_defaults(gui=True)

headless_parser = subparsers.add_parser("headless", help="run solely in command prompt")

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
    "oneliner", help="puzzle onliner in csv format, 0 = unknown", metavar="0,1,9,3,0..."
)

headless_file_parser = subparsers.add_parser("file", help="input puzzle as file")
headless_file_parser.add_argument(
    "file",
    help="path to file that contains puzzle",
    metavar="puzzle.txt",
)

args = parser.parse_args()

if __name__ == "__main__":
    if hasattr(args, "gui"):
        from gui import Gui

        print(f"GUI - [{args.gui}]")

        gui = Gui(ui_file_name="qt_gui.ui")

        gui.load()
        gui.run()
    elif hasattr(args, "oneliner"):
        print(f"OneLiner=[{args.oneliner}], Output=[{args.output}]")
    elif hasattr(args, "file"):
        print(f"File=[{args.file}], Output=[{args.output}]")
