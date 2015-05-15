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
import sys
import time
import numpy
from gnuradio import gr
import sciscipy

class Max_val(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,tstart,tstop,tstep):
	self.c = 0
	self.i = 0
	self.max_arr = []
	self.final_max = 0
	self.sec_max = 0		
	self.num = float(tstop)/float(tstep)
	
        gr.sync_block.__init__(self,
            name="Max_val",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
	    
    def work(self, input_items, output_items):
	self.b = input_items[0][:]
	self.i = self.i+1
	self.c = max(self.b)
	if(self.i <= self.num):
		self.max_arr.append(self.c)
		print "I am here\n",self.i
	else:
		self.sec_max = max(self.max_arr)
		self.i = 0
		print "I am sec_max", self.sec_max

	self.final_max = self.sec_max
	out = output_items[0]
	out[:] = numpy.float32(self.final_max)
	return len(output_items[0])
    

