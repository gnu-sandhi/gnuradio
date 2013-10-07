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
from generic import *


class qa_generic (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
    	
    	src0 = numpy.arange(0,3.1416,1)

	src0 = gr.vector_source_f(src0)
	expected_result = (0.0, 0.8414709568023682, 0.9092974066734314, 0.14112000167369843)

	sqr = generic()
	sqr.set_parameters("sin",1)

	dst = gr.vector_sink_f()
	
	self.tb.connect(src0, (sqr,0)) # src0(vector_source) -> sqr_input_0
	self.tb.connect(sqr,dst) # sqr_output_0 -> dst (vector_source)

	self.tb.run()

	result_data = dst.data()
	print result_data, "Result data"
	
   	self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)
	

if __name__ == '__main__':
    gr_unittest.main()
