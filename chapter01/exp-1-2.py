# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/28 18:41
from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x , self.y - other.y)

    # vector * scalar
    def __mul__(self, scalar):
        return Vector(self.x * scalar , self.y * scalar)

    # scalar * vector
    def __rmul__(self, scalar):
        return Vector(self.x * scalar , self.y * scalar)

    # ipython
    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    # print
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

def main():
    v1 = Vector(2, 4)
    v2 = Vector(1, 3)
    v3 = Vector(1, 3)
    print(v1 + v2)
    print(v1 - v2)
    print(v2 == v3)
    print(v2 * 2)
    print(2 * v2)


if __name__ == '__main__':
    main()