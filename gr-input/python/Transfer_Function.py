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

class Transfer_Function(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,order,itype,tstart,tstop,tstep):
	a = []
	self.b = [0,0,0,0,0,0]
	self.c = [0,0,0,0,0,0]
	self.i = 0
        self.order=int(order)+1
	self.itype = itype
	self.tstart = tstart
	self.tstop  = tstop
	self.tstep  = tstep
        gr.sync_block.__init__(self,
            name="tf_rises",
            in_sig=[numpy.float32,numpy.float32],
            out_sig=[numpy.float32])
	    
	#print "I am over slept"
        #print len(self.ret_array)

    def find_resp(self,b,c):
        if (self.itype == 11):
            typo = "'imp'"
        elif (self.itype == 12):
            typo = "'step'"
        else:
            typo = "t"
#        print "self b",self.b
        string1 = "s=%s; h=syslin('c',"
        string2 = str(b[4])+"*s^4+"+str(b[3])+"*s^3+"+str(b[2])+"*s^2+"+str(b[1])+"*s+"+str(b[0])+","
        string3 = str(c[4])+"*s^4+"+str(c[3])+"*s^3+"+str(c[2])+"*s^2+"+str(c[1])+"*s+"+str(c[0])+");"
        string4 = "t="+str(self.tstart)+":"+str(self.tstep)+":"+str(self.tstop)+";"
        string5 = "deff('u=input(t)','u=50');"
        string6 = "r=tf2ss(h); a=csim("+typo+",t,r);"
        string = string1+string2+string3+string4+string5+string6
        print "I am strin g",string
        sciscipy.eval(string)
        self.a = sciscipy.read("a")
        print "value of a\n",self.a





    def work(self, input_items, output_items):

        print "input value:\n",input_items
	for i in range(0,5):
	    self.b[i] = input_items[0][i]
	#    print "I am b[i]", b[i]
	#print "I am BBBBB", self.b
	
	for j in range(0,5):
	    self.c[j] = input_items[1][j]
	    #print "I am c[j]", c[j]
	#print "I am CCCCC", self.c
	self.find_resp(self.b,self.c)	
	
	
        out = output_items[0]
        self.i+=1
        print "I am self i\n",self.i
        if self.i >= len(self.a):
            self.i = 0
        print "len of out\n",len(out)
        #time.sleep(0.125)
        out[:] = numpy.float32(self.a[self.i])
        #print 
        print "i am out\n",out
        
        return len(output_items[0])
    

