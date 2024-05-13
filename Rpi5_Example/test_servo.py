# Servo motor test
# 서보모터를 3가지 각으로 1초간 동작시키는 코드

from gpiozero import AngularServo
from time import sleep

servo_pin = 14

servo = AngularServo(servo_pin, min_angle=0, max_angle=180, min_pulse_width=0.0006, max_pulse_width=0.0024)

while True:
    servo.angle = 0
    sleep(1)

    servo.angle = 90
    sleep(1)

    servo.angle = 170
    sleep(1)
