import gras
import numpy
from gnuradio import gr
from gnuradio import blocks

# Source block1 import
import gr_step_source
from gnuradio import blocks

class HierBlock(gr.hier_block2):
        def __init__(self, step_size, H_Off, W_Off):
                gr.hier_block2.__init__(self, "HierBlock", 
                        gr.io_signature(1,1,gr.sizeof_float),
                        gr.io_signature(1,2,gr.sizeof_float))

                # constant_block initialized
                self.constant_block = gr.sig_source_f(0, gr.GR_CONST_WAVE,0,0,1)
                # step_source block initialized
                self.step_source = gr_step_source.step()
                self.step_source.set_parameters(step_size, H_Off, W_Off)
                self.connect(self, (self.constant_block,0) , (self.step_source,0), self)

