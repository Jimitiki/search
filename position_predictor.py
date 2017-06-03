import time
import numpy

class position_predictor:
    def __init__(self):
        self.position = None
        self.velocity = None
        self.time = None
        
    def update_position(self, new_position):
        if self.time == None:
            self.time = time.time()            
        else:        
            delta_time = time.time() - self.time
            self.time = time.time()
            self.velocity = [x / delta_time for x in numpy.subtract(new_position, self.position)]
        self.position = new_position        
        
    def prediction(self, delta_time):
        return numpy.add(self.position, [x * delta_time for x in self.velocity])