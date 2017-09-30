# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/30 15:50

from unicodedata import name

def main():
    n = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
    print(n)


if __name__ == '__main__':
    main()