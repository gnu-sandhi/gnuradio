#!/usr/bin/python

import gras
import numpy
# Serial is imported in __init__
class ramp(gras.Block):
	

        def __init__(self):
                gras.Block.__init__(self,
                        name="ser",
                        in_sig=[numpy.float32],
                        out_sig=[numpy.float32])
		self.i = 0
		self.flag=True
        
	def set_parameters(self, ramp_slope, height_Offset, width_Offset):
		self.slope = ramp_slope	
		self.width = width_Offset
		self.offset = height_Offset

        def work(self, input_items, output_items):
		
                out = output_items[0][0:1]
		input_stream = input_items[0][0]
		
		if self.flag:
			for j in range(self.width):
				out = self.offset
				print "OUT", out

				self.produce(0,1) # Produce from port 0 output_items
				self.consume(0,1) # Consume from port 0 input_items
			
			self.flag = False

		else:

			self.i = self.i + 1
			out[:1] =self.offset + self.i*input_stream*self.slope
		
			print "OUT", out
			
		self.produce(0,1) # Produce from port 0 output_items
		self.consume(0,1) # Consume from port 0 input_items

