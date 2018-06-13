import copy
import random

dim_num = 10

#[0.06631586145491863, -0.944620975795994, 0.25498501465302703, 0.014401932031731235, -0.7591292495364039, 0.0683147392938952, -0.5286976659986529, -0.9301037633258202, 0.7256813654905556, -0.1312924677385343]

class Net(object):
    def __init__(self):
        self.w = [random.uniform(-0.1, 0.1) for i in xrange(dim_num)]
        #self.b = random.uniform(-0.1, 0.1)
        self.grad = [0 for i in xrange(dim_num)]
        self.lr = 0.001

    def train(self, data):
        self.cal_grad(data)
        
        self.update_param()

    def cal_grad(self, data):
        y = 0
        for index in xrange(dim_num):
            y += self.w[index] * data[0][index]

        delta_y = y - data[1]
        for index, grad_i in enumerate(self.grad):
            self.grad[index] += self.lr * delta_y * data[0][index]

    def update_param(self):
        for index, wi in enumerate(self.w):
            self.w[index] -= self.grad[index]
        self.init_grad()
 
    def init_grad(self):
        self.grad = [0 for i in xrange(dim_num)]

if __name__ == "__main__":
    net = Net()
    print net.w
        
