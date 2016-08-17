#!/usr/bin/env python3,
import pigpio
import time
from lib.fischerpi import PWM
pi = pigpio.pi('192.168.15.4')
pines = [17,27,18,23,9,11,25,8]

for pin in pines:
    pi.write(pin,0)

for pin in pines:
    print('Probando pin %s...'%pin)
    ppin = PWM(pin)
    ppin.set_duty(128)
    time.sleep(1)
    ppin.set_duty(172)
    time.sleep(1)
    ppin.set_duty(0)
    time.sleep(0.5)


