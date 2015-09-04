import numpy
from gnuradio import gr,gr_unittest
from gnuradio import blocks
from Max_val import Max_val
class qa_maxval(gr_unittest.TestCase):
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
        src_data0 = (1,2,3)
        #expected_result = (1,2,3)
        src0 = gr.vector_source_f(src_data0)
        max_val = Max_val(1,10,1)
        dst = gr.vector_sink_f()
        self.tb.connect(src0,max_val)  
        self.tb.connect(max_val,dst)         
        self.tb.run()
        result_data = dst.data()
        print "Result data is : ",result_data
        #self.assertFloatTuplesAlmostEqual(expected_result,result_data,6)
        
    
if __name__ == "__main__":
    gr_unittest.main()        
        