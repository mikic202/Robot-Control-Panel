from DataManipuation.SensorReading import SensorReading
from typing import List, Dict


class ReadingsDataset:
    def __init__(self) -> None:
        self.data = {}

    def add_sensor_data(self, data: SensorReading):
        if data.angle not in self.data:
            self.data[data.angle] = []
        self.data[data.angle].append(data.value)

    def add_sensors_data(self, data: List[SensorReading]):
        [self.add_sensor_data(reading) for reading in data]

    def get_latest_data(self, data_horizon: int = 30) -> Dict[str, List[float]]:
        return {str(key): value[-data_horizon:] for key, value in self.data.items()}
