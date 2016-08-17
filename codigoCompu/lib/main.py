#!/usr/bin/env python3

from fischerpi import Encoder
enc1 = Encoder(21)

while 1:
    try:
        sp = input('Introduce Posicion : \n>> ')
        sp2 = int(int(sp)*4400/360)
        print('%s grados && %s interrupciones'%(sp,sp2))
        enc1.setPoint(sp2)
    except KeyboardInterrupt: 
        enc1.shutdown()