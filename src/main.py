from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

CarPark1 = CarPark(location="moondalup", capacity=100, log_file="moondalup.txt")
CarPark1.write_config("moondalup_config")
CarPark1.from_config(config_file="moondalup_config.json")
EntrySensor1 = EntrySensor(id=1, is_active=True, car_park=CarPark1)
ExitSensor1 = ExitSensor(id=2, is_active=True, car_park=CarPark1)
Display1 = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=CarPark1)
for cars in range(10):
    EntrySensor1.detect_vehicle()
for cars in range(2):
    ExitSensor1.detect_vehicle()

