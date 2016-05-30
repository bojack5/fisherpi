#!/usr/bin/env python

import pigpio

class FinCarrera(object):
    """docstring for FinCarrera"""
    def __init__(self, pin , callback):
    	self.pin  = pin
    	self.callback = callback
    	self.pi = pigpio.pi()
    	

    def function(self):
        pass    	





