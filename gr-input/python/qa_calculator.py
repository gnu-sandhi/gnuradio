import numpy
from gnuradio import gr,gr_unittest
from gnuradio import blocks
from Calculator import Calculator
class qa_calculator(gr_unittest.TestCase):
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
        src_data0 = (5,7,8)
        src_data1 = (6,7,3) 
        src_data2 = (8,2,2)
            
        expected_result = (3,12,9)
        src0 = gr.vector_source_f(src_data0)
        src1 = gr.vector_source_f(src_data1)
        src2 = gr.vector_source_f(src_data2)
        cal_ref = Calculator("a0+a1-a2",3)
        dst = gr.vector_sink_f()
        self.tb.connect(src0,(cal_ref,0))  # connection from First block to Calculator block  1stconstants_source_block --> to Calculator_block
        self.tb.connect(src1,(cal_ref,1))  # connection from Second block to Calculator block 2ndconstants_source_block --> to Calculator_block
        self.tb.connect(src2,(cal_ref,2))  # connection from Third block to Calculator block  3rdconstants_source_block --> to Calculator_block
        self.tb.connect(cal_ref,dst)       # connection from Calculator block to sink_block    Calculator_block --> Sink_Block (Here WxNumberSink)  
        self.tb.run()
        result_data = dst.data()
        print "Result data is : ",result_data
        self.assertFloatTuplesAlmostEqual(expected_result,result_data,6)
        
    def test_002_t(self):
        """
        Defined source data for three incoming port
        For one port src_data0 
        For N port src_data0,src_data1,src_data2,.......,src_dataN.
        """
        src_data0 = (1,2,3,1)
        src_data1 = (2,7,3,0) 
        src_data2 = (1,2,2,3)
        src_data3 = (25,16,4,81)
        expected_result = (8,20,13,12)
        src0 = gr.vector_source_f(src_data0)
        src1 = gr.vector_source_f(src_data1)
        src2 = gr.vector_source_f(src_data2)
        src3 = gr.vector_source_f(src_data3)
        cal_ref = Calculator("(a0*a1)+a2+sqrt(a3)",4)
        dst = gr.vector_sink_f()
        self.tb.connect(src0,(cal_ref,0))  
        self.tb.connect(src1,(cal_ref,1)) 
        self.tb.connect(src2,(cal_ref,2)) 
        self.tb.connect(src3,(cal_ref,3)) 
        self.tb.connect(cal_ref,dst)         
        self.tb.run()
        result_data = dst.data()
        print "Result data is : ",result_data
        self.assertFloatTuplesAlmostEqual(expected_result,result_data,6)

if __name__ == "__main__":
    gr_unittest.main()        
        