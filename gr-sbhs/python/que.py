# Data Acquisition list based queue

class Queue: 
    """A sample implementation of a First-In-First-Out
       data structure."""
    def __init__(self, length):
    	
	# Initializes with empty zeros
        self.queue = [0] * length
	self.length = length

    def push(self,obj):
	if len(self.queue) < self.length:
		self.queue.append(obj)
	else:
		print "Queue full"
		
		### To discard first in queue and append obj anyway ###
		#self.queue.pop(0)
		#self.queue.append(obj)

    def pop(self):
    	try:
		return (self.queue.pop(0))
	except:
		print "queue empty"

    def size(self):
   	return len(self.queue)

    def discard(self):
   	self.queue=[]
    
    def flush(self):
    	self.return_queue = self.queue
	self.queue = []
	return(self.return_queue)
