# Planning for classes

```mermaid
classDiagram
    
class Carpark {
    +String location
    +Int Capacity
    +List[plates]
    +List[displays]
    +addCar()
    +removeCar()
    +updateDisplays(plate)
    +updateDisplaycMsg(message)
    
}

class Display {
    +String cmessage
    +String message
    +Bool is_on
    +updateDisplay()
    +updateCmessage()
}

class Sensor {
    +String id
    +Bool is-active
    +sensePlate()
    +updateCpark(plate)
}
Sensor <|.. Entrysensor
Sensor <|.. Exitsensor
Carpark *-- Display
Carpark <-- Sensor

```