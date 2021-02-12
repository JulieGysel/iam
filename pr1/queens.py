#!/usr/bin/python3

import sys
import numpy as np

QUEEN = 1
BANNED = -1

num = int(sys.argv[1])
print('p cnf', num*num, num)
array = [[0 for i in range(num)] for i in range(num)]


def ban(arr, row, col):
    arr[row] = [BANNED for i in range(num)]
    col1 = col
    col2 = col

    for i in range(row, num):
        arr[i][col] = BANNED

    for i in range(row, num):
        if col1 < 0:
            break
        arr[i][col1] = BANNED
        col1 -= 1

    while row < num and col2 < num:
        arr[row][col2] = BANNED
        row += 1
        col2 += 1

    return arr


def place(arr, row):
    if row >= num:
        return True
    for i in range(len(arr[row])):
        if arr[row][i] == 0:
            arr = ban(arr, row, i)
            arr[row][i] = QUEEN
            return
            # return place(arr, row+1)

    print('problem', row)
    return False


place(array, 0)
place(array, 1)
place(array, 2)
place(array, 3)

end_list = list(range(1, num+1))
print(end_list)
for i in array:
    print(*i, 0)
