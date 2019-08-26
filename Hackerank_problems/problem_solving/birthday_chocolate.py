#!/bin/python3
#https://www.hackerrank.com/challenges/the-birthday-bar/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count=0
    sum_1 =[]
    for i in range(0,len(s)):
        if i + m <= len(s):
            sum_1.append(s[i:i+m])
    for i in range(0,len(sum_1)):
        # print(sum(sum_1[i]),d)
        if sum(sum_1[i]) == d:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
