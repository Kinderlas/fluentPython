# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/29 16:46

def main():
    aList = 'aaa bbb aab bba aca aaaa bbbb aaab'.split()
    print(sorted(aList))
    print(sorted(aList, key=len))
    print(sorted(aList, key=lambda x: (len(x), str(x))))
    print(sorted(aList, key=lambda x: (len(x), str(x)),
                 reverse=True))
    print(aList)
    print(aList.sort())
    print(aList)

    aList = [1, 2, 3, '4', '02', '33', 45, 55, '101']
    print(sorted(aList, key=int))
    print(sorted(aList, key=str))


if __name__ == '__main__':
    main()