import numpy
from gnuradio import gr,gr_unittest
from gnuradio import blocks
from Numerator import Numerator
class qa_numerator(gr_unittest.TestCase):
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
        Test Case for Number of inputs is 3 i.e Numerator order is 2 then numerator becomes s^2+s+1
        """
        src_data0 = (0,1,0)
        src_data1 = (1,5,3)
        src_data2 = (4,5,6) 
        src0 = gr.vector_source_f(src_data0)
        src1 = gr.vector_source_f(src_data1)
        src2 = gr.vector_source_f(src_data2)
        nume_ref = Numerator(2)
        dst = gr.vector_sink_f()
        self.tb.connect(src0,(nume_ref,0)) 
        self.tb.connect(src1,(nume_ref,1)) 
        self.tb.connect(src1,(nume_ref,2)) 
        self.tb.connect(nume_ref,dst)         
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
        Test Case for Number of inputs is 2 i.e Numerator order is 1 then numerator becomes s+1
        """
        src_data0 = (0,0,0)
        src_data1 = (5,6,9)
        src0 = gr.vector_source_f(src_data0)
        src1 = gr.vector_source_f(src_data1)
        nume_ref = Numerator(1)
        dst = gr.vector_sink_f()
        self.tb.connect(src0,(nume_ref,0)) 
        self.tb.connect(src1,(nume_ref,1)) 
        self.tb.connect(nume_ref,dst)         
        self.tb.run()
        result_data = dst.data()
        print "Result data is : ",result_data
       
if __name__ == "__main__":
    gr_unittest.main()        
        