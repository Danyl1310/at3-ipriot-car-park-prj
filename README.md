# AT3 IP4RIoT Car-Park PRJ
*Daniel Cummings*  
26/11/2025
## Prototype Smart Parking Solution
This project is for the design and creation of a smart parking system, with 
the aim to reduce traffic and enhance the parking experience. The parking system
will use sensors and have displays that provide weather updates and other relevant
information such as community messages.  

Link to used guide: [Guide-Link](https://github.com/NM-TAFE/civ-ipriot-in-class-demos/blob/main/assessments/prj/carpark-guide.md)

## Initial Commit
screenshot of GitHub after the first push:  

![Initial commit](screenshots/Image-of-GitHub-after-first-push.png)

## Second Commit
The implementation of stubs for classes:  

![Stubs for classes](/screenshots/Stubs-for-classes.png)

## Proof of Git tags
Screenshot of the ```Git tag``` command in Git Bash.  

![Git tags](/screenshots/Image-of-git-tags.png)

## Class Responsibilities question

> Q. Which class is responsible for the number of available bays (and why)?  
> The class which is responsible for the number of available bays is the car park
> class since it represents the physical car park which physically contains available bays.

>Q. Which class is responsible for the current temperature (and why)?  
I believe the sensor class or at-least a subclass of class sensor should be responsible
> for the current temperature value because it just makes sense that a sensor is able
> to measure the temperature.  

>Q. Which class is responsible for the time (and why)?
> I believe the car park class should also be responsible for the time because it is the main
> class and can forward the current time to all individual displays.

![Added methods to car park class](/screenshots/Git-Repository-With-Tags.png)

>Review Questions:
>1. Which class is responsible for each of the following pieces of information (and why)?
>   * The number of available bays: ```Only the car park class can be responsible for the number of available bays since it is the only class which can contain the virtual property "available_bays()" which is calculated from the attributes of capacity and list of plates.```  
>   * The current temperature: ```The carpark class is also responsible for holding the value for the current temperature since it needs to send or forward the information to all the displays in its attribute list of displays.```
>   * The time: ```The time should also be stored in the car park class to forward to each display.```
>2. What's the difference between an attribute and a property?  
>```The term attribute, refers to regular attributes like "self.location" in the carpark class. A property refers to a special attribute, called virtual attributes, an example of a virtual attribute is: "available_bays()" in the carpark class, which has the @property decorator, the attribute in the example is different to a normal attribute since it encapsulates the values and the calculations used to get the value it returns.```
>3. Why do you think we used a dictionary to hold the data we passed the display? List at least one advantage and one disadvantage of this approach.  
>```I think a dictionary was used to pass the data since it is easier to pass multiple values as one single item but a disadvantage is that the dictionary must contain both values whenever new values need to be added. and any extra information cannot be added```