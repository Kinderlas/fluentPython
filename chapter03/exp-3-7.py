# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/30 15:43

from types import MappingProxyType

def main():
    d = {1:'AA'}
    d_proxy = MappingProxyType(d)
    print(d_proxy[1])
    print(d_proxy.get(2, 'NULL'))
    d[2] = 'BB'
    print(d_proxy.get(2, 'NULL'))


if __name__ == '__main__':
    main()