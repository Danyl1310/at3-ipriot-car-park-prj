# Display class
class Display:
    def __init__(self, id, message="", cmessage="", is_on=False):
        self.id = id
        self.message = message
        self.cmessage = cmessage
        self.is_on = is_on

    def __str__(self):
        print("Display", self.id + ": Welcome to the car park.")
