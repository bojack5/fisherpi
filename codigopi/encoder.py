#!/usr/bin/env python
import pigpio
from Motor_encoder.motor.fisher_rojo import Motor_encoder
from PID.pid_posicion import PID_posicion as pidv 

class Encoder(object):
    """docstring for Motor_Encoder"""
    def __init__(self,pinEncoder , pinA , pinB):
        
        self.pinEncoder = pinEncoder
        self.pi = pigpio.pi()
        self.pi.set_mode(pinEncoder, pigpio.INPUT)
        self.pi.set_pull_up_down(pinEncoder, pigpio.PUD_UP)
        self.cbE = self.pi.callback(self.pinEncoder, pigpio.EITHER_EDGE, self.interrupcion)
        self.pidp = pidv() #faltan definir los pines 
        self.posicion = 0 #Posicion del encoder

    def interrupcion(self):
    	#Funcion que definira el avance , y error en el PID de posicion
        self.posicion += 1
        error = self.pid_posicion.pid.update(self.posicion)
        if not error:
            self.pido.motor.avance(0)
        else:
            self.pido.motor.avance(error)    





