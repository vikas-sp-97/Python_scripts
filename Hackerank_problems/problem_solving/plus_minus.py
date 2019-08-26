#!/bin/python3
#https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_pos=0
    count_neg=0
    count_zero=0
    for i in range(len(arr)):
        if(arr[i]>0):
            count_pos+=1
        elif arr[i]<0:
            count_neg+=1
        else:
            count_zero+=1

    print(count_pos/len(arr))
    print(count_neg/len(arr))
    print(count_zero/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
