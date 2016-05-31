#!/usr/bin/env python
from pid import PID 
from motor.fisher_rojo import Motor_encoder

class PID_Posicion(object):
    """docstring for PID_Posicion"""
    def __init__(self, kp = 1.0 , ki =0.0, kd =0.0 , pinA = 4, pinB = 21):
        self.pid  = PID(kp , ki , kd)        
        self.motor = Motor_encoder(pinA , pinB)

    def SetPoint(self , setpoint):
        self.pid.setPoint(abs(setpoint))	
        self.motor.avance(setpoint)
