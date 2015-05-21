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
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.pyplot import axvline, axhline



class plzr_plot(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,order1,order2,order3,num_tf,itype):
	a = []
        for i in range(0,2*num_tf):
            a.append(numpy.float32)
	print "This is a", a
	self.i = 0
	self.max_2 = [0,0,0,0]
	self.z = []
	self.z1 = [0,0,0,0]
	self.z2 = []
	self.z3= [0,0,0,0]
	self.num_tf = num_tf
	self.itype = itype
        self.order1=int(order1)+1
	self.order2=int(order2)+1
	self.order3=int(order3)+1

	self.b = self.order1*[0]
	self.b11 = self.order1*[0]
	self.c = self.order1*[0]
	self.c11 = self.order1*[0]
	self.b1 = self.order2*[0]
	self.b12 = self.order2*[0]
	self.c1 = self.order2*[0]
	self.c12 = self.order2*[0]
	self.b2 = self.order3*[0]
	self.b21 = self.order3*[0]
	self.c2 = self.order3*[0]
	self.c21 = self.order3*[0]

        gr.sync_block.__init__(self,
            name="plzr_plot",
            in_sig=[numpy.float32,numpy.float32,numpy.float32,numpy.float32],
            out_sig=None)
	    
    def plot_cont(self,b,c):
	self.z, self.p, self.k = signal.tf2zpk(b, c) 
	plt.plot(numpy.real(self.z), numpy.imag(self.z), 'or', label='Zeros of TF 1')
        plt.plot(numpy.real(self.p), numpy.imag(self.p), 'xb', label='Poles of TF 1')
	plt.legend(loc=1,numpoints=1)

    def plot_cont1(self,b1,c1):
	
        self.z1, self.p1, self.k1 = signal.tf2zpk(b1, c1)
	plt.plot(numpy.real(self.z1), numpy.imag(self.z1), 'og', label='Zeros of TF2')
        plt.plot(numpy.real(self.p1), numpy.imag(self.p1), 'xm', label='Poles of TF2')
	plt.legend(loc=1,numpoints=1)

    def plot_cont2(self,b2,c2):
        self.z2, self.p2, self.k2 = signal.tf2zpk(b2, c2)
	plt.plot(numpy.real(self.z2), numpy.imag(self.z2), 'oy', label='Zeros of TF3')
        plt.plot(numpy.real(self.p2), numpy.imag(self.p2), 'xk', label='Poles of TF3')
	plt.legend(loc=1,numpoints=1)

    def common_plot_cont(self):

	ax = plt.subplot(1, 1, 0)
	axvline(0, color='0.7')
	axhline(0, color='0.7') 
	plt.title('Pole / Zero Plot')
	plt.ylabel('Real')
	plt.xlabel('Imaginary')
	plt.grid()
	
    def common_plot_dist(self):
	
        ax = plt.subplot(1, 1, 0)
	unit_circle = patches.Circle((0,0), radius=1, fill=False,
        color='black', ls='solid', alpha=0.1)
	ax.add_patch(unit_circle)
        axvline(0, color='0.7')
        axhline(0, color='0.7')
        plt.title('Pole / Zero Plot')
        plt.ylabel('Real')
        plt.xlabel('Imaginary')
        plt.grid()

	
    def work(self, input_items, output_items):
	k1 = self.order1
	k2 = self.order2
	k3 = self.order3

	try:
		for i in range(0,k1):
		    self.b[i] = input_items[0][i]
	        v1 = 0
	        for i2 in reversed(self.b):
	            self.b11[v1]=i2
	            v1 = v1 + 1
       		print "I am z1\n",self.b11


	except IndexError:
		pass

	try:	
		for j in range(0,k1):
		    self.c[j] = input_items[1][j]
	        v = 0
	        for i3 in reversed(self.c):
	            self.c11[v] = i3
	            v = v + 1
	        print "I  am z3\n", self.c11
        except IndexError:
	        pass
	
	try:

		for i in range(0,k2):
           		 self.b1[i] = input_items[2][i]
                v1 = 0
                for i2 in reversed(self.b1):
                    self.b12[v1]=i2
	except IndexError:
		pass
	try:
        	for j in range(0,k2):
            		self.c1[j] = input_items[3][j]
                v = 0
                for i3 in reversed(self.c1):
                    self.c12[v] = i3
                    v = v + 1


        except IndexError:
		pass
	try:
        	for i in range(0,k3):
            		self.b2[i] = input_items[4][i]
                v1 = 0
                for i2 in reversed(self.b2):
                    self.b21[v1]=i2
                    v1 = v1 + 1

	except IndexError:
		pass
	try:
        	for j in range(0,k3):
            		self.c2[j] = input_items[5][j]
                v = 0
                for i3 in reversed(self.c2):
                    self.c21[v] = i3
                    v = v + 1

	except IndexError:
		pass

	if (self.itype == 12):
		self.common_plot_cont()
		
	else:
		self.common_plot_dist()
	if self.num_tf == 1:
                self.plot_cont(self.b11,self.c11)

		self.z11 = [abs(k11) for k11 in self.z]
		self.z22 = max(self.z11)
		self.p11 = [abs(k22) for k22 in self.p]
		self.p22 = max(self.p11)
		
		if(z22 > p22):
			limit = self.z22 + 1
		else:
			limit = self.p22 + 1
		plt.ylim([-limit,limit])
		plt.xlim([-limit,limit])
		plt.ion()
		plt.draw()
	elif self.num_tf == 2:
		self.plot_cont(self.b11,self.c11)
		self.plot_cont1(self.b12,self.c12)
                self.z11 = [abs(k11) for k11 in self.z]
		try:
	                self.z22 = max(self.z11)
		except ValueError:
			self.z22 = 0
                self.p11 = [abs(k22) for k22 in self.p]
                self.p22 = max(self.p11)

                self.z21 = [abs(k21) for k21 in self.z1]
		try:
	                self.z32 = max(self.z21)
		except ValueError:
			self.z32 = 0
                self.p21 = [abs(k32) for k32 in self.p1]
                self.p32 = max(self.p21)

		self.max_2[0] = self.z22
		self.max_2[1] = self.p22
		self.max_2[2] = self.z32
		self.max_2[3] = self.p32
		limit = max(self.max_2)
		plt.ylim([-limit,limit])
                plt.xlim([-limit,limit])



		plt.ion()
		plt.draw()
	else:
		self.plot_cont(self.b11,self.c11)
		self.plot_cont1(self.b12,self.c12)
		self.plot_cont2(self.b21,self.c21)
		plt.ion()
		plt.draw()
		
	plt.clf()	
        in0 = input_items[0]
        # <+signal processing here+>
        return len(input_items[0])

