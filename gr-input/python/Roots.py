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
import sciscipy

class Roots(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,order):
	self.out = [0,0,0,0,0,0,0,0,0,0]
	a = []
	self.b = [0,0,0,0,0,0]
        self.order=int(order)+1
	self.number = int(order)*2
	for i in range(0,self.number):
	    a.append(numpy.float32)
        gr.sync_block.__init__(self,
            name="Roots",
            in_sig=[numpy.float32],
            out_sig=a)
	    
    def find_roots(self,n):
	string1 = "s=%s;"
	string2 = "h2="+str(n[3])+"*s^3+"+str(n[2])+"*s^2+"+str(n[1])+"*s+"+str(n[0])+";[E1]=roots(h2);a11=real(E1(1));a12=imag(E1(1));b11 = real(E1(2));b12 = imag(E1(2));c11 = real(E1(3));c12 = imag(E1(3)); d11 = real(E1(4)); d12 = imag(E1(4)); e11 = real(E1(5)); e12 = imag(E1(5));"
        string = string1+string2
	print "This is string\n", string
        sciscipy.eval(string)


        try:
            self.a11 = sciscipy.read("a11")
            print "I am a11", self.a11
        except TypeError:
            self.a11 = 0
        try:
            self.a12 = sciscipy.read("a12")
            print "I am a12", self.a12
        except TypeError:
            self.a12 = 0
        try:
            self.b11 = sciscipy.read("b11")
            print "I am b11", self.b11
        except TypeError:
            self.b11 = 0
        try:
            self.b12 = sciscipy.read("b12")
        except TypeError:
            self.b12 = 0
        try:
            self.c11 = sciscipy.read("c11")
	    print "I am c11\n", self.c11
        except TypeError:
            self.c11 = 0
        try:
            self.c12 = sciscipy.read("c12")
	    print "I am c12\n", self.c12
        except TypeError:
            self.c12 = 0
        try:
            self.d11 = sciscipy.read("d11")
	    print "I am d11\n", self.d11
        except TypeError:
            self.d11 = 0
        try:
            self.d12 = sciscipy.read("d12")
        except TypeError:
            self.d12 = 0
        try:
            self.e11 = sciscipy.read("e11")
        except TypeError:
            self.e11 = 0
        try:
            self.e12 = sciscipy.read("e12")
        except TypeError:
            self.e12 = 0

    def work(self, input_items, output_items):

#	print "I am here\n", output_items
	k = self.order
	for i in range(0,k):
	    self.b[i] = input_items[0][i]
   
	self.find_roots(self.b)	
	

        self.out[0] = numpy.float32(self.a11)
        self.out[1] = numpy.float32(self.b11)
        self.out[2] = numpy.float32(self.a12)
        self.out[3] = numpy.float32(self.b12)
        self.out[4] = numpy.float32(self.c11)
        self.out[5] = numpy.float32(self.c12)
        self.out[6] = numpy.float32(self.d11)
        self.out[7] = numpy.float32(self.d12)
        self.out[8] = numpy.float32(self.e11)
        self.out[9] = numpy.float32(self.e12)


	for i in range (0,self.number):
		output_items[i][:]= self.out[i]
	print "I am out item",output_items

        return len(output_items[0])
    

