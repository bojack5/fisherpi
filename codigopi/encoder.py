#!/usr/bin/env python
import pigpio

class Motor_Encoder(object):
    """docstring for Motor_Encoder"""
    def __init__(self, pinA , pinB , pinEncoder):
        self.pinA = pinA
        self.pinB = pinB
        self.pinEncoder = pinEncoder
        self.pi = pigpio.pi()
    
    def interrupcion(self):
        pass

    def avance(self):
        pass

    



