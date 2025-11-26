# Sensor class
class Sensor:
    def __init__(self, id, is_active=False):
        self.id = id
        self.is_active = is_active

    def __str__(self):
        print("Sensor", self.id + ": Status-", "Offline" if self.is_active is False else "Online")


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass
