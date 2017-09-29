# -*- coding: utf-8 -*-
# @author: Kinderlas (Kinderlas@gmail.com)
# @date: 2017/9/29 16:33

def main():
    board = [['_'] * 3] * 3
    print(board)
    board[1][2] = 'X'
    print(board)

    row = ['_'] * 3
    board = []
    for _ in range(3):
        board.append(row)
    print(board)
    board[1][2] = 'X'
    print(board)

    board = []
    for _ in range(3):
        row = ['_'] * 3
        board.append(row)
    print(board)
    board[1][2] = 'X'
    print(board)

    board = [['_'] * 3 for _ in range(3)]
    print(board)
    board[1][2] = 'X'
    print(board)

if __name__ == '__main__':
    main()