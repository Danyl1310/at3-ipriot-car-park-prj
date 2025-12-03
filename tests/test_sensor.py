# Imports
import unittest
from sensor import EntrySensor
from sensor import ExitSensor
from car_park import CarPark


# Test Sensor Class
class TestSensor(unittest.TestCase):
    def setUp(self):
        # car park
        self.car_park1 = CarPark()
        # entry sensor
        self.entry_sensor = EntrySensor(id=1, car_park=self.car_park1, is_active=True)
        # exit sensor
        self.exit_sensor = ExitSensor(id=1, car_park=self.car_park1, is_active=True)

    # Test entry sensor
    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, True)

    def test_entry_sensor_detect_car(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park1.plates), 1)

    # Test exit sensor
    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 1)
        self.assertEqual(self.exit_sensor.is_active, True)

    def test_exit_sensor_detect_car(self):
        self.car_park1.plates.append("12345a")
        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park1.plates), 0)
