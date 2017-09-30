# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/30 14:51

class StrKeyDict(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, k, default=None):
        return self[k] if k in self else default

    #def get(self, k, default=None):
        # try:
        #     return self[k]
        # except KeyError:
        #     return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()

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