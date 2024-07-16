from UiRobotData import Ui_RobotDataWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from io import BytesIO
from DataReader import DataReader
from SensorReading import SensorReading


def generate_plots(x, y, labels):
    plt.clf()
    for y_val, label in zip(y, labels):
        print(x, label)
        plt.plot(x, y_val, label=label)
    # plt.plot(x, y)
    buffor = BytesIO()
    plt.savefig(buffor, format="png")
    return buffor.getvalue()


class RobotDataWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RobotDataWindow()
        self.ui.setupUi(self)
        # self.draw_plot([1, 2, 3], [1, 2, 3])
        self.datapoints = {}

    # def draw_plot(self, x, y):
    #     image_data = generate_plot(x, y)
    #     pixmap = QPixmap()
    #     if pixmap.loadFromData(image_data):
    #         self.ui.sensor_output.setPixmap(pixmap)

    def add_datpoint(self, datapoint: SensorReading):
        if datapoint.angle not in self.datapoints:
            self.datapoints[datapoint.angle] = []
        self.datapoints[datapoint.angle].append(datapoint.value)

    def draw_sensor_data(self, data):
        [self.add_datpoint(reading) for reading in data]
        image_data = generate_plots(
            range(len(list(self.datapoints.values())[0])),
            self.datapoints.values(),
            self.datapoints.keys(),
        )
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.ui.sensor_output.setPixmap(pixmap)

    def draw_control_data(self, data):
        # [self.datapoints.append(reading) for reading in data]
        pass


def gui_main(args):
    app = QApplication(args)
    window = RobotDataWindow()
    window.show()
    reader = DataReader()

    while window.isVisible():
        window.draw_sensor_data(reader.read_sensor_data())
        window.draw_control_data(reader.read_control_values())
        app.processEvents()


if __name__ == "__main__":
    gui_main(sys.argv)
