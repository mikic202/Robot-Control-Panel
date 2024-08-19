from UiRobotData import Ui_RobotDataWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from io import BytesIO
from DataReader import DataReader
from DataManipuation.SensorReading import SensorReading
from DataManipuation.ControlValue import ControlValue
from DataManipuation.ReadingsDataset import ReadingsDataset
from DataManipuation.ControlDataset import ControlDataset


def generate_plots(x, y, labels):
    plt.clf()
    for y_val, label in zip(y, labels):
        plt.plot(x, y_val, label=label)

    plt.legend(labels)
    buffor = BytesIO()
    plt.savefig(buffor, format="png")
    return buffor.getvalue()


class RobotDataWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RobotDataWindow()
        self.ui.setupUi(self)
        self.sensor_readings = ReadingsDataset()
        self.control_points = ControlDataset()
        self._readings_range = 30
        self.ui.ReadingsNumber.valueChanged.connect(self._readings_range_changed)
        self.ui.ReadingsNumber.setValue(self._readings_range)
        self.ui.ReadingsNumber.setMinimum(1)

    def _readings_range_changed(self, value: int):
        self._readings_range = value

    def draw_sensor_data(self, data):
        self.sensor_readings.add_sensors_data(data)
        latest_readings = self.sensor_readings.get_latest_data(self._readings_range)
        if len(latest_readings) == 0 or latest_readings is None:
            return
        image_data = generate_plots(
            range(len(list(latest_readings.values())[0])),
            latest_readings.values(),
            latest_readings.keys(),
        )

        self.ui.sensors.clear()
        for reading in latest_readings:
            self.ui.sensors.addItem(f"{reading}: {latest_readings[reading][-1]}")

        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.ui.sensor_output.setPixmap(pixmap)

    def draw_control_data(self, data):
        self.control_points.add_controls_data(data)
        latest_control_points = self.control_points.get_latest_data(
            self._readings_range
        )
        image_data = generate_plots(
            range(len(list(latest_control_points.values())[0])),
            latest_control_points.values(),
            latest_control_points.keys(),
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
        app.processEvents()
        window.draw_sensor_data(reader.read_sensor_data())
        window.draw_control_data(reader.read_control_values())


if __name__ == "__main__":
    gui_main(sys.argv)
