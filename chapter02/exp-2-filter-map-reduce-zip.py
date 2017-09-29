# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/29 15:38

from functools import reduce


def foo(x):
    return x * x


def main():
    aList = list(range(10))
    bList = list(reversed(range(10)))
    cList = list(range(10, 20))
    print(aList)
    filter_1 = list(filter(lambda k: k % 2 == 0, aList))
    filter_None = list(filter(None, aList))
    print(filter_1)
    print(filter_None)

    map_1 = list(map(lambda x: x * x, aList))
    print(map_1)

    print([x * x for x in aList])

    reduce1 = reduce(lambda x, y: x + y, aList)
    print(reduce1)

    zip1 = list(zip(aList, bList))
    zip2 = list(zip(aList, bList, cList))
    zip3 = list(zip(*zip1))
    zip4 = list(map(list, zip(aList, bList)))
    print(zip1)
    print(zip2)
    print(zip3)
    print(zip4)


if __name__ == '__main__':
    main()
