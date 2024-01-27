from gui import Gui

if __name__ == "__main__":
    gui = Gui(ui_file_name="qt_gui.ui")

    gui.load()
    gui.run()
