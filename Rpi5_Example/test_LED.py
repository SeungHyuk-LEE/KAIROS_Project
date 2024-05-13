# LED test

from gpiozero import LED

pin_led_01 = 12

led = LED()

while True:
    number_input=int(input("Enter 0 or 1: "))   #when run code, Enter 0 or 1 : output

    if number_input == 1:   # input 1, LED ON
        led.on()
        print('P1 on -> led1 on')
    
    if number_input == 0:   # input 0, LED OFF
        led.off()
        print('P1 off -> led1 off')