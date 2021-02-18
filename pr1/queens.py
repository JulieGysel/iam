#!/usr/bin/python3

import sys
import copy
import numpy as np

num = int(sys.argv[1])
arr = np.array([[num*j+i+1 for i in range(num)] for j in range(num)])
out = []

arr_tr = np.transpose(arr)
for (row1, row2) in zip(arr, arr_tr):
    out.append([*row1, 0])
    out.append([*row2, 0])

    for col in range(num):
        for i in range(col+1, num):
            out.append([-row1[col], -row1[i], 0])
            out.append([-row2[col], -row2[i], 0])


arr_fl = np.fliplr(arr)
for offset in range(-num+2, num-1):
    out1 = np.diagonal(arr, offset)
    out2 = np.diagonal(arr_fl, offset)

    for i in range(len(out1)):
        for j in range(i+1, len(out1)):
            out.append([-out1[i], -out1[j], 0])
            out.append([-out2[i], -out2[j], 0])

print('c N-Queens Problem for N =', num)
print('p cnf', num*num, len(out))
for i in out:
    print(*i)
