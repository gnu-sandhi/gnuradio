"""
$$

Modified for working as a GNU Radio block
Rakesh Peter (rakesh.peter@gmail.com)
Last modified: 07.05.2010

$$

This demo demonstrates how to draw a dynamic mpl (matplotlib) 
plot in a wxPython application.

It allows "live" plotting as well as manual zooming to specific
regions.

Both X and Y axes allow "auto" or "manual" settings. For Y, auto
mode sets the scaling of the graph to see all the data points.
For X, auto mode makes the graph "follow" the data. Set it X min
to manual 0 to always see the whole data from the beginning.

Note: press Enter in the 'manual' text box to make a new value 
affect the plot.

Eli Bendersky (eliben@gmail.com)
License: this code is in the public domain
Last modified: 31.07.2008
"""

import os
import pprint
import random
import sys
import wx
import gnuradio.grc.gui
from gnuradio.grc.gui import Actions,ActionHandler
# The recommended way to use wx with mpl is with the WXAgg
# backend. 
#
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
    FigureCanvasWxAgg as FigCanvas, \
    NavigationToolbar2WxAgg as NavigationToolbar
import numpy as np
import pylab


class DataGen(object):
    """ A silly class that generates pseudo-random data for
        display in the plot.
    """
    def __init__(self, init=50):
        self.data = self.init = init
        
    def next(self):
        self._recalc_data()
    #return self.data
        return [0.0,1.1,2.2,3.3]
    
    def _recalc_data(self):
        delta = random.uniform(-0.5, 0.5)
        r = random.random()

        if r > 0.9:
            self.data += delta * 15
        elif r > 0.8: 
            # attraction to the initial value
            delta += (0.5 if self.init > self.data else -0.5)
            self.data += delta
        else:
            self.data += delta



class matplotsink(wx.Panel):
  
    def __init__(self, parent, title, queue,gsz,zoom):
         wx.Panel.__init__(self, parent, wx.SIMPLE_BORDER)
        
	 self.gsz = gsz
         self.parent = parent
         self.title = title
         self.q = queue
	 self.zoom=zoom
         self.paused = False
       
#        self.create_menu()
#        self.create_status_bar()
         self.create_main_panel()
	 

    def create_menu(self):
        self.menubar = wx.MenuBar()
        
        menu_file = wx.Menu()
        m_expt = menu_file.Append(-1, "&Save plot\tCtrl-S", "Save plot to file")
        self.Bind(wx.EVT_MENU, self.on_save_plot, m_expt)
        menu_file.AppendSeparator()
        m_exit = menu_file.Append(-1, "E&xit\tCtrl-X", "Exit")
        self.Bind(wx.EVT_MENU, self.on_exit, m_exit)
        self.menubar.Append(menu_file, "&File")
        self.SetMenuBar(self.menubar)


    def create_main_panel(self):
        self.panel = self

        self.init_plot()
        self.canvas = FigCanvas(self.panel, -1, self.fig)
	self.scroll_range = 400
	self.canvas.SetScrollbar(wx.HORIZONTAL,0,5,self.scroll_range)
	self.canvas.Bind(wx.EVT_SCROLLWIN,self.OnScrollEvt)
	
        
        self.pause_button = wx.Button(self.panel, -1, "Pause")
        self.Bind(wx.EVT_BUTTON, self.on_pause_button, self.pause_button)
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_pause_button, self.pause_button)
        
        self.cb_grid = wx.CheckBox(self.panel, -1, 
            "Show Grid",
            style=wx.ALIGN_RIGHT)
        self.Bind(wx.EVT_CHECKBOX, self.on_cb_grid, self.cb_grid)
        self.cb_grid.SetValue(True)
        
        self.cb_xlab = wx.CheckBox(self.panel, -1, 
            "Show X labels",
            style=wx.ALIGN_RIGHT)
        self.Bind(wx.EVT_CHECKBOX, self.on_cb_xlab, self.cb_xlab)        
        self.cb_xlab.SetValue(True)
        
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox1.Add(self.pause_button, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.AddSpacer(20)
        self.hbox1.Add(self.cb_grid, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox1.AddSpacer(10)
        self.hbox1.Add(self.cb_xlab, border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        
        
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.canvas, 1, flag=wx.LEFT | wx.TOP | wx.GROW)        
        self.vbox.Add(self.hbox1, 0, flag=wx.ALIGN_LEFT | wx.TOP)
        
        self.panel.SetSizer(self.vbox)
        self.vbox.Fit(self)
	self.ani=animation.FuncAnimation(self.fig,self.draw_plot,interval=100)
    
    def OnScrollEvt(self,event):
	self.i_start = event.GetPosition()
	self.i_end =  self.i_window + event.GetPosition()
	self.draw_plot(0)
	
    def create_status_bar(self):
        self.statusbar = self.CreateStatusBar()

    def draw_test(self,event):
	self.xar=np.arange(len(self.q.queue))
        self.yar=np.array(self.q.queue)
	self.axes.plot(self.xar,self.yar)

    def init_plot(self):
        self.dpi = 100
 	self.fig = Figure((3.0, 3.0), dpi=self.dpi)
        self.fig.set_size_inches(7.0,4.0)
        self.fig.set_dpi(self.dpi)

        self.axes = self.fig.add_subplot(111)
        self.axes.set_axis_bgcolor('black')
        self.axes.set_title(self.title, size=12)
        
        pylab.setp(self.axes.get_xticklabels(), fontsize=8)
        pylab.setp(self.axes.get_yticklabels(), fontsize=8)
	self.i_window = self.gsz
	self.i_start = 0
	self.i_end = self.i_start + self.i_window
        # plot the data as a line series, and save the reference 
        # to the plotted line series
        #
        self.plot_data = self.axes.plot(
             [], 
             linewidth=1,
             color=(1, 1, 0),
             )[0]

     
    def draw_plot(self,event):
         """ Redraws the plot
         """
	 if len(list(self.q.queue))>1 and not self.paused:

             if self.zoom:
                 xmax = len(list(self.q.queue)) if len(list(self.q.queue)) > 50 else 50
               
                 xmin = xmax - 50
                 # for ymin and ymax, find the minimal and maximal values
                 # in the data set and add a mininal margin.
                 # 
                 # note that it's easy to change this scheme to the 
                 # minimal/maximal value in the current display, and not
                 # the whole data set.
                 # 
                 ymin = round(min(list(self.q.queue)), 0) - 1
            
                 ymax = round(max(list(self.q.queue)), 0) + 1

                 self.axes.set_xbound(lower=xmin, upper=xmax)
                 self.axes.set_ybound(lower=ymin, upper=ymax)
           
                 # anecdote: axes.grid assumes b=True if any other flag is
                 # given even if b is set to False.
                 # so just passing the flag into the first statement won't
                 # work.
                 #
                 if self.cb_grid.IsChecked():
                     self.axes.grid(True, color='gray')
                 else:
                     self.axes.grid(False)

                 # Using setp here is convenient, because get_xticklabels
                 # returns a list over which one needs to explicitly 
                 # iterate, and setp already handles this.
                 #  
                 pylab.setp(self.axes.get_xticklabels(), 
                 visible=self.cb_xlab.IsChecked())

            
                 self.plot_data.set_xdata(np.arange(len(list(self.q.queue))))
                 self.plot_data.set_ydata(np.array(list(self.q.queue)))
                 self.canvas.draw()
        	
             else: 
    	         if self.cb_grid.IsChecked():
    	             self.axes.grid(True, color='gray')
    	         else:
            	     self.axes.grid(False)

           		 # Using setp here is convenient, because get_xticklabels
            	 # returns a list over which one needs to explicitly 
    	         # iterate, and setp already handles this.

    	         pylab.setp(self.axes.get_xticklabels(), 
            	 visible=self.cb_xlab.IsChecked())
    		 
    	         self.plot_data.set_xdata(np.arange(len(list(self.q.queue)))[self.i_start:self.i_end])
            	 self.plot_data.set_ydata(np.array(list(self.q.queue))[self.i_start:self.i_end])
    		 self.axes.set_xlim(min(np.arange(len(list(self.q.queue)))[self.i_start:self.i_end]),max(np.arange(len(list(self.q.queue)))[self.i_start:self.i_end]))
    #		 if self.zoom:
    	  	 self.axes.set_ylim(min(np.array(list(self.q.queue))),max(np.array(list(self.q.queue))))
    		 
    		 self.canvas.draw()


    
    def on_pause_button(self, event):
        self.paused = not self.paused
    
    def on_update_pause_button(self, event):
        label = "Resume" if self.paused else "Pause"
        self.pause_button.SetLabel(label)
    
    def on_cb_grid(self, event):
        self.draw_plot(0)
    
    def on_cb_xlab(self, event):
        self.draw_plot(0)
    
    def on_save_plot(self, event):
        file_choices = "PNG (*.png)|*.png"
        
        dlg = wx.FileDialog(
            self, 
            message="Save plot as...",
            defaultDir=os.getcwd(),
            defaultFile="plot.png",
            wildcard=file_choices,
            style=wx.SAVE)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.canvas.print_figure(path, dpi=self.dpi)
            self.flash_status_message("Saved to %s" % path)
    
    def on_redraw_timer(self, event):
        # if paused do not add data, but still redraw the plot
        # (to respond to scale modifications, grid change, etc.)
        #
        if not self.paused:
            self.data += self.datagen.next()
        self.draw_plot(0)

    
    def on_exit(self, event):
        self.Destroy()
    
    def flash_status_message(self, msg, flash_len_ms=1500):
        self.statusbar.SetStatusText(msg)
        self.timeroff = wx.Timer(self)
        self.Bind(
            wx.EVT_TIMER, 
            self.on_flash_status_off, 
            self.timeroff)
        self.timeroff.Start(flash_len_ms, oneShot=True)
    
    def on_flash_status_off(self, event):
        self.statusbar.SetStatusText('')

	



