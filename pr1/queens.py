#!/usr/bin/python3

import sys
import numpy as np


def checkcol(arr, pos, num):
    while pos > 0:
        if arr[pos] in queens:
            return False
        else:
            pos -= num
    return True


def checkDia1(arr, pos, num):
    while pos > 0:
        if arr[pos] in queens:
            return False
        else:
            pos -= (num-1)
    return True


def checkDia2(arr, pos, num):
    while pos > 0:
        if arr[pos] in queens:
            return False
        else:
            pos -= (num+1)
    return True


def place(arr, row, num):
    for i in range(row*num, row*num+num):
        pos = row*num+i
        if pos == 0:
            continue
        if checkcol(arr, pos, num) and checkDia1(arr, pos, num) and checkDia2(arr, pos, num):
            queens.append(pos)
            return


# main
num = int(sys.argv[1])

print('p cnf', num*num, num)
arr = np.array(list(range(1, num*num+1)))
queens = []

place(arr, 0, num)
place(arr, 1, num)


print(queens)

# for i in range(num):
#     print(*arr[i*num:i*num + num], 0)
