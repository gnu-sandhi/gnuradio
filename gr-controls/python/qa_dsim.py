#!/usr/bin/env python
# 
# Copyright 2013 <+YOU OR YOUR COMPANY+>.
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

from gnuradio import gr, gr_unittest
#import mymod_swig as mymod
from dsim import dsim


class qa_dsim (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
    	
    	src_data = [0]*100
	src_data1 = [1]*1000
	src_data = tuple(src_data+src_data1)
 	
	expected_result = (-2.0, 0.0, 5.0, 8.0, 9.0, 11.0, 14.0, 18.0)
	
	src0 = gr.vector_source_f(src_data)
	sqr = dsim()
	sqr.set_parameters(2,0.5,0.6,1,1, 0.1, 2, 1, 1100)

	#Preload
	sqr.input_config(1).preload_items = 1
	dst = gr.vector_sink_f()
	
	self.tb.connect(src0, (sqr,0)) # src0(vector_source) -> sqr_input_0
	self.tb.connect(sqr,dst) # sqr_output_0 -> dst (vector_source)

	self.tb.run()

	result_data = dst.data()
	
	import  matplotlib.pyplot as plt
    	plt.plot(result_data)
    	plt.show()
   	#self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)
	

if __name__ == '__main__':
    gr_unittest.main()
   #gr_unittest.run(qa_dsim, "qa_dsim.xml")
