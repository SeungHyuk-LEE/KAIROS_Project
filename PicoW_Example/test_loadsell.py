from machine import Pin
from hx711 import *
import utime

hx = hx711(Pin(16), Pin(20)) 

hx.set_power(hx711.rate.rate_10)

while True:
    val = hx.get_value()
    print(val)
    weight = (val-13000)/(543500-13000)*2036    #Correction value
    print("weight==", round(weight,1))
    utime.sleep(1)
    
hx.close()