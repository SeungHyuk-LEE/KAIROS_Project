# DistanceSensor test ( HC-SR04 )

from gpiozero import DistanceSensor
import time

pin_echo = 20
pin_trgger = 21
sensor = DistanceSensor(echo=pin_echo, trigger=pin_trgger)

while True:
    print("Distance: ", sensor.distance * 100)
    time.sleep(1)