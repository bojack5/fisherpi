#!/usr/bin/env python
import pigpio

class Motor_Encoder(object):
    """docstring for Motor_Encoder"""
    def __init__(self, pinA , pinB , pinEncoder):
        self.pinA = pinA
        self.pinB = pinB
        self.pinEncoder = pinEncoder
        self.pi = pigpio.pi()
        self.pi.set_mode(pinA, pigpio.OUTPUT)
        self.pi.set_mode(pinB, pigpio.OUTPUT)
        self.pi.set_mode(pinEncoder, pigpio.INPUT)
        self.pi.set_pull_up_down(pinEncoder, pigpio.PUD_UP)
        self.cbE = self.pi.callback(self.pinEncoder, pigpio.EITHER_EDGE, self.interrupcion)
        
    def interrupcion(self):
    	#Funcion que definira el avance , y error en el PID de posicion
        pass

    def avance(self):
        pass
    



