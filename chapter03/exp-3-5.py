# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/30 15:26

from collections import Counter

def main():
    counter = Counter()
    counter.update('ablasdkjlasdfj')
    print(counter)
    counter.update([11,22,33])
    print(counter)
    counter.update(['aaa', 'bbb', 'ccc'])
    print(counter)
    print(counter.most_common(3))


if __name__ == '__main__':
    main()