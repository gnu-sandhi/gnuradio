import gras 
import numpy
from gnuradio import gr
from gnuradio import blocks

# Source block1 import
import gr_ramp_source
from gnuradio import blocks

class HierBlock(gr.hier_block2):
	def __init__(self,ramp_slope, height_Offset, width_Offset):
		gr.hier_block2.__init__(self,"HierBlock",gr.io_signature(1,1,gr.sizeof_float), gr.io_signature(1,2,gr.sizeof_float))
		#constant_block initialized
		self.constant_block = gr.sig_source_f(0,gr.GR_CONST_WAVE,0,0,1)
		#ramp_source block initialized
		self.ramp_source=gr_ramp_source.ramp()
		self.ramp_source.set_parameters(ramp_slope, height_Offset, width_Offset)
		self.connect(self,(self.constant_block,0),(self.ramp_source,0),self)

