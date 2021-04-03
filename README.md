# ECE140B Team Project: RUFF RIDERS
**The goal of this project is to make an IOT dog feeder.**

## Challenges
- making the website
- interfacing with the Arduinos
- pushing to the internet
- designing the feeder

** key features**
- feeding
- reading water levels
- reading heart beats
- way to find dog


## Design Considerations

- Should refrain from only marketing to dogs since a lot of people purchase these feeders for cats. It is possible that more feeders
 are purchased for cats than dogs since cats are thought to be low maintanence pets and are more likely to be left alone for long
 periods of time.
- Camera and sound system is needed to be competitive.
- Dogs are smart, and they hijack their food sometimes, since water is involved it must be in
a tip proof container. food should also be in tip proof container.
- Definitely don't want device ruined from a tip, use some physics to make it tip proof or make it emit a sound at an offensive 
 frequency upon an attempted tip. or both. a bunch of feeders were tipped over when a person testing them threw a 10 lb bag of food at the feeder.
- Bowl that pet eats from should be stainless steel.
- Food and water containers should be anti-microbial.
- Water dispensing should be automatic.
- Many devices have backup battery in case of power failure.
- Device should have the ability to provide a default feeding in the event that the owner loses internet connection
 at their location or the location of the feeder (for manual feeding setting).
- Containers that hold food should be fully detachable from the main unit and easy to clean. dishwasher safe would be good.
- It might be more efficient to make the water dispenser separate from the food dispenser and sell them as a set,
 since the complicated circuitry will be in the feeder it will be safer this way. Additionally, people could
 purchase them separately. 
- Might want to consider a simple interface that also allows the unit to work without wifi functionality, a simple
 digital clock with the ability to set a time could provide this functionality.
- Many feeders allow you to use wet or dry food
- 2 common complaints to be addresses are 
  - The dispenser gets jammed 
  - The feeder doesn't dispense the correct amount of food. Someone who tested a bunch of feeders finds that most of them dispensed too much food, which could lead to poor health. 

## Making the website
The website hasa splash page(optional), fake login page, and a dashboard
dashboard will have
- sensor status's
  - possible bpm chart of the last 24 hrs 
  - hydration level illustrated by javascript icon
  - food level
  - weight over time option?
  - gps tracking?
- option to manually feed

**required commands**
- post:  from user click         that the user has requested the dog be manually fed
- get:   from website on load    bpm data of last 24 hrs
- get:   from website on load    the water level
- get:   from website on load    the last time dog was fed
- get:   from website on load    ...


-after researching pros and cons of having an application, and considering our time frame, it is best to have
 the entire user experience contained on the website.
-provide fake login

-optional community part of the website for people to post cute pics
-website MUST be mobile friendly 
-since we are tracking the dog, functionality to alert the owner if the dog is doing something its not
 supposed to be doing so they can yell at it through the microphone on the feeder. Dogs have outstanding hearing so
 they will likely hear their owner even if they are kinda far from the feeder. Microphone is also good
 to encourage a shy dog to go to the feeder. Many feeders available have a function to record a voice message. laaaame. lets provide
 the microphone.
 
 ## making the backend  ##
 using the format of previous labs we will 
 recive post commands from the arduino to an adress on our website to recive data from it
 store that data somehow
 recieve a post command from the user to manually feed the dog
 store that and when a get command comes in from the arduino send the proper output to it to trigger the motors
 
 ** adresses required **
/login.html
/dashboard.html

** required commands **
- post:  that the user has requested the dog be manually fed
- get:   bpm data of last 24 hrs
- get    the water level
- get:   the last time dog was fed
- post:  water level
- post:  dog GPS
- get:   command to give food
 
## Connecting to Internet ##
** Hello World **
Purchase a domain name and upload a docker container to run a simple hello world file

**Tasks to Overcome**
-  Global hello world
-  buy Domain (complete)
-  make sure it is being hosted(complete)
-  load a docker container on the server that loads a helloworld.html to user
-  load Lab 2 from last quarter into container

** hello Doggo **
-load backend for current project onto live website
-make sure everything works



## Interfacing with Arduino  ##
The arduino will be posting sensor input at regular time intervals and making a get request every so often to decide if it is going to perform an action such as feeding the dog.
enable the set up of a manual feeding in the event of internet failure.

**Required Commands**
- post: every 5 minutes    water level
- post: every minute       dog GPS
- get:  every minute       command to give food

**Things to purchase**
- bowl
- motor with corkscrew for dispersing food
- 3d print?

**Useful Links**

- **WIFI Transceiver Buy Link**: https://www.amazon.com/HiLetgo-Wireless-Transceiver-Development-Compatible/dp/B010N1ROQS/ref=sr_1_3?dchild=1&keywords=arduino+wifi+module&qid=1617399917&sr=8-3

- **Arduino HTTP Request**: https://arduinogetstarted.com/tutorials/arduino-http-request

- **WIFI Sensor Tutorial**: https://www.youtube.com/watch?v=qU76yWHeQuw

- **Write POST to Server**: https://youtu.be/32VcKyI0dio

- **Eli Computer Guy**: https://www.elithecomputerguy.com/2019/07/write-post-data-to-server-with-arduino-uno-with-wifi/



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
