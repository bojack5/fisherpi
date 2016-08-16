#!/usr/bin/env python3

import pigpio
DIRECCION = '192.168.1.85'
pi = pigpio.pi(DIRECCION)


class Motor(object):
    """Clase para manejar motor en ambas polarizaciones , 
    mandando voltaje a uno u otro pin para girar en esa direccion"""
    def __init__(self,pin1,pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        self.stop()

    def avance(self):
        pi.write(self.pin1,1)
        pi.write(self.pin2,0)

    def retroceso(self):
        pi.write(self.pin1,0)
        pi.write(self.pin2,1)

    def stop(self):
        pi.write(self.pin1,0)
        pi.write(self.pin2,0)    



class Encoder(object):
    """Clase para manejar las interrupciones mandadas por el Encoder
    del servomotor , """
    cuenta = 0
    def __init__(self,pin):
        self.pin = pin
        self.start()
        
    def interrupt(self , *args):
        self.cuenta +=1
        print(self.cuenta,args[0])

    def start(self):
        self.cb = pi.callback(self.pin,pigpio.RISING_EDGE,self.interrupt)

    def cancel(self):
        self.cb.cancel()

class FinDeCarrera(Encoder):
    """Clase para manejo de interrupciones de fines de carrera"""
    cuenta = 0
    def __init__(self,pin,callback):
        self.pin = pin
        self.callback = callback
        self.start()

    def start(self):
        self.cb = pi.callback(self.pin,pigpio.RISING_EDGE,self.callback)



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
