from UiRobotData import Ui_RobotDataWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import matplotlib.pyplot as plt


class RobotDataWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RobotDataWindow()
        self.ui.setupUi(self)

    def


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = RobotDataWindow()
    window.show()
    sys.exit(app.exec_())
