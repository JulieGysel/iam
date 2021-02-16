#!/usr/bin/python3

import sys
import copy
import numpy as np


def rows(array, num):
    array2 = np.transpose(array)
    for (row1, row2) in zip(array, array2):
        print(*row2, 0)
        print(*row1, 0)

        for col in range(num):
            for i in range(col+1, num):
                print(-row1[col], -row1[i], 0)
                print(-row2[col], -row2[i], 0)


def diagonals(array, num):
    array2 = np.fliplr(array)

    for offset in range(-num+1, num-1):
        out1 = np.diagonal(array, offset)
        out2 = np.diagonal(array2, offset)
        for i in range(len(out1)):
            for j in range(i+1, len(out1)):
                print(-out1[i], -out1[j], 0)
                print(-out2[i], -out2[j], 0)


# program
num = int(sys.argv[1])
arr = np.array([[num*j+i+1 for i in range(num)] for j in range(num)])

print('p cnf', num*num, 1)
rows(arr, num)
diagonals(arr, num)
