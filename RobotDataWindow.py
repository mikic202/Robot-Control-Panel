from UiRobotData import Ui_RobotDataWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
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
        self._readings_to_display = []

    def _readings_range_changed(self, value: int):
        self._readings_range = value

    def _create_readings_checkboxes(self, readings):
        for i in reversed(range(self.ui.readings_checkbox.count())):
            self.ui.readings_checkbox.itemAt(i).widget().setParent(None)
        for i, reading in enumerate(readings):
            self._readings_to_display.append(reading)
            checkbox = QCheckBox(str(reading))
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(
                lambda _, name=reading: (
                    self._readings_to_display.remove(name)
                    if name in self._readings_to_display
                    else self._readings_to_display.append(name)
                )
            )
            self.ui.readings_checkbox.addWidget(checkbox, i)

    def _draw_graph_from_dict(self, data: dict, canvas):
        image_data = generate_plots(
            range(len(list(data.values())[0])),
            data.values(),
            data.keys(),
        )

        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            canvas.setPixmap(pixmap)

    def draw_sensor_data(self, data):
        self.sensor_readings.add_sensors_data(data)
        latest_readings = self.sensor_readings.get_latest_data(self._readings_range)
        if len(latest_readings) == 0 or latest_readings is None:
            return

        readings_to_display_dict = {}

        for reading in latest_readings:
            if reading in self._readings_to_display:
                readings_to_display_dict[reading] = latest_readings[reading]

        if len(readings_to_display_dict) != 0:
            self._draw_graph_from_dict(readings_to_display_dict, self.ui.sensor_output)

        if self.ui.readings_checkbox.count() != len(latest_readings.keys()):
            self._create_readings_checkboxes(latest_readings.keys())

    def draw_control_data(self, data):
        self.control_points.add_controls_data(data)
        latest_control_points = self.control_points.get_latest_data(
            self._readings_range
        )
        self._draw_graph_from_dict(latest_control_points, self.ui.stearing)


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
