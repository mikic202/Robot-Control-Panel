from typing import List
from SensorReading import SensorReading
from ControlValue import ControlValue
from random import random


class DataReader:
    def __init__(self) -> None:
        pass

    def read_sensor_data(self) -> List[SensorReading]:
        return [SensorReading(0, 0), SensorReading(1, random()), SensorReading(2, 2)]

    def read_control_values(self) -> List[ControlValue]:
        return [ControlValue("control", 0.5)]
