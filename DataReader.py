from typing import List
from DataManipuation.SensorReading import SensorReading
from DataManipuation.ControlValue import ControlValue
from random import random
import socket
import json

HOST = "localhost"
SENSOR_DATA_PORT = 65432


class DataReader:
    def __init__(self) -> None:
        self.sensor_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sensor_server.bind((HOST, SENSOR_DATA_PORT))
        self.sensor_server.listen()
        self.sensor_connection, _ = self.sensor_server.accept()

    def read_sensor_data(self) -> List[SensorReading]:
        request = self.sensor_connection.recv(1024)
        request = request.decode("utf-8")
        readings = []
        for json_reading in json.loads(request):
            readings.append(SensorReading(json_reading["angle"], json_reading["value"]))
        return readings

    def read_control_values(self) -> List[ControlValue]:
        return [ControlValue("control", 0.5)]
