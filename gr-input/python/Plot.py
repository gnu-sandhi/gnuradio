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
from time import sleep
from collections import deque
from matplotlib import pyplot as plt
import numpy
import gras
from gnuradio import gr
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import collections
import random
import time
import math
import numpy as np
import threading
import multiprocessing
no=0
class Plot(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,sampleinterval,timewindow,num_plot):
	a = []
        for i in range(0,num_plot):
	    a.append(numpy.float32)
	size=(600,350)
	self.num_plot = num_plot
	global no
	no = num_plot
	self.ip = 0
	self.ptr1 = 0
	self.win = pg.GraphicsWindow()
        self._interval = int(sampleinterval*1000)
        self._bufsize = int(timewindow/sampleinterval)
	self.plt=[0 for x1 in range(no)]
	self.databuffer=[0 for x2 in range(no)]
	self.x=[0 for x3 in range(no)]
	self.y=[0 for x4 in range(no)]
	self.curve=[0 for x5 in range(no)]
        op=0
	while (op< self.num_plot ):
            self.plt[op] = self.win.addPlot()
            self.plt[op].showGrid(x=True, y=True)
            self.plt[op].setLabel('left', 'amplitude', 'V')
            self.plt[op].setLabel('bottom', 'time', 's')

	    self.databuffer[op] = collections.deque([0.0]*self._bufsize, self._bufsize)
	    self.x[op] = np.linspace(0.0,timewindow,self._bufsize)
            self.y[op] = np.zeros(self._bufsize, dtype=np.float)
            self.curve[op] = self.plt[op].plot(self.x[op], self.y[op], pen=(255,200,0))
	    op=op+1
	    if op<self.num_plot:
		self.win.nextRow()		
	
        gr.sync_block.__init__(self,
            name="Plot",
            in_sig=a,
            out_sig=None)

    def getdata(self,ip):
        new = ip
	print "new\n",ip
        return new

    def updateplot(self,i):
	self.databuffer[i].append(self.getdata(self.ip[i]) )
        self.y[i][:] = self.databuffer[i]
	self.curve[i].setData(self.y[i])

    def work(self, input_items, output_items):
	try:
	    i=0	
	    self.ip = []
	    while (i<no):
	   	self.ip.insert(i,input_items[i][0])
		i=i+1
	except IndexError:
	    pass
	i=0
	while (i<no):
		self.updateplot(i)
		i=i+1
	return len(input_items[0])
