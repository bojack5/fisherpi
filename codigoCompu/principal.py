#!/usr/bin/env python3

from pid_posicion import PID_Posicion as pidp

from pid_posicion import Encoder
from settings import pines
def callback_enc(self):

    self.pos += 0.01818181818
    error = self.pidp.pid.update(self.pos)
    if error < 0:  direccion = -1
    if error > 0:  direccion =  1
    if abs(error) < 0.5: direccion =  0

    sp = abs(error)*10*direccion
    self.pidp.motor.avance(sp)

enc1 = Encoder(pines['encoder'][1],callback_enc,)

while 1:
    try:
        sp = int(input('Ingresa posicion \n>>'))
        enc1.pidp.setPoint(sp)

    except KeyboardInterrupt:
        enc1.pidp.motor.stop()

