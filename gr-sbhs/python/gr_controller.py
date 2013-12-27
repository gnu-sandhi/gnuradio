import gras
import numpy
from que import *

class sbhs_controller(gras.Block):

	def __init__(self):
		gras.Block.__init__(self,
			name="sbhs_controller",
			in_sig=[numpy.float32],
			out_sig=[numpy.float32])	
		
		# Initializing  FIFO Queues
		# Remember Total_Number(Q_Push) should be equal to Total_Number(Q_Pull)

		self.q1 = Queue(3) # Queue for Error t_0 .. t_2
		self.q2 = Queue(2) # Queue for output o_0 o_1
		
		# Initial queue values
		self.t_1 = 0
		self.o_0 = 0

	def set_parameters(self,p,i,d,a,b,f):
		self.proportional = p 
		self.integtime = i
		self.derivtime = d
		self.delt = a #del_t
		self.setpt = b #set_point
		self.n = f #window
	
	def work(self, input_items, output_items):
		
		in0 = input_items[0][0]
		out = output_items[0]
		
		# Queue structure
		#  --> |0|0|0| =>  |in0|t_1|0|
		self.q1.push(self.t_1)
		self.q1.push(in0) 
		
		# Queue Structure
		# --> |0|0|  => |self.o_0|0|
		self.q2.push(self.o_0)

		# Popping
		self.t_0 = in0
		self.t_1 = self.q1.pop()
		self.t_2 = self.q1.pop()
		
		self.o_1 = self.q2.pop()
		
		# Error propogation 
		print "E(t=t)", self.t_0
		print "E(t=t-1)", self.t_1
		print "E(t=t-2)", self.t_2
		print "-------------------"
		
		# Difference Equation
		self.o_0 = ((self.proportional * (in0 - self.t_1)
                	+(self.delt/self.integtime)*in0
			+(self.derivtime/self.delt)*(in0 - 2*self.t_1
			+self.t_2 )) + self.o_1 ) * 0.92
		
		out[:1] = self.o_0
			
		self.consume(0,1) # Consumuption from port 0 input_items
		self.consume(1,1) 
	
		self.produce(0,1) # Produce from port 0 output_items
