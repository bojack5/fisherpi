#!/usr/bin/env python3

import pigpio

DIRECCION = '192.168.1.85'
pi = pigpio.pi(DIRECCION)


class Motor(object):
    velocidad = 0
    """Clase para manejar motor en ambas polarizaciones , 
    mandando voltaje a uno u otro pin para girar en esa direccion"""
    def __init__(self,pines,):
        self.pin1 = pines[0]
        self.pin2 = pines[1]
        self.pwm1 = PWM(self.pin1)
        self.pwm2 = PWM(self.pin2)
        self.stop()

    def avance(self , vel = 128):
        if vel == 0:
            self.stop()
            self.velocidad = 0
        else:
            if vel > 0:
                #saturacion
                if abs(vel) < 75 : vel = 75
                if abs(vel) > 255 : vel = 255
                
                self.pwm1.set_duty(vel)
                self.pwm2.set_duty(0)
                self.velocidad = vel
            elif vel < 0:
                #saturacion
                if abs(vel) < 75 : vel = 75
                if abs(vel) > 255 : vel = 255

                self.pwm1.set_duty(0)
                self.pwm2.set_duty(-vel)
                self.velocidad = vel




    def stop(self):
        #saturacion
        self.pwm1.set_duty(0)
        self.pwm2.set_duty(0)    



  

class FinDeCarrera(object):
    """Clase para manejo de interrupciones de fines de carrera"""
    cuenta = 0
    def __init__(self,pin,callback):
        self.pin = pin
        self.callback = callback
        self.start()



class PWM(object):
    'Clase para Manejo de PWM'
    def __init__(self , pin):
        self.pin = pin

    def set_duty(self , dc):
        pi.set_PWM_dutycycle(self.pin,abs(dc))

    def set_frequency(self , freq):
        pi.set_PWM_frequency(pin,freq)






if __name__ == '__main__':
    import time
    giro = Motor(8,25)
    giro.stop()
    subeBaja = Motor(9,11)
    enc1 = Encoder(21)
    enc2 = Encoder(20)

    giro.retroceso()
    time.sleep(1)
    giro.stop()
    giro.avance()
    time.sleep(1)
    giro.stop()

    subeBaja.avance()
    time.sleep(1)
    subeBaja.stop()
    subeBaja.retroceso()
    time.sleep(1)
    subeBaja.stop()


    enc1.cancel()    			        	
    enc2.cancel()
