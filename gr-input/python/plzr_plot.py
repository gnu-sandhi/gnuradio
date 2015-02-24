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

class plzr_plot(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,order):
	sys.setrecursionlimit(2000)
	a = []
#	self.flag = 0
	self.b = [0,0,0,0,0,0]
	self.c = [0,0,0,0,0,0]
	self.i = 0
        self.order=int(order)+1
        gr.sync_block.__init__(self,
            name="plzr_plot",
            in_sig=[numpy.float32,numpy.float32],
            out_sig=None)
	    
    def plot(self,b,c):
        string1 = "s=%s; h=syslin('c',"
        string2 = str(b[4])+"*s^4+"+str(b[3])+"*s^3+"+str(b[2])+"*s^2+"+str(b[1])+"*s+"+str(b[0])+","
        string3 = str(c[4])+"*s^4+"+str(c[3])+"*s^3+"+str(c[2])+"*s^2+"+str(c[1])+"*s+"+str(c[0])+");"
	string4 = "plzr(h);"
  
	string = string1 + string2 +string3 + string4
        sciscipy.eval(string)


	
    def work(self, input_items, output_items):
	print "I am input", input_items
	print "I am output", output_items
	k = self.order
	for i in range(0,k):
	    self.b[i] = input_items[0][i]
	print "I am value of b\n",self.b    
	
	
	for j in range(0,k):
	    self.c[j] = input_items[1][j]
	print "I am vlaue of c\n", self.c
		
        self.plot(self.b,self.c)	
        in0 = input_items[0]
        # <+signal processing here+>
        return len(input_items[0])

