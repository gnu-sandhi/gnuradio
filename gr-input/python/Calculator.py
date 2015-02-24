#!/usr/bin/env python
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from numpy import log
from numpy import exp
from numpy import sqrt
from gnuradio import gr
import time

class Calculator(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,num_inputs):
	number = num_inputs
	a = []
	for i in range(0,number):
            a.append(numpy.float32)
#	print "value of a",a
        gr.sync_block.__init__(self,
            name="Calculator",
            in_sig=a,
            out_sig=[numpy.float32])
	    
	#print "I am over slept"
        #print len(self.ret_array)
    def set_parameters(self,Exp,num_inputs):
	self.Exp = Exp
	#print "This is EXP", Exp
	self.num_inputs = num_inputs


    def work(self, input_items, output_items):
	try:
            a0 = input_items[0]
	except IndexError:
	    pass
	try:
            a1 = input_items[1]
	except IndexError:
	    pass
	try:
	    a2 = input_items[2]
	except IndexError:
	    pass
	try:
	    a3 = input_items[3]
	except IndexError:
	    pass
	try:
	    a4 = input_items[4]
	except IndexError:
	    pass
	try:
	    a5 = input_items[5]
	except IndexError:
	    pass
	try:
	    a6 = input_items[6]
	except IndexError:
	    pass
	try:
	    a7 = input_items[7]
	except IndexError:
	    pass
	try:
	    a8 = input_items[8]
	except IndexError:
	    pass
	try:
	    a9 = input_items[9]
	except IndexError:
	    pass
        #out = output_items[0][0]
	print "This is self.Exp\n",self.Exp
	
        output_items[0][:] = eval(self.Exp)
	#print "This is the output value\n", output_items[0][0]
	#print "I am the oputput add python\n", eval(self.Exp)
        return len(output_items[0])
                                              
