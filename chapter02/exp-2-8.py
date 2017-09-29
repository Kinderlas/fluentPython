# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/29 16:56
import bisect
import random

def main():
    aList = [x*x for x in range(10)]
    search_list = list(range(10))

    for i in ('{:2d}'.format(x) for x in aList):
        print(i, end=' ')
    print()
    # 找到list中第一个 >key 的位置
    print([bisect.bisect(aList, x) for x in search_list])
    # 找到list中第一个 >=key 的位置
    print([bisect.bisect_left(aList, x) for x in search_list])

    grades = list(reversed(list('ABCDE')))
    points = [random.randint(40, 100) for _ in range(10)]
    break_points = [i*10 for i in range(6, 10)]
    print(points)
    for point in points:
        print(grades[bisect.bisect(break_points, point)], end=', ')
    print()

    bList = []
    for i in range(100):
        bisect.insort(bList, random.randint(1, 10))
    print(bList)


if __name__ == '__main__':
    main()