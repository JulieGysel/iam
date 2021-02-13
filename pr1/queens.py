#!/usr/bin/python3

import sys
import copy
import numpy as np


def printf(format, *args):
    sys.stdout.write(format % args)


QUEEN = 1
BANNED = -1

num = int(sys.argv[1])
print('p cnf', num*num, num)
array = [[0 for i in range(num)] for i in range(num)]
# array[0][0] = BANNED


def print_arr(arr):
    for i in range(num):
        for j in range(num):
            printf(' %s%d\033[0m', '\x1B[34m ' if arr[i]
                   [j] >= 0 else '', arr[i][j])
        printf('\n')


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

            if row == num-1:
                print_arr(arr)
                # return True

            if place(arr, row+1) == True:
                return True
            else:
                # print(row)
                arr = copy.deepcopy(save)
                # print_arr(arr)
                # arr[row][col] = BANNED
    return False


print(place(array, 0))
