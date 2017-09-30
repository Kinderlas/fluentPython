# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/30 11:22
import re
import os
from collections import defaultdict

WORD_RE = re.compile(r'\w+')

index = {}

def _defaultdict():
    index = defaultdict(list)
    with open(os.path.join('data', 'zen.txt'), 'r') as f:
        for line_no, line in enumerate(f):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start()+1
                location = (line_no, column_no)
                index[word].append(location)
    for key in index:
        print("{}:{}".format(key, index[key]))

def best():
    with open(os.path.join('data', 'zen.txt'), 'r') as f:
        for line_no, line in enumerate(f):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start()+1
                location = (line_no, column_no)
                index.setdefault(word, []).append(location)
    for key in index:
        print("{}:{}".format(key, index[key]))

def normal():
    with open(os.path.join('data', 'zen.txt'), 'r') as f:
        for line_no, line in enumerate(f):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start()+1
                location = (line_no, column_no)
                tmp = index.get(word, [])
                index[word] = tmp
                tmp.append(location)
    for key in index:
        print("{}:{}".format(key, index[key]))

if __name__ == '__main__':
    _defaultdict()
