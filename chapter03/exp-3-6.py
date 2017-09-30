# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/30 15:40
from collections import UserDict

class StrKeyDict(UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self.data[str(key)]

    def __setitem__(self, key, value):
        self.data[str(key)] = value

    def __contains__(self, item):
        return str(item) in self.data

def main():
    d = StrKeyDict({str(key):key*key for key in range(10)})
    print(d)
    print(d[1])
    print(d[9])
    print(d.get(1, -1))
    print(d.get(-1, -1))
    print(1 in d)

if __name__ == '__main__':
    main()
