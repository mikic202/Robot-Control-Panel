from typing import List
from SensorReading import SensorReading
from ControlValue import ControlValue


class DataReader:
    def __init__(self) -> None:
        pass

    def read_sensor_data() -> List[SensorReading]:
        return [SensorReading(0, 0), SensorReading(1, 1), SensorReading(2, 2)]

    def read_control_values() -> List[ControlValue]:
        return [ControlValue("control", 0.5)]
