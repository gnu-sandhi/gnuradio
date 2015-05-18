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

class Comparator(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,ref_val,high_val,low_val):
        self.ref_val = ref_val
	self.high_val = high_val
	self.low_val = low_val
        gr.sync_block.__init__(self,
            name="Comparator",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
	    

    def work(self, input_items, output_items):
	b = input_items[0][:]
        c = max(b)
	print "I am val of b\n",b
	print "I am value of c\n",c
#	print "I am ref value\n",self.ref_val
	#print "High value\n",self.high_val
        #print "lowwwwwwwwwwwwwww value\n",self.low_val
	
#	print "Val of c max of b\n", c
	if(c > self.ref_val):
		t = self.high_val
		print "I am in 1 if"	
	elif(c < self.ref_val):
		t = self.low_val
		print "I am in 2 if"
	else:
		t = float(self.high_val + self.low_val)/2
		print "I am in 3 if"
	print "I am value of t\n",t
	

        out = output_items[0]
        out[:] = numpy.float32(t)
        return len(output_items[0])
    

