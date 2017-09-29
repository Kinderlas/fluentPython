# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/29 16:08
import os

def main():
    t = ('username', 'passport')

    u, p = t
    print(u, p)

    _, p = t
    print(p)

    tt = ('username', 'passport', 1, 2, 3)
    u, p, *_ = tt
    print(u, p, _)

    *_, filename = os.path.abspath(__file__).split(os.sep)
    print(filename)
    *_, filename = os.path.split(os.path.abspath(__file__))
    print(filename)

if __name__ == '__main__':
    main()