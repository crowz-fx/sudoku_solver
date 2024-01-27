import sys

from functools import partial

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice, QSize


class Gui:
    def __init__(self, ui_file_name="qt_gui.ui", args=[]):
        self.ui_file_name = ui_file_name
        self.ui_file = QFile(self.ui_file_name)
        self.app = None
        self.loader = QUiLoader()
        self.app = QApplication(args)

        if not self.ui_file.open(QIODevice.ReadOnly):
            raise RuntimeException(
                f"Issue opening file [{self.ui_file_name}], with error [{self.ui_file.errorString()}]"
            )

    def get_all_widgets(self):
        return self.app.allWidgets()

    def get_all_widgets_by_type(self, widget_type):
        return list(
            filter(
                lambda widget: isinstance(widget, widget_type), self.get_all_widgets()
            )
        )

    def get_widget_by_type_and_name(self, name, widget_type):
        return (
            list(
                filter(
                    lambda widget: widget.objectName() == name,
                    self.get_all_widgets_by_type(widget_type),
                )
            )[0]
            or None
        )

    def get_all_widgets_by_name_starting_with(self, name):
        return (
            list(
                filter(
                    lambda widget: widget.objectName().startswith(name),
                    self.get_all_widgets(),
                )
            )
            or None
        )

    def get_all_widgets_by_type_and_name_starting_with(self, name, widget_type):
        return (
            list(
                filter(
                    lambda widget: widget.objectName().startswith(name),
                    self.get_all_widgets_by_type(widget_type),
                )
            )
            or None
        )

    def load(self, window_size=(640, 470)):
        self.window = self.loader.load(self.ui_file)
        self.window.setFixedSize(QSize(*window_size))
        self.ui_file.close()

        if not self.window:
            raise RuntimeError(
                f"Window failed to instantiate with error [{self.loader.errorString()}]"
            )

        self.get_widget_by_type_and_name(
            "clearButton", QtWidgets.QPushButton
        ).clicked.connect(self.clear_board)
        self.get_widget_by_type_and_name(
            "newButton", QtWidgets.QPushButton
        ).clicked.connect(
            partial(self.set_board_values, "X")
        )  # TODO - change
        self.get_widget_by_type_and_name(
            "solveButton", QtWidgets.QPushButton
        ).clicked.connect(self.solve_board)
        self.get_widget_by_type_and_name(
            "inputButton", QtWidgets.QPushButton
        ).clicked.connect(self.handle_input_toggle)

    def handle_input_toggle(self):
        print("InputButton - Clicked")
        button_value = self.get_widget_by_type_and_name(
            "inputButton", QtWidgets.QPushButton
        ).text()

        read_only_value = False

        if button_value == "INPUT":
            read_only_value = False
            button_value = "GUIDED"
        else:
            read_only_value = True
            button_value = "INPUT"

        # Now set all text boxes to input enabled
        self.get_widget_by_type_and_name("inputButton", QtWidgets.QPushButton).setText(
            button_value
        )

        board_squares = self.get_all_widgets_by_type_and_name_starting_with(
            name="txt", widget_type=QtWidgets.QPlainTextEdit
        )

        for square in board_squares:
            square.setReadOnly(read_only_value)

    def solve_board(self):
        print("SolveButton - Clicked")
        # TODO - add

    def generate_new_board(self, game_ease=0.5):
        print("NewButton - Clicked")
        # TODO - add

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())

    def set_board_value(self, row, column, value):
        self.get_widget_by_type_and_name(
            f"txtRow{row}Col{column}", QtWidgets.QPlainTextEdit
        ).setPlainText(value)

    def get_board_value(self, row, column):
        return self.get_widget_by_type_and_name(
            f"txtRow{row}Col{column}", QtWidgets.QPlainTextEdit
        ).getPlainText()

    def set_board_values(self, value="0"):
        board_squares = self.get_all_widgets_by_type_and_name_starting_with(
            name="txt", widget_type=QtWidgets.QPlainTextEdit
        )

        for square in board_squares:
            square.setPlainText(value)

    def clear_board(self):
        print("clicked clear")
        self.set_board_values("")
