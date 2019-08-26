#!/bin/python3
#https://www.hackerrank.com/challenges/apple-and-orange/problem

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    for i in range(0, len(apples)):
        apples[i] += a
    for i in range(0, len(oranges)):
        oranges[i] += b
    count_a = 0
    count_o = 0
    for i in range(0, len(apples)):
        if apples[i] in range(s, t + 1):
            count_a += 1
    print(count_a)
    for i in range(0, len(oranges)):
        if oranges[i] in range(s, t + 1):
            count_o += 1
    print(count_o)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
