from UiRobotData import Ui_RobotDataWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from io import BytesIO
from DataReader import DataReader
from DataManipuation.SensorReading import SensorReading
from DataManipuation.ControlValue import ControlValue


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
        self.control_points = {}

    # def draw_plot(self, x, y):
    #     image_data = generate_plot(x, y)
    #     pixmap = QPixmap()
    #     if pixmap.loadFromData(image_data):
    #         self.ui.sensor_output.setPixmap(pixmap)

    def add_sensor_datpoint(self, datapoint: SensorReading):
        if datapoint.angle not in self.datapoints:
            self.datapoints[datapoint.angle] = []
        self.datapoints[datapoint.angle].append(datapoint.value)

    def add_control_datpoint(self, datapoint: ControlValue):
        if datapoint.controll_name not in self.control_points:
            self.control_points[datapoint.controll_name] = []
        self.control_points[datapoint.controll_name].append(datapoint.value)

    def draw_sensor_data(self, data):
        [self.add_sensor_datpoint(reading) for reading in data]
        image_data = generate_plots(
            range(len(list(self.datapoints.values())[0])),
            self.datapoints.values(),
            self.datapoints.keys(),
        )
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.ui.sensor_output.setPixmap(pixmap)

    def draw_control_data(self, data):
        [self.add_control_datpoint(reading) for reading in data]
        image_data = generate_plots(
            range(len(list(self.control_points.values())[0])),
            self.control_points.values(),
            self.control_points.keys(),
        )
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.ui.stearing.setPixmap(pixmap)


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
