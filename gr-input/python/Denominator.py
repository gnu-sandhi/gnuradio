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

import time
import numpy
from gnuradio import gr

class Denominator(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,num_inputs):
	number = num_inputs
	a = []
#        out_arr=[]
	for i in range(0,number):
            a.append(numpy.float32)
	print "value of a",a
        gr.sync_block.__init__(self,
            name="denomenator",
            in_sig=a,
            out_sig=[numpy.float32])

    def work(self, input_items, output_items):
        b=[0,0,0,0,0,0,0,0,0,0]
	try:
            b[0] = input_items[0][0]
	except IndexError:
	    pass
	try:
            b[1] = input_items[1][0]
	except IndexError:
	    pass
	try:
	    b[2] = input_items[2][0]
	except IndexError:
	    pass
	try:
	    b[3] = input_items[3][0]
	except IndexError:
	    pass
	try:
	    b[4] = input_items[4][0]
	except IndexError:
	    pass
	try:
	    b[5] = input_items[5][0]
	except IndexError:
	    pass
	try:
	    b[6] = input_items[6][0]
	except IndexError:
	    pass
	try:
	    b[7] = input_items[7][0]
	except IndexError:
	    pass
	try:
	    b[8] = input_items[8][0]
	except IndexError:
	    pass
	try:
	    b[9] = input_items[9][0]
	except IndexError:
	    pass
    	out = output_items[0][:5]
        out_arr=[]
        time.sleep(0.001)
        
#        print "value of b",b
        for i in range(0,len(input_items)):
            out_arr.append(b[i])
#            print "I am input items",input_items[i][0]
#        print "out_array",out_arr
        out[:] = out_arr 
#	print "i am length",len(output_items[0][:])
#	print "value of out",out
        return len(output_items[0][:])

