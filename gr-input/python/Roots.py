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
from numpy.polynomial import Polynomial as P

class Roots(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,order):
	self.out = [0,0,0,0,0,0,0,0,0,0]
	a = []
	z = []
	self.rev = (order+1) * [0]
	self.zreal = (order+1) * [0]
	self.zimag = (order + 1) * [0]
	self.b = [0,0,0,0,0,0]
        self.order=int(order)+1
	self.number = int(order)*2
	for i in range(0,self.number):
	    a.append(numpy.float32)
        gr.sync_block.__init__(self,
            name="Roots",
            in_sig=[numpy.float32],
            out_sig=a)
    
    def find_roots(self,numpol):
	print " i am numpol\n",numpol
	p = P(numpol)
	z=p.roots()
	self.zreal=z.real
	self.zimag=z.imag
	del self.rev[:]
	print "i am real root\n",self.zreal
	print" i am imaginary root\n",self.zimag
        

    def work(self, input_items, output_items):

#	print "I am here\n", output_items
	k = self.order
	for i in range(0,k):
	    self.b[i] = input_items[0][i]
        self.find_roots(self.b)		
	try:
            self.out[0] = numpy.float32(self.zreal[0])
	except IndexError:
            pass
        try:
            self.out[1] = numpy.float32(self.zimag[0])
	except IndexError:
            pass
        try:
            self.out[2] = numpy.float32(self.zreal[1])
	except IndexError:
            pass
        try:
	    self.out[3] = numpy.float32(self.zimag[1])
	except IndexError:
            pass
	try:
            self.out[4] = numpy.float32(self.zreal[2])
	except IndexError:
            pass
	try:
            self.out[5] = numpy.float32(self.zimag[2])
	except IndexError:
            pass
	try:
            self.out[6] = numpy.float32(self.zreal[3])
	except IndexError:
            pass
	try:
            self.out[7] = numpy.float32(self.zimag[3])
	except IndexError:
            pass
	try:
            self.out[8] = numpy.float32(self.zreal[4])
	except IndexError:
            pass        
	try:
	    self.out[9] = numpy.float32(self.zimag[4])
	except IndexError:
            pass


	for i in range (0,self.number):
		output_items[i][:]= self.out[i]
	print "I am out item",output_items

        return len(output_items[0])
    

