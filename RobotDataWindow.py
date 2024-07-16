from UiRobotData import Ui_RobotDataWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from io import BytesIO


def generate_plot(x, y):
    plt.plot(x, y)
    buffor = BytesIO()
    plt.savefig(buffor, format="png")
    return buffor.getvalue()


class RobotDataWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RobotDataWindow()
        self.ui.setupUi(self)
        self.draw_plot([1, 2, 3], [1, 2, 3])

    def draw_plot(self, x, y):
        image_data = generate_plot(x, y)
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.ui.sensor_output.setPixmap(pixmap)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = RobotDataWindow()
    window.show()
    sys.exit(app.exec_())
