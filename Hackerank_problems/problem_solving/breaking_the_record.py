#!/bin/python3
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    count_high=0
    count_low=0
    high=scores[0]
    low=scores[0]
    for i in range(0,len(scores)):
        if scores[i]!=high and scores[i]!=low:
            if scores[i]>high:
                count_high+=1
                high = scores[i]
            elif scores[i]<low:
                count_low+=1
                low=scores[i]
    return count_high,count_low

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
