#!/usr/bin/python

import gras
import numpy
import serial
class ser(gras.Block):
	

        def __init__(self):
                gras.Block.__init__(self,
                        name="ser",
                        in_sig=[numpy.float32],
                        out_sig=[numpy.float32])
		self.n = 1
        def set_parameters(self, port, baud, bytesize, parity, stopbits):
		
		try:
			print port
			self.ser_obj = serial.Serial(port, baud,  bytesize, parity,  stopbits)
			print("serial found on " + port )
			self.ser_obj.open()
		except:
			print "Couldn't Open Serial Port " + port + " Failed"
	

        def work(self, input_items, output_items):
		
		self.n = input_items[0][0]
                out = output_items[0][:self.n]
		# Input is size of output_items to be returned

		for i in range(self.n):
			
			# Try catch block to avoid Error
			# ValueError: invalid literal for int() with base 10: '\xfe354\r\n'
			try:
				out[i] = int(self.ser_obj.readline())
			except:
				pass
		
		print "OUT", out[:self.n]
			
		self.produce(0,len(out)) # Produce from port 0 output_items
		self.consume(0,1) # Consume from port 0 input_items

