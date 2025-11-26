#Imports
from sensor import Sensor
from display import Display

# Car-Park class
class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, displays=None, sensors=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []

    def __str__(self):
        print("Car-Park at", self.location, ", with", self.capacity, "bays.")

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
            