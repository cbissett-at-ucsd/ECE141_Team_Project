# ECE141_Team_Project
the goal of this project is to make an IOT dog feeder.

Challenges
-making the website
-interfaceing with the arduinos
-pushing to the internet


## making the website
we need to make a functional website
features
-dog weight monitoring
-water and food consumption charts
-feed now button
-set up automatic feeding times
    - sql? text file?
-GPS
   - requesting maps from google api?
   - just put a realitive location to the home
- heart monitor tracking
  -heart beat throughout day
  -indicator that its healthy


## interfacing with arduino

https://arduinogetstarted.com/tutorials/arduino-http-request

commands required on website
post-water level
post-dog GPS
get-command to give food

things to purchase
bowl
motor with corkscrew for dispersing food
  - 3d print?
may need to make a debugging page that displays text of whatever was posted last

## connecting to internet
### hello world 
Purchase a domain name and upload a docker container to run a simple hello world file

tasks to overcome
-  global hello world
  -  buy Domain
    -  possible website names
      - notramsin.com
      - ramsin.tech
      - ECE141RuffRiders.com
  -  load files
  -  run docker container on server
  -  fix python code to work with internet

### hello webserving
try and load assignment two on the server and change the domain adresses to get the thing to work
may have to switch to a different serving program that has better tutorials

-load files
-adjust links in the python files
-figure out problems?
