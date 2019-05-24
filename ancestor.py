# BUILD USING PYTHON 3

import time
import gopigo3
from di_sensors.easy_distance_sensor import EasyDistanceSensor
from di_sensors.inertial_measurement_unit import InertialMeasurementUnit

class MrA(gopigo3.GoPiGo3):

    def __init__(self):
        super().__init__()
        self.imu = InertialMeasurementUnit(bus = "GPG3_AD1") 
        self.ds = EasyDistanceSensor()

    def dist(self):
        num = self.ds.read()
        print("distance from object: {} mm".format(num))
        return num

    def angle(self):
        num = self.imu.read_euler()[0]
        print("currently facing angle: {} deg".format(num))
        return num





    