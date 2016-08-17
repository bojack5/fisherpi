#!/usr/bin/env python3

from pid_posicion import PID_Posicion as pidp
from pid_posicion import Encoder
from settings import pines
import time
pos = 0 

def callback_enc(vel):
    global pos
    if vel > 0:
        pos += 0.081818181818
    if vel < 0: 
        pos -= 0.081818181818   
    #print(pos)
    return pos


enc1 = Encoder(pines['encoder'][1],)
print('posicion\terror\n')
while 1:
    try:
        sp = int(input('Ingresa posicion \n>>'))
        enc1.pidp.setPoint(sp)
        enc1._set = 0
        while not enc1._set:
            time.sleep(0.1)
            print('%s\t'%enc1.pos,)

        
        time.sleep(0.1)
        

    except KeyboardInterrupt:
        enc1.pidp.motor.stop()

