#!/usr/bin/python3

import sys
import copy
import numpy as np

QUEEN = 1
BANNED = -1

num = int(sys.argv[1])
print('p cnf', num*num, num)
array = [[0 for i in range(num)] for i in range(num)]
array[0][0] = BANNED


def print_arr(arr):
    for j in arr:
        print(*j)


def ban(arr, row, col):
    col1 = col
    col2 = col

    for i in range(num):
        arr[row][i] = BANNED
    for i in range(row, num):
        arr[i][col] = BANNED
        if col1 >= 0:
            arr[i][col1] = BANNED
            col1 -= 1
        if col2 < num:
            arr[i][col2] = BANNED
            col2 += 1
    return arr


def place(arr, row):
    if row >= num:
        return True

    save = copy.deepcopy(arr)

    for col in range(num):
        if arr[row][col] == 0:

            ban(arr, row, col)
            arr[row][col] = QUEEN
            # print(row, col)
            # print_arr(arr)

            if place(arr, row+1) != save:
                return arr
            else:
                # print(row, 'rollback')
                arr = copy.deepcopy(save)
                # print()
                # print_arr(arr)

    return save


place(array, 0)

# print_arr(array)
for i in range(num):
    for j in range(num):
        if array[i][j] != BANNED:
            print(i, j)

# print(end_list)
# for i in array:
#     print('\t'.join(map(str, i)), '\t', 0)
