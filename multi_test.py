#encoding=utf-8
from multiprocessing import current_process
from multiprocessing import Process
from multiprocessing import Lock
from multiprocessing import TimeoutError
from multiprocessing import Manager
#from multiprocessing import Pool
#from multiprocessing import Pipe

import random
import time
import os

#import param_server
import net
import util


process_cnt = 8
file_cnt = 10
commu_batch = 1000


def file_feed():
    res = ["data/" + str(i) + ".txt" for i in xrange(file_cnt)]
    random.shuffle(res)
    return res
    
def push_param(n, w_share, lock):
    with lock:
        for index in range(net.dim_num):
            w_share[index] -= n.grad[index]

def fetch_param(n, w_share, lock):
    with lock:
        for i in range(net.dim_num):
            n.w[i] = w_share[i]
    n.init_grad()

def process(w_share, file_share, lock, f_lock):
    with f_lock:
        if len(file_share) < 1:
            return -1
        pick_file = file_share.pop()

    n = net.Net()
    fetch_param(n, w_share, lock)
    datas = util.read_data(pick_file)
    iter_commu_batch = 0
    for i in datas:
        iter_commu_batch += 1
        n.cal_grad(i)
        if iter_commu_batch % commu_batch == 0:
            push_param(n, w_share, lock)
            fetch_param(n, w_share, lock)

    print current_process().name + '-' + pick_file

if __name__ == "__main__":
    with Manager() as manager:
        w_share = manager.list([random.uniform(-0.1, 0.1) for i in xrange(net.dim_num)])
        file_share = manager.list(file_feed())
        lock = Lock()
        f_lock = Lock()
        jobs = []
        while len(file_share) > 0:
            for i in xrange(process_cnt):
                p = Process(target=process, args=(w_share, file_share, lock, f_lock))
                jobs.append(p)
                p.start()
            
            for i in jobs:
                i.join()
            jobs = []
        print w_share
        print "process done."
