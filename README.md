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