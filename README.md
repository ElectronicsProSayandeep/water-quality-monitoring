# water-quality-system by TechPandits

What do we want to achieve with this project:
With this system we intend to measure various water quality parameters such as
pH, Turbidity, TDS, Temperature(and more sensors be added). This is measured by 
the hardware unit of the project. Many such hardware units are deployed on a large
water body to continously monitor its quality. The software collects the reading
and stores it in a database. The database can then be accessed to predict any
anomalous behaviour using Machine Learning and hence give an advanced warning.

But why measure water quality:
With increased demand on water supply due to ever increasing population, quality
of water has been neglected since long. Forms of pollution such as air and land
is very much visible to common public and hence measures are taken as soon as
abnormality surfaces. But in case of water, which need not be visible can 
deteriorate due to invisible minerals and also hot water discharge which heavily
impacts the aquatic life in the water body and also people living nearby. Hence
it is becoming increasingly important to measure water quality so that measures
can be taken to curb water pollution.

Current status of project:
The project has is completed till the basic functionality to realise its
potential of a single unit of the network. The GUI, along with the graphs can 
display status of water and also predict the possible future values of water
quality parameters.

What more needs to be done to make this project a success:
A battery pack and renewable sources of energy(solar, wind, hydel), can be used
to generate the required electrical power. Additionally the sleep mode can be
activated after taking a reading to save power, also depending on the external
situation, a power source can be removed to save some capital. A network of such
units can be formed which can communicate with each other, and send the data over
to the server. Readings from different nodes can be compared to check the source
of water pollution. Additionally, the readings can be used to plan future sewage
treatment plants.

Hardware setup:
An Arduino microcontroller is used to read the raw sensor data and convert it
into readable format. Then the serial data is sent to the computer via USB and
read by the python script. Arduino sketch ard/final.ino is uploaded to the Arduino
and following connections are made:

Sensor      Arduino Pin

pH 
Po    ----> A2
G     ----> GND
V+    ----> 5V

Turbidity
G     ----> GND
V     ----> 5V
S     ----> A0

TDS
S     ----> A1
GND   ----> GND
VCC   ----> 5V

Temperature DS18B20
S     ----> D2
GND   ----> GND
VCC   ----> 5V


How to run this software:
First the COM port(from Arduino Software) is mentioned in the PySerial initialise
then we can run the code. In the UI, we can see current values, predicted values
(for next hour) and also the graphs, which are for measured values and the
anomalous values.

Credits to Sayandeep Nayak(Team Leader), Dhyeya Patel, Dev Jhamtani, Isha Shah