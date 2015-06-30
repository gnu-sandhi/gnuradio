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
        self.b = [0]*self.number
	for i in range(0,self.number):
            a.append(numpy.float32)
        gr.sync_block.__init__(self,
            name="Numerator",
            in_sig=a,
            out_sig=[numpy.float32])

    def work(self, input_items, output_items):
        for i in range(0,self.number):
            self.b[i] = input_items[i][0]
    	o1 = output_items[0][:self.number]
        out_arr=[]
        time.sleep(0.001)
        
        for i in range(0,self.number):
            out_arr.append(self.b[i])
        o1[:] = out_arr
        return len(output_items[0][:])
