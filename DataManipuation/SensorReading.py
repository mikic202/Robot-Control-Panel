from dataclasses import dataclass


@dataclass
class SensorReading:
    angle: float
    value: float
