import gras
import numpy
from gnuradio import gr
from gnuradio import blocks

# Source block1 import
import ser_functions
from gnuradio import blocks

class HierBlock(gr.hier_block2):
        def __init__(self, port, baud, bytesize, parity, stopbits):
                gr.hier_block2.__init__(self, "HierBlock", 
                        gr.io_signature(1,1,gr.sizeof_float),
                        gr.io_signature(1,2,gr.sizeof_float))

                # constant_block initialized
                self.constant_block = gr.sig_source_f(0, gr.GR_CONST_WAVE,0,0,1)
                # step_source block initialized
                self.serial_source = ser_functions.ser()
                self.serial_source.set_parameters(port, baud, bytesize, parity, stopbits)
 
                # Connect Block1 and Block2
                self.connect(self, (self.constant_block,0) , (self.serial_source,0), self)

