#!/usr/bin/env python3

from PID import PID
import pigpio
from settings import pines
from fischerpi import Motor
DIRECCION = '192.168.1.85'
pi = pigpio.pi(DIRECCION)

class PID_Posicion(object):
    """docstring for PID_Posicion"""
    def __init__(self,callback,kp = 1.5 ,ki = 0.5 ,kd = 0.0, motor_no = 4,):
        self.callback = callback
        self.pid = PID(kp,ki,kd)
        self.motor = Motor(pines['motor'][motor_no])

    def setPoint(self , setpoint):
        self.pid.setPoint(setpoint)
        sp = int(setpoint*(10))
        self.motor.avance(sp)


class Encoder(object):
    """Clase para manejar las interrupciones mandadas por el Encoder
    del servomotor , """
    pos = 0
    rev = 0
    pulsos_revolucion = 74
    def __init__(self,pin , callback , kp = 1.5 , ki = 0.5 , kd = 0.0):
        self.pin = pin
        self.callback = callback
        self.pidp = PID_Posicion(kp,ki,kd)
        self.start()
        
    def interrupt(self , *args):
        pos = self.callback()
        error = self.pidp.pid.update(pos)
        if error < 0:  direccion = -1
        if error > 0:  direccion =  1
        if abs(error) < 0.5: direccion =  0

        sp = abs(error)*10*direccion
        self.pidp.motor.avance(sp)

    def start(self):
        self.cb = pi.callback(self.pin,pigpio.RISING_EDGE,self.interrupt)

    def cancel(self):
        self.cb.cancel()

    def reset(self):
        self.pos = 0
        self.rev = 0  


		