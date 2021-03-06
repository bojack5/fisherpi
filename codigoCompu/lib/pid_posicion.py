#!/usr/bin/env python3

from PID import PID
import pigpio
from settings import pines
from fischerpi import Motor
DIRECCION = '192.168.15.39'
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
    _set = 1
    pulsos_revolucion = 74
    def __init__(self,pin , kp = 1.5 , ki = 0.5 , kd = 0.0):
        self.pin = pin
        #self.callback = callback
        self.pidp = PID_Posicion(kp,ki,kd)
        self.start()
        
    def interrupt(self , *args):
        vel = self.pidp.motor.velocidad
        if vel > 0:
            self.pos += 0.081818181818
        if vel < 0: 
            self.pos -= 0.081818181818   
        #print('posicion = %s'%self.pos)
        
        #print('Velocidad = %s'%vel)
        #pos = self.callback(self.pidp.motor.velocidad)
        error = self.pidp.pid.update(self.pos)
        #print('error = %s'%error)
        if error < 0:  direccion = -1
        if error > 0:  direccion =  1
        if abs(error) < 0.5: 
            direccion = 0
            self._set = 1
        sp = abs(error)*10*direccion
        self.pidp.motor.avance(sp)
        
    def start(self):
        self.cb = pi.callback(self.pin,pigpio.RISING_EDGE,self.interrupt)

    def cancel(self):
        self.cb.cancel()

    def reset(self):
        self.pos = 0
        self.rev = 0  


		