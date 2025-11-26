# Car-Park class
class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        print("Car-Park at", self.location, ", with", self.capacity, "bays.")
