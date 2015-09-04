import numpy
from gnuradio import gr,gr_unittest
from gnuradio import blocks
from Denominator import Denominator
class qa_denominator(gr_unittest.TestCase):
    def setUp(self):
        self.tb = gr.top_block()
    def tearDown(self):
        self.tb = None
    def test_001_t(self):
        """
        Defined source data for three incoming port
        For one port src_data0 
        For N port src_data0,src_data1,src_data2,.......,src_dataN.
        """
        """
        Test Case for Number of inputs is 3 i.e Denominator order is 2 then denominator becomes s^2+s+1
        """
        src_data0 = (0,1,1)
        src_data1 = (1,7,8)
        src_data2 = (4,5,9) 
        src0 = gr.vector_source_f(src_data0)
        src1 = gr.vector_source_f(src_data1)
        src2 = gr.vector_source_f(src_data2)
        deno_ref = Denominator(2)
        dst = gr.vector_sink_f()
        self.tb.connect(src0,(deno_ref,0)) 
        self.tb.connect(src1,(deno_ref,1)) 
        self.tb.connect(src1,(deno_ref,2)) 
        self.tb.connect(deno_ref,dst)         
        self.tb.run()
        result_data = dst.data()
        print "Result data is : ",result_data
        
    def test_002_t(self):
        """
        Defined source data for three incoming port
        For one port src_data0 
        For N port src_data0,src_data1,src_data2,.......,src_dataN.
        """
        """
        Test Case for Number of inputs is 2 i.e Denominator order is 1 then denominator becomes s+1
        """
        src_data0 = (1,4,0)
        src_data1 = (5,6,9)
        src0 = gr.vector_source_f(src_data0)
        src1 = gr.vector_source_f(src_data1)
        deno_ref = Denominator(1)
        dst = gr.vector_sink_f()
        self.tb.connect(src0,(deno_ref,0)) 
        self.tb.connect(src1,(deno_ref,1)) 
        self.tb.connect(deno_ref,dst)         
        self.tb.run()
        result_data = dst.data()
        print "Result data is : ",result_data
       
if __name__ == "__main__":
    gr_unittest.main()        
        