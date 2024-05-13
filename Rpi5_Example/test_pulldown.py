# 풀업스위치

from gpiozero import LED
from gpiozero import Button

from time import sleep

pin_led_01 = 21 #
pin_sw = 20
pin_pullup = 16 

led = LED(pin_led_01)
switch = Button(pin_sw)
pullup = LED(pin_pullup)

while True:
    pullup.on()
    sleep(0.5)

    if switch.is_pressed:
        led.on()
        print("switch: on")
    else:
        led.off()
        print("switch: off")
