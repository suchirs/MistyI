"""
Created on Sat Mar  9 20:36:49 2019
@author: Suchir
"""
import mistyPy   # Imports misty's program
import time      # Imports time module to use the sleep command
mia=mistyPy.Robot("192.168.0.17") # Connect's to misty
mia.changeLED(0,0,255) #Set the LED to Blue to show start of the program
time.sleep(30) # To show we can see the program has started
mia.changeLED(0,255,0)   # Change the led to green to signal ready state
mia.subscribe("TimeOfFlight") # Subsribes to time of flight
while True:    # Start a infinite loop 
    incoming_data=mia.time_of_flight()  # Start reading the distance from all sensor's
    print(incoming_data)  # Check the sensor's data
    distance=incoming_data["Center"]  # Get the center's time of flight data
    print(distance)   # Tell us how far the object is
    if distance < 0.080:   #If distance is less than meter-20% 
       mia.changeLED(255,0,0) #Change color to red as misty is blocked
       mia.unsubscribe("TimeOfFlight") # Unsubscribe 
       break  # Break from while loop
mia.changeLED(127,255,212) # In the end set to Aquamarine color to show program completion
