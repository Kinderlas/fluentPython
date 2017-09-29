# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/29 16:37

def main():
    l = [1, 2, 3]
    print(id(l))
    l *= 2  # l = l * 2
    print(l)
    print(id(l))
    t = (1, 2, 3)
    print(id(t))
    t *= 2
    print(t)
    print(id(t))

    k = [1, 2, [3, 4]]
    print(k)
    k[2] += [5, 6]
    print(k)

    k = (1, 2, [3, 4])
    print(k)
    try:
        k[2] += [5, 6]
    except:
        pass
    print(k)

    k = (1, 2, (3, 4))
    print(k)
    try:
        k[2] += (5, 6)
    except:
        pass
    print(k)



if __name__ == '__main__':
    main()
