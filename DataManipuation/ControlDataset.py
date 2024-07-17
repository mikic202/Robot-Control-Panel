from DataManipuation.ControlValue import ControlValue
from typing import List, Dict


class ControlDataset:
    def __init__(self) -> None:
        self.data = {}

    def add_control_data(self, data: ControlValue):
        if data.controll_name not in self.data:
            self.data[data.controll_name] = []
        self.data[data.controll_name].append(data.value)

    def add_controls_data(self, data: List[ControlValue]):
        [self.add_control_data(reading) for reading in data]

    def get_latest_data(self, data_horizon: int = 30) -> Dict[str, List[float]]:
        return {str(key): value[-data_horizon:] for key, value in self.data.items()}
