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
import time
from functools import partial

from PySide6 import QtWidgets, QtCore
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice, QSize

from solver import Solver


class Gui:
    """
    All wrapper and GUI related functionality
    """

    def __init__(self, ui_file_name="qt_gui.ui", args=[]):
        """ "
        Parameters
        ----------
        ui_file_name : str, default='qt_gui.ui'
            Name of the Qt ui file to load and execute
        args: list, default=[]
            Arguments to pass into the Qt application object

        Raises
        ------
        RuntimeException
            If the `ui_file_name` does not exist or cannot be opened
        """
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
        """Return the list of all widgets within the QApplication

        Return
        ------
        list[QWidget]
            List of all the QWidget's within the application
        """
        return self.app.allWidgets()

    def get_all_widgets_by_type(self, widget_type):
        """Get all QWidgets of a certain QtWidget type in the application

        Processes via lambda and filters to return only `widget_type` instance type widgets

        Paramters
        ---------
        widget_type : QtWidget
            Type of widget to filter

        Return
        ------
        list[QWidget]
            Widgets that matched the `isinstance()` criteria
        """
        return list(
            filter(
                lambda widget: isinstance(widget, widget_type), self.get_all_widgets()
            )
        )

    def get_widget_by_type_and_name(self, name, widget_type):
        """Get all QWidgets of a certain QtWidget type with a certain name in the application

        Processes via lambda and filters to return only one `widget_type` instance type widgets
        that matches the `objectName()` on the widget

        Paramters
        ---------
        widget_type : QtWidget
            Type of widget to filter

        Return
        ------
        QWidget
            Widgets that matched the `isinstance()` and name criteria
        """
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
        """Get all QWidgets with a name that starts with `name` in the application

        Processes via lambda and filters to return only QWidgets that have an `objectName()`
        that starts with `name`

        Paramters
        ---------
        name : str
            Starting string of object name in QWidget

        Return
        ------
        list[QWidget]
            Widgets that object name start with `name`
        """
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
        """Get all QWidgets with a name that starts with `name` and are of type `widget_type`
        in the application

        Processes via lambda and filters to return only QWidgets that have an `objectName()`
        that starts with `name` and `isinstance()` of `widget_type`

        Paramters
        ---------
        name : str
            Starting string of object name in QWidget
        widget_type: QWidget
            QWidget type

        Return
        ------
        list[QWidget]
            Widgets that object name start with `name` and match `widget_type`
        """
        return (
            list(
                filter(
                    lambda widget: widget.objectName().startswith(name),
                    self.get_all_widgets_by_type(widget_type),
                )
            )
            or None
        )

    def load(self, window_size=(640, 560)):
        """Method to load the UI file and process 'precursor' setup such as binding buttons

        Parameters
        ----------
        window_size : tuple, default=(640, 470)
            Size of the window to generate when calling `self.run()`. Would advise not changing
            this, I didn't put much effort into anchors on the GUI design

        Raises
        ------
        RuntimeError
            If could not load UI file and/or instantiate the window
        """
        self.window = self.loader.load(self.ui_file)
        self.window.setFixedSize(QSize(*window_size))
        self.ui_file.close()

        if not self.window:
            raise RuntimeError(
                f"Window failed to instantiate with error [{self.loader.errorString()}]"
            )

        # Centre all QLineEdit boxes - dumb i know but gui editor is poop for it
        for box in self.get_all_widgets_by_type(QtWidgets.QLineEdit):
            box.setAlignment(QtCore.Qt.AlignCenter)
            box.setText(str(0))

        self.get_widget_by_type_and_name(
            "difficultySelectBox", QtWidgets.QComboBox
        ).addItem("Easy", 0.35)
        self.get_widget_by_type_and_name(
            "difficultySelectBox", QtWidgets.QComboBox
        ).addItem("Medium", 0.45)
        self.get_widget_by_type_and_name(
            "difficultySelectBox", QtWidgets.QComboBox
        ).addItem("Hard", 0.60)
        self.get_widget_by_type_and_name(
            "difficultySelectBox", QtWidgets.QComboBox
        ).addItem("Expert", 0.70)

        self.set_progress_bar_value(0)

        self.get_widget_by_type_and_name(
            "clearButton", QtWidgets.QPushButton
        ).clicked.connect(self.clear_board)
        self.get_widget_by_type_and_name(
            "newButton", QtWidgets.QPushButton
        ).clicked.connect(
            partial(self.generate_new_board, 0.5)  # TODO - add in game ease on gen
        )
        self.get_widget_by_type_and_name(
            "solveButton", QtWidgets.QPushButton
        ).clicked.connect(self.solve_board)
        self.get_widget_by_type_and_name(
            "inputButton", QtWidgets.QPushButton
        ).clicked.connect(self.handle_input_toggle)

    def handle_input_toggle(self):
        """Bound to the input button, handles updates to GUI to switch between `INPUT`
        and `GUIDED` mode

        `INPUT` - allows user to input into the cells the puzzle to be solved
        `GUIDED` - locks all cels and application will gen/input values to be solved
        """
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
            name="txt", widget_type=QtWidgets.QLineEdit
        )

        for square in board_squares:
            square.setReadOnly(read_only_value)

    def solve_board(self):
        """Bound to the `solve` button and does what it says on the tin

        Calls into the solver class and processes
        """
        print("SolveButton - Clicked")
        cpu_start_time = time.process_time()
        wall_start_time = time.time()

        self.get_widget_by_type_and_name("statusLabel", QtWidgets.QLabel).setText(
            "Solving..."
        )
        self.get_widget_by_type_and_name("timeLabel", QtWidgets.QLabel).setText(
            "Capturing..."
        )
        self.get_widget_by_type_and_name("operationsLabel", QtWidgets.QLabel).setText(
            "Adding..."
        )
        for button in self.get_all_widgets_by_type(QtWidgets.QPushButton):
            button.setEnabled(False)

        board = []
        board_valid = True
        for i in range(9):
            row = []
            for j in range(9):
                try:
                    row.append(int(self.get_board_value(i, j)))
                except ValueError:
                    board_valid = False
                    continue
            board.append(row)

        result = False
        solver = Solver()
        if board_valid:
            result = solver.solve(board, self)

        wall_end_time = time.time()
        cpu_end_time = time.process_time()

        cpu_time = cpu_end_time - cpu_start_time
        wall_time = wall_end_time - wall_start_time

        self.get_widget_by_type_and_name("timeLabel", QtWidgets.QLabel).setText(
            f"CPU={round(cpu_time, 2)}, Wall={round(wall_time, 2)}"
        )

        label_value = "Not Solvable"
        if result and board_valid:
            label_value = "Solved"
        elif not board_valid:
            label_value = "Invalid Board"

        self.get_widget_by_type_and_name("statusLabel", QtWidgets.QLabel).setText(
            label_value
        )
        self.get_widget_by_type_and_name("operationsLabel", QtWidgets.QLabel).setText(
            str(solver.operation_count)
        )

        for button in self.get_all_widgets_by_type(QtWidgets.QPushButton):
            button.setEnabled(True)

    def generate_new_board(self, game_ease=0.5):
        """Bound to the `generate` button and does what it says on the tin

        Will clear the cells, and generate a new puzzle with `game_ease` setting
        the level of masking i.e. how difficult to make it for a human to solve

        Parameters
        ----------
        game_ease : float
            How much of the generated board to hide, i.e. difficulty

        """
        print("NewButton - Clicked")
        # TODO - add
        self.set_board_values("0")
        self.get_widget_by_type_and_name("operationsLabel", QtWidgets.QLabel).setText(
            "0"
        )

        self.get_widget_by_type_and_name("statusLabel", QtWidgets.QLabel).setText(
            "Ready"
        )
        self.set_progress_bar_value(0)
        self.get_widget_by_type_and_name("timeLabel", QtWidgets.QLabel).setText("0")

    def run(self):
        """Brains of the operation, post load, this is executed to actually
        excute the application and display the window to the user

        Bound to `sys.exit()` on the QApplication execution signal
        """
        self.window.show()
        sys.exit(self.app.exec())

    def set_progress_bar_value(self, value):
        """Set the value for progress on the progress bar

        Parameters
        ----------
        value : int
            Value between 0 to 100
        """
        self.get_widget_by_type_and_name(
            "progressBar", QtWidgets.QProgressBar
        ).setValue(value)

        # Dirty hack to process gui updates
        self.app.processEvents()

    def set_board_value(self, row, column, value):
        """For given `row`, `column` set it to the value `value`

        Note - all zero-indexed i.e. 8 rows not 9

        Parameters
        ----------
        row : int
        column : int
        value : int
        """
        self.get_widget_by_type_and_name(
            f"txtRow{row}Col{column}", QtWidgets.QLineEdit
        ).setText(str(value))

        # Dirty hack to process gui updates
        self.app.processEvents()

    def get_board_value(self, row, column):
        """For given `row` and `column` get it's value

        Note - all zero-indexed i.e. 8 rows not 9

        Parameters
        ----------
        row : int
        column : int

        Return
        ------
        str
            Value of the cell, not always an int hence str
        """
        return self.get_widget_by_type_and_name(
            f"txtRow{row}Col{column}", QtWidgets.QLineEdit
        ).text()

    def set_board_values(self, value="0"):
        """Utility function to set all of the cells to a given `value`

        Parameters
        ----------
        value : str
            What to set the cell value to
        """
        board_squares = self.get_all_widgets_by_type_and_name_starting_with(
            name="txt", widget_type=QtWidgets.QLineEdit
        )

        for square in board_squares:
            square.setText(value)

    def clear_board(self):
        """Bound to the `clear` button, will set all of the cells to be blank"""
        self.set_board_values("")
        self.get_widget_by_type_and_name("statusLabel", QtWidgets.QLabel).setText(
            "Ready"
        )
        self.set_progress_bar_value(0)
        self.get_widget_by_type_and_name("timeLabel", QtWidgets.QLabel).setText("0")
        self.get_widget_by_type_and_name("operationsLabel", QtWidgets.QLabel).setText(
            "0"
        )
