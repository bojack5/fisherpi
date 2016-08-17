#!/usr/bin/env python3

import pigpio

DIRECCION = '192.168.15.4'
pi = pigpio.pi(DIRECCION)
#from settings import pines


class Motor(object):
    velocidad = 0
    direccion = None
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
                self.direccion = 1
                if abs(vel) < 75 : vel = 75
                if abs(vel) > 255 : vel = 255
                
                self.pwm1.set_duty(vel)
                self.pwm2.set_duty(0)
                self.velocidad = vel
            elif vel < 0:
                self.direccion = 0
                #saturacion
                if abs(vel) < 75 : vel = 75
                if abs(vel) > 255 : vel = 255

                self.pwm1.set_duty(0)
                self.pwm2.set_duty(-vel)
                #print('Velocidad desde motor %s'%vel)
                self.velocidad = -vel




    def stop(self):
        #saturacion
        self.pwm1.set_duty(0)
        self.pwm2.set_duty(0)



#from fischerpi import Motor
   

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

class Encoder(object):
    """Clase para manejar las interrupciones mandadas por el Encoder
    del servomotor , """
    pos = 0
    rev = 0
    setpoint = 0
    pulsos_revolucion = 74
    motor = Motor([25,8])
    velocidad = 255
    def __init__(self,pin , motor_no = 4):
        self.pin = pin        
        
    
    def setPoint(self , sp):
        self.start()
        self.setpoint = int(sp)
        diferencia = self.setpoint-self.pos
        if self.setpoint == self.pos:

            self.motor.stop()
           
        elif abs(diferencia) < 500:
            self.velocidad = abs(diferencia)/2
           
        print(self.velocidad)    
        if diferencia > 0:
            print('hacia adelante')
            self.motor.avance(self.velocidad)
        elif diferencia < 0:
            print('hacia atras')
            self.motor.avance(-self.velocidad)


            
                     
    def callback(self , *args):
        if self.motor.direccion:
            self.pos += 1
        else: 
            self.pos -= 1    
        print('posicion = %s\tvelocidad = %s\t'%(self.pos , self.velocidad))
        diferencia = self.setpoint-self.pos
        try:   
            if abs(diferencia) < 500:
                self.velocidad = abs(diferencia)/2
            if diferencia > 0:
                self.motor.avance(self.velocidad)

            elif diferencia < 0:
                self.motor.avance(-self.velocidad)
            if diferencia == 0:
                self.cancel()
                self.motor.stop()     
        except KeyboardInterrupt:
            self.motor.stop()
            self.cancel()
            self.setpoint = 0
            pi.cancel()
    def start(self):
        self.cb = pi.callback(self.pin,pigpio.RISING_EDGE,self.callback)

    def cancel(self):
        self.cb.cancel()

    def shutdown(self):
        self.motor.stop()
        self.cb.cancel()
        pi.stop()
    def reset(self):
        self.pos = 0
        self.rev = 0




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
