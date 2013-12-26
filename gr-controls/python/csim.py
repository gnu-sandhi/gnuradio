#!/usr/bin/python
import gras
import numpy

class csim(gras.Block):

        def __init__(self):
                gras.Block.__init__(self,
                        name="csim",
                        in_sig=[numpy.float32],
                        out_sig=[numpy.float32])

        def set_parameters(self,p,i,d,a,b,d1,e,f):
                self.param1 = p
                self.param2 = i
                self.param3 = d
                self.param4 = a #n0
                self.param5 = b #n1
                self.param6 = d1 #d0
		self.param7 = e #d1
                self.n = f #window

        def isIntegralWin(self, input_item, window):
                if (len(input_item) % window ):
                        raise Exception("Value of Window should be an integral value of length of input items")

        def work(self, input_items, output_items):

                #n = min(len(input_items[0]), len(output_items[0]))
                in0 = input_items[0]
                out = output_items[0]

                from csim_sci import csim
                
		#Processing 
		out[:self.n] = csim(self.param1, self.param2, self.param3, self.param4,
                                        self.param5, self.param6, self.param7, in0[:self.n].tolist()) # IMP: in0[:self.n].tolist() passes a python array, without which window cannot be raised above certain value | numpy.array bug

                print "OUT ", out[:self.n]
		
                self.consume(0,self.n) # Consume from port 0 input_items
                self.produce(0,self.n) # Produce from port 0 output_items

