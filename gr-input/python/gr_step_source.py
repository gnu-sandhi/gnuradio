#!/usr/bin/python

import gras
import numpy
# Serial is imported in __init__
class step(gras.Block):
	

        def __init__(self):
                gras.Block.__init__(self,
                        name="ser",
                        in_sig=[numpy.float32],
                        out_sig=[numpy.float32])
		self.flag=True

        def set_parameters(self, step_size, offset, width):
		self.step_size = step_size	
		self.width = width
		self.offset = offset

        def work(self, input_items, output_items):
		
                out = output_items[0][0:1]
		input_stream = input_items[0][0]

		if self.flag:
			for i in range(self.width):
				out[:1] = self.offset	
				print "OUT", out
					
				self.produce(0,1) # Produce from port 0 output_items
				self.consume(0,1) # Consume from port 0 input_items

			self.flag = False

		else:	
			out[:1] = self.offset + input_stream*self.step_size
			
			print "OUT", out
				
			self.produce(0,1) # Produce from port 0 output_items
			self.consume(0,1) # Consume from port 0 input_items

