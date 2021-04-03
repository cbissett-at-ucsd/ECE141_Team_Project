# ECE140B Team Project: RUFF RIDERS
**The goal of this project is to make an IOT dog feeder.**

## Challenges
- making the website
- interfacing with the Arduinos
- pushing to the internet
- designing the feeder

## Design Considerations

-should refrain from only marketing to dogs since a lot of people purchase these feeders for cats. It is possible that more feeders
 are purchased for cats than dogs since cats are thought to be low maintanence pets and are more likely to be left alone for long
 periods of time.
-camera and sound system is needed to be competitive.
-dogs are smart and they hijack their food sometimes, since water is involved it must be in
a tip proof container. food should also be in tip proof container.
-definitely don't want device ruined from a tip, use some physics to make it tip proof or make it emit a sound at an offensive 
 frequency upon attempted tip. or both. a bunch of feeders were tipped over when a person testing them threw a 10 lb bag of food at the feeder.
-bowl that pet eats from should be stainless steel.
-food and water containers should be anti microbial.
-water dispensing should be automatic.
-many devices have backup battery in case of power failure.
-device should have the ability to provide a default feeding in the event that the owner loses internet connection
 at their location or the location of the feeder (for manual feeding setting).
-containers that hold food should be fully detachable from the main unit and easy to clean. dishwasher safe would be good.
-it might be more efficient to make the water dispenser separate from the food dispenser and sell them as a set,
 since the complicated circuitry will be in the feeder it will be safer this way. Additionally, people could
 purchase them separately.
 -might want to consider simple interface that also allows the unit to work without wifi functionality, a simple
 digital clock with the ability to set a time could provide this functionality.
 -many feeders allow you to use wet or dry food
 -2 common complaints to be addresses are 1) the dispenser gets jammed and 2) the feeder doesnt dispense the correct amount of food. Someone
  who tested a bunch of feeders found that most of them dispensed too much food, which could lead to poor health. 

## Making the website
We need to make a functional website features
- dog weight monitoring
- water and food consumption charts
- feed now button
- set up automatic feeding times
- sql? text file?
- GPS
  - requesting maps from google api?
  - just put a relative location to the home
  - heart monitor tracking
  - heart beat throughout day 
  - indicator that its healthy
-after researching pros and cons of having an application, and considering our time frame, it is best to have
 the entire user experience contained on the website.
-provide login for security and customized experience
-enable the set up of a default feeding in the event of internet failure.
-optional community part of the website for people to post cute pics
-website MUST be mobile friendly 
-since we are tracking the dog, functionality to alert the owner if the dog is doing something its not
 supposed to be doing so they can yell at it through the microphone on the feeder. Dogs have outstanding hearing so
 they will likely hear their owner even if they are kinda far from the feeder. Microphone is also good
 to encourage a shy dog to go to the feeder. Many feeders available have a function to record a voice message. laaaame. lets provide
 the microphone.

## Interfacing with Arduino

**Useful Links**

- **WIFI Transceiver Buy Link**: https://www.amazon.com/HiLetgo-Wireless-Transceiver-Development-Compatible/dp/B010N1ROQS/ref=sr_1_3?dchild=1&keywords=arduino+wifi+module&qid=1617399917&sr=8-3

- **Arduino HTTP Request**: https://arduinogetstarted.com/tutorials/arduino-http-request

- **WIFI Sensor Tutorial**: https://www.youtube.com/watch?v=qU76yWHeQuw

- **Write POST to Server**: https://youtu.be/32VcKyI0dio

- **Eli Computer Guy**: https://www.elithecomputerguy.com/2019/07/write-post-data-to-server-with-arduino-uno-with-wifi/

**Commands required on Website**
- post-water level
- post-dog GPS
- get-command to give food

**Things to purchase**
- bowl
- motor with corkscrew for dispersing food
- 3d print?
may need to make a debugging page that displays text of whatever was posted last

## Connecting to Internet
### Hello World 
Purchase a domain name and upload a docker container to run a simple hello world file

**Tasks to Overcome**
-  Global hello world
-  buy Domain
   - possible website names
   - notramsin.com
   - ramsin.tech
   - ECE141RuffRiders.com
-  load files
-  run docker container on server
-  fix python code to work with internet

### Hello Webserving
Try and load assignment two on the server and change the domain adresses to get the thing to work
may have to switch to a different serving program that has better tutorials

- load files
- adjust links in the python files
- figure out problems?

## Possible Sensors to be used
### Water Level Sensor
- **Tutorial**: https://www.youtube.com/watch?v=n7WRi5U5lQk
- **Buy Link**: https://www.amazon.com/Sensor-Module-Detection-Surface-Arduino/dp/B01N058HS6/ref=asc_df_B01N058HS6/?tag=hyprod-20&linkCode=df0&hvadid=198091640568&hvpos=&hvnetw=g&hvrand=7398691741834090910&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061191&hvtargid=pla-350450658191&psc=1

### Distance Sensor
- **Tutorial**: 
  - https://www.tutorialspoint.com/arduino/arduino_ultrasonic_sensor.htm
  - https://www.youtube.com/watch?v=ZejQOX69K5M
- **Buy Link**: https://www.amazon.com/SainSmart-HC-SR04-Ranging-Detector-Distance/dp/B004U8TOE6/ref=asc_df_B004U8TOE6/?tag=hyprod-20&linkCode=df0&hvadid=312127837151&hvpos=&hvnetw=g&hvrand=16617634376972589103&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061191&hvtargid=pla-459285090715&psc=1&tag=&ref=&adgrpid=57636291530&hvpone=&hvptwo=&hvadid=312127837151&hvpos=&hvnetw=g&hvrand=16617634376972589103&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061191&hvtargid=pla-459285090715

### Arduino GPS Module
- **Tutorial**: 
  - https://create.arduino.cc/projecthub/amalmathewtech/arduino-gps-module-destination-notifier-288a55
  - https://www.youtube.com/watch?v=q2llnFjRSxk
- **Buy Link**: https://www.amazon.com/Navigation-Positioning-Microcontroller-Compatible-Sensitivity/dp/B084MK8BS2/ref=asc_df_B084MK8BS2/?tag=hyprod-20&linkCode=df0&hvadid=416672656770&hvpos=&hvnetw=g&hvrand=11803108201460712897&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061191&hvtargid=pla-906486472275&psc=1&tag=&ref=&adgrpid=95587149724&hvpone=&hvptwo=&hvadid=416672656770&hvpos=&hvnetw=g&hvrand=11803108201460712897&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061191&hvtargid=pla-906486472275
