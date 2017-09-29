# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/29 16:25

def main():
    s = 'abcdefg'
    print(s[::2])
    print(s[::-1])
    print(s[::-2])

    aList = list(range(10))
    del aList[::2]
    print(aList)

    aList = list(range(10))
    aList[3:5] = [-1, -2]
    print(aList)
    aList[3:5] = [100]
    print(aList)
    aList[3:5] = [100, 200, 300, 400]
    print(aList)


if __name__ == '__main__':
    main()