#!/usr/bin/env python3
from fischerpi import *

pines = {'motor':{
                    1:[17,27],
                    2:[18,23],
                    3:[9,11],
                    4:[25,8],
                    
                    },

         'encoder':{
                     1:21,
                     2:20,
                     },

         'FinCarrera':{
                       1:16,
                       2:12,
                       3:7,
                       4:26,
                       5:19,
                       6:13,
                       },            
         }

motor1 = Motor(pines['motor'][1])
motor2 = Motor(pines['motor'][2])
motor3 = Motor(pines['motor'][3])
motor4 = Motor(pines['motor'][4])

'''encoder1 = Encoder(pines['encoder'][1])
encoder2 = Encoder(pines['encoder'][2])

fc1 = FinDeCarrera(pines['FinCarrera'][1])
fc2 = FinDeCarrera(pines['FinCarrera'][2])
fc3 = FinDeCarrera(pines['FinCarrera'][3])
fc4 = FinDeCarrera(pines['FinCarrera'][4])
fc5 = FinDeCarrera(pines['FinCarrera'][5])
fc6 = FinDeCarrera(pines['FinCarrera'][6])
'''
