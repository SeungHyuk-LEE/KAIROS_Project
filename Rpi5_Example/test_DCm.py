from gpiozero import Motor
import time

pin_enable = 22
pin_forward = 23
pin_backward = 24

motor = Motor(forward= pin_forward, backward= pin_backward, enable= pin_enable)

print("motor turn = forward")
motor.forward()
time.sleep(5)
    
"""
wheel_pin = 23
speed_pin = 24

motor = Motor(forward=wheel_pin, backward=wheel_pin, enable=speed_pin)

motor.forward()

sleep(10)

motor.stop()
"""
