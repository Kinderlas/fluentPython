# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/29 17:28

from array import  array
import random
import time
import numpy as np
from collections import deque

def _array():
    st = time.time()
    double_floats = array('d', (random.random()
                                for _ in range(10**7)))
    print(double_floats[-1])
    print('gen time:', time.time() - st)
    st = time.time()
    with open('a.txt', 'wb') as f:
        double_floats.tofile(f)
    print('bin time:', time.time() - st)

    st = time.time()
    double_floats2 = array('d')
    with open('a.txt', 'rb') as f:
        double_floats2.fromfile(f, 10**7)
    print(double_floats2[-1])
    print('read time:', time.time() - st)

def _memory_view():
    aList = array('h', [i for i in range(8)])
    memv = memoryview(aList)
    print(len(memv))
    print(memv[-1])
    memv_oct = memv.cast('B')
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(memv.tolist())

def _numpy():
    a = np.arange(12)
    print(a)
    print(a.shape)
    a.shape = 3, 4
    print(a)
    print(a[2])
    print(a[2, 1])
    print(a[:, 1])
    print(a.transpose())
    a[2] *= 3
    print(a)
    a[:, 1] *= 3
    print(a)

def _deque():
    dq = deque(range(10), maxlen=10)
    print(dq)
    dq.rotate(3)
    print(dq)
    dq.rotate(-3)
    print(dq)
    dq.append('aa')
    print(dq)
    dq.pop()
    print(dq)
    dq.extend(list('ABCD'))
    print(dq)
    dq.extendleft(range(15))
    print(dq)


if __name__ == '__main__':
    _deque()
