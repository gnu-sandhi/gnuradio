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

class Numerator(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,num_inputs):
	self.number = num_inputs+1
	a = []
	for i in range(0,self.number):
            a.append(numpy.float32)
        gr.sync_block.__init__(self,
            name="Numerator",
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
	var = self.number
    	o1 = output_items[0][:var]
        out_arr=[]
        time.sleep(0.001)
        
        for i in range(0,var):
            out_arr.append(b[i])
        o1[:] = out_arr
        print "out value\n",o1
        return len(output_items[0][:])
