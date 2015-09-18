import numpy
import numpy as np
import scipy as sp
from gnuradio import gr
import matplotlib
from control import *
from control.freqplot import default_frequency_range
from numpy import pi
import os
import wx
import gnuradio.grc.gui
import pylab
import scipy
import control.config
from control.ctrlutil import unwrap
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import gnuradio.wxgui.plot as plot
import matplotlib.animation as animation
temp = ''
class Bode(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,parent,title,order):
		a = []
		self.count = 1
		self.parent = parent
		self.title = title
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
	        self.win = BodePlot(parent)

    def work(self, input_items, output_items):
    	global temp
    	if (self.count == 1):
    		temp = input_items+list()
    	bool = not(np.allclose(temp,input_items))
    	parent = self.parent
    	title = self.title
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
		if ( bool or self.count == 1 ):
			try:
				self.win.plot(tf(self.z1,self.z3),None,True,True,True,True)
			except:
				pass
		self.count = 0
		print "Counter",self.i
		self.i+=1
		in0 = input_items[0]
		temp = input_items+list()
		return len(input_items[0])

class BodePlot(wx.Panel):
	def __init__(self, parent, dB=None, Hz=None, deg=None):
		wx.Panel.__init__(self , parent , -1 ,size=(600,475))
		self.fig = Figure()
		self.axes1 = self.fig.add_subplot(211)
		self.axes1.grid(True , color='gray')
		self.axes1.set_ylabel("Magnitude (dB)" if dB else "Magnitude")
		self.axes2 = self.fig.add_subplot(212)
		self.axes2.grid(True , color='gray')
		self.axes2.set_ylabel("Phase (deg)" if deg else "Phase (rad)")
		self.axes2.set_xlabel("Frequency (Hz)" if Hz else "Frequency (rad/sec)")

	def plot(self, syslist, omega=None, dB=None, Hz=None, deg=None, Plot=True, *args , **kwargs):
		self.axes1.clear()
		self.axes1.grid(True , color='gray')
		self.axes1.set_ylabel("Magnitude (dB)" if dB else "Magnitude")		
		self.axes2.clear()
		self.axes2.grid(True , color='gray')
		self.axes2.set_ylabel("Phase (deg)" if deg else "Phase (rad)")
		self.axes2.set_xlabel("Frequency (Hz)" if Hz else "Frequency (rad/sec)")
		if (dB is None):
			dB = control.config.bode_dB
		if (deg is None):
			deg = control.config.bode_deg
		if (Hz is None):
			Hz = control.config.bode_Hz
		if (not getattr(syslist, '__iter__', False)):
			syslist = (syslist,)
		mags, phases, omegas = [], [], []
		if (omega == None):
			omega = default_frequency_range(syslist)
		mag_tmp, phase_tmp, omega = syslist[0].freqresp(omega)
		mag = np.atleast_1d(np.squeeze(mag_tmp))
		phase = np.atleast_1d(np.squeeze(phase_tmp))
		phase = unwrap(phase)
		if Hz: omega = omega/(2*sp.pi)
		if dB: mag = 20*sp.log10(mag)
		if deg: phase = phase * 180 / sp.pi
		mags.append(mag)
		phases.append(phase)
		omegas.append(omega)
		if dB:
			self.axes1.semilogx(omega,mag,*args,**kwargs)
		else:
			self.axes1.loglog(omega,mag,*args,**kwargs)
		self.axes2.semilogx(omega,phase,*args,**kwargs)
		self.canvas = FigCanvas(self, -1, self.fig)
		self.canvas.draw()
