#!/usr/bin/env python3

from tkinter.ttk import Frame, Button
from tkinter import Tk, BOTH ,Listbox, StringVar, END , Menu , Label , Entry , DISABLED ,NORMAL, RAISED , FLAT , LEFT , TOP , X ,Canvas , Checkbutton , BooleanVar , IntVar , Radiobutton
from tkinter import messagebox as mbox

import pigpio
import time
from lib.fischerpi import PWM , Encoder

class Aplicacion(Frame):
    pi = pigpio.pi('192.168.15.4')
    def __init__(self,parent):
        Frame.__init__(self , parent)
        self.enc1 = Encoder(21)
        self.parent = parent
        self.conexion = True#is_connected()
        self.est_pinza = 1
        self.est_subebaja = 1
        self.initUI()

    def initUI(self):
        
        for i in range(4):
            self.columnconfigure(i, pad=3)
        for i in range(4):
            self.rowconfigure(i, pad=3)
        
        #self.listBox()
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        self.fischerpi()
        self.parent.geometry('%dx%d' % (sw/4, sh/4))        
        self.pack()  

    def fischerpi(self):
        self.botonPrueba = Button(self , text = 'Prueba Motores', command = self.prueba)
        self.botonPrueba.grid()

        

        self.botonGiro = Button(self , text = 'Giro PID', command =  self.Giro)
        self.botonGiro.grid(row = 1 , column = 0)

        self.cant_posicion = Entry(self)
        self.cant_posicion.grid(row = 1 , column = 1)

        self.pinza = Button(self , text = 'Pinza', command =  lambda estado = self.est_pinza :self.pinzac(estado))
        self.pinza.grid(row = 2 , column = 0)   

        self.subeybaja = Button(self , text = 'sube', command =  self.subebaja)
        self.subeybaja.grid(row = 3 , column = 0)

    def subebaja(self):
        estado = self.est_subebaja
        if estado:
            self.pi.write(9,0)
            self.pi.write(11,1)
            self.id_sb = self.subeybaja.after(5000,self.sbcancel)
        else:
            self.pi.write(9,1)
            self.pi.write(11,0)
            print('bajando...')
            print(estado)
            self.id_sb = self.subeybaja.after(1000,self.sbcancel)     
        self.est_subebaja = not self.est_subebaja
        

    def sbcancel(self):
        self.subeybaja.after_cancel(self.id_sb)
        self.pi.write(9,0)
        self.pi.write(11,0)


    def pinzacancel(self ):
        self.pinza.after_cancel(self.id)
        self.pi.write(27,0)
        self.pi.write(17,0)

    def pinzac(self , estado):
        estado = self.est_pinza
        if estado:
            self.pi.write(27,0)
            self.pi.write(17,1)
            print('abriendo...')
            print(estado)
            
        else:
            self.pi.write(27,1)
            self.pi.write(17,0)
            print('cerrando...')
            print(estado)    
        self.est_pinza = not self.est_pinza
        print (self.est_pinza)
        self.id = self.pinza.after(1000,self.pinzacancel)



    def Giro(self):
    	grados = self.cant_posicion.get()
    	pulsos = int(grados) * 12.222222222222221
    	self.enc1.setPoint(int(pulsos))

        

    def prueba(self):
        self.botonPrueba.config(state = DISABLED)
        pines = [17,27,18,23,9,11,25,8]

        for pin in pines:
            self.pi.write(pin,0)

        for pin in pines:
            print('Probando pin %s...'%pin)
            ppin = PWM(pin)
            ppin.set_duty(128)
            time.sleep(1)
            ppin.set_duty(172)
            time.sleep(1)
            ppin.set_duty(0)
            time.sleep(0.5)
        self.botonPrueba.config(state = NORMAL)    

        

        
    def onExit(self,*args):
        self.quit()      

def main():
    root = Tk()
    app = Aplicacion(root)
    root.bind("<Control-q>", app.onExit)
    root.mainloop()


if __name__ == '__main__':
    main() 