<p align="center">
 <h1 align="center">Project on Programmable Logic Controller</h1>
</p>

# Introduction
This project designs and constructs a product classification model by color using PLC Simens S7-1200 combined with image processing applications. In this project, we use Computer Vision to detect three different colors such as Yellow, Blue and Purple. After that, we communicate with PLC S7-1200 through Modbus TCP/IP Protocol. The version of TIA Portal is v16.

# System design and construction
The product classification system by color works on the basis of processing color scanned images of each product. The colors are sent to the computer and processed and then put into the PLC, the PLC is responsible for processing and emitting signals to control the cylinder to push the product into the corresponding container. Products that are not among the products that need to be sorted are taken to the end of the conveyor and dropped into the defective product container. This system is repeated continuously along with packaging, labeling and storage lines to create a complete production line of the factory.

The hardware of the system includes: control devices (PLC, relay), actuators, motors, conveyors, pneumatic cylinders, Camera Logitech C270, sensors.

<p align="center">
  <img src="images/hardware.jpg" width=600><br/>
  <i>System model built</i>
</p>

The system algorithm flowchart is shown below:

<p align="center">
  <img src="images/diagram.png" width=600><br/>
</p>

The system wiring diagram is as follows:

<p align="center">
  <img src="images/wiring_diagram.png" width=600><br/>
  <i>Connection diagram of PLC control circuit</i>
</p>

<p align="center">
  <img src="images/wiring2.png" width=600><br/>
  <i>Connection diagram of motor dynamic circuit and cylinder solenoid valve</i>
</p>

# Control interface design
The interface is designed by the team using the Python programming language.

<p align="center">
  <img src="images/gui_start.jpg" width=600><br/>
  <i>Python login interface</i>
</p>

<p align="center">
  <img src="images/gui_qs.jpg" width=600><br/>
  <i>Color Observation Interface on Python</i>
</p>

# Create a monitoring interface on WinCC

<p align="center">
  <img src="images/scada.jpg" width=600><br/>
  <i>Main interface of the system on WinCC</i>
</p>

<p align="center">
  <img src="images/scada_main.jpg" width=600><br/>
  <i>System control and monitoring interface on WinCC</i>
</p>

# Experimental results

<p align="center">
  <img src="images/yello.jpg" width=600><br/>
  <i>Camera results identify yellow products</i>
</p>

<p align="center">
  <img src="images/blue.jpg" width=600><br/>
  <i>Camera results identify blue products</i>
</p>

<p align="center">
  <img src="images/purple.jpg" width=600><br/>
  <i>Camera results identify purple products</i>
</p>

<p align="center">
  <img src="images/xilanh.jpg" width=600><br/>
  <i>WINCC Sorted Product Push Cylinder</i>
</p>

<p align="center">
  <img src="images/xilanh2.jpg" width=600><br/>
  <i>Number of products in each carton after sorting on WINCC</i>
</p>

# Video
For more detail, you can watch the Video show how the system operating: https://youtu.be/-eSwlSKctss
