# ECE140B Team Project: RUFF RIDERS
**The goal of this project is to make an IOT dog feeder.**

## Challenges
- making the website
- interfacing with the Arduinos
- pushing to the internet


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

