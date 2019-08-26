#!/bin/python3
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count=0
    ar.sort()
    highest=ar[len(ar)-1]
    for i in range(0,len(ar)):
        if ar[i] == highest:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
