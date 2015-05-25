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
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline

from control import *


class Bode(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,order):
	a = []
#	self.flag = 0
	self.z =[]
	self.z1=[0,0,0,0]
	self.z2=[]
	self.z3=[0,0,0,0]
	self.b = [0,0,0,0]
	self.c = [0,0,0,0]
	self.i = 0
        self.order=int(order)+1
        gr.sync_block.__init__(self,
            name="Bode",
            in_sig=[numpy.float32,numpy.float32],
            out_sig=None)
	    
    def plot_bode(self,b,c):
	omega = None
	db = True
	deg = True
	Hz= True
	plot = True
	s1 = tf(b,c)
	bode_plot(s1,omega,db,Hz,deg,plot)
	plt.ion()
	plt.draw()
	

    def work(self, input_items, output_items):
	k = self.order
	for i in range(0,k):
	    self.b[i] = input_items[0][i]
	for i in reversed(self.b):
	    self.z.append(i)
	v1 = 0
	for i2 in self.z:
	    self.z1[v1]=i2
	    v1 = v1 + 1
	del self.z[:]
	print "I am z1\n",self.z1
		
	for j in range(0,k):
	    self.c[j] = input_items[1][j]
	for i1 in reversed(self.c):
            self.z2.append(i1)
	v = 0
	for i3 in self.z2:
	    self.z3[v] = i3
	    v = v + 1
	print "Z2222\n", self.z2
        del self.z2[:]
	print "I  am z3\n", self.z3
	self.plot_bode(self.z1,self.z3)
	plt.clf()	
	print "Counter",self.i
	self.i+=1
        in0 = input_items[0]
        # <+signal processing here+>
        return len(input_items[0])

