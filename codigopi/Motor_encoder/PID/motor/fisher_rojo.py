import pigpio

class Motor_encoder(object):
    """docstring for Motor_encoder"""
    def __init__(self, pinA , pinB):
        self.pinA = pinA
        self.pinB = pinB
        self.pi = pigpio.pi()
        self.pi.set_mode(pinA, pigpio.OUTPUT)
        self.pi.set_mode(pinB, pigpio.OUTPUT)

    def avance(self , velocidad): # funcion que avanza hacia adelante o hacia aras dependiendo de la velocidad propuesta
        if velocidad > 0:    # si la velocidad es mayor a cero definimos pin hacia adelante , para que ese pin actue el PWM y apagamos el PWM en el otro pin 
            pin = self.pinA
            self.pi.set_PWM_cycle(self.pinB , 0)
        elif velocidad < 0: #Si la velocidad es menor a cero , el motor debera ir hacia atras 
            pin = self.pinB
            velocidad = abs(velocidad)
            self.pi.set_PWM_cycle(self.pinA , 0)

        if not velocidad:    
            self.pi.write(self.pinA , 0) #Si la velocidad es 0 paramos el motor mandando 0 a los 2 pines del L293D
            self.pi.write(self.pinB , 0)    
        
        if abs(velocidad) > 255 : velocidad = 255
        
        self.pi.set_PWM_cycle(pin , velocidad) # Rodar motor a la direccion decidida , a la velocidad propuesta

    def stop(self):
        self.pi.set_PWM_cycle(self.pinA , 0)
        self.pi.set_PWM_cycle(self.pinB , 0) 
