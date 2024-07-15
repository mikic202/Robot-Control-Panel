from UiRobotData import Ui_RobotDataWindow
import sys
from PySide2.QtWidgets import QApplication, QMainWindow


class RobotDataWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RobotDataWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = RobotDataWindow()
    window.show()
    sys.exit(app.exec_())