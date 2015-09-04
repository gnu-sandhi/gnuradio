import numpy
from gnuradio import gr,gr_unittest
from gnuradio import blocks
from Response import Response
import matplotlib.pyplot as plt
class qa_response(gr_unittest.TestCase):
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
        src_data0 = (1,0,0)
        src_data1 = (1,5,3) 
        #expected_result = (0.6622645854949951, 0.6622645854949951, 0.6622645854949951)
        src0 = gr.vector_source_f(src_data0)
        src1 = gr.vector_source_f(src_data1)
        response_ref = Response(2,"step",1,50,1)
        dst = gr.vector_sink_f()
        self.tb.connect(src0,(response_ref,0))  
        self.tb.connect(src1,(response_ref,1))  
        self.tb.connect(response_ref,dst)         
        self.tb.run()
        result_data = dst.data()
        print "Result data is : ",result_data
        #plt.plot(result_data)
        #plt.show()
        #self.assertFloatTuplesAlmostEqual(expected_result,result_data,6)
        
    
if __name__ == "__main__":
    gr_unittest.main()        
        