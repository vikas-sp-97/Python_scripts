#!/bin/python3
#https://www.hackerrank.com/challenges/time-conversion/problem?h_r=next-challenge&h_v=zen

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[8:] == 'AM':
        if s[:2] == '12':
            s = '00' + s[2:8]
            return s
        else:
            return s[:8]
    elif s[8:] == 'PM':
        if s[:2] == '12':
            s = '00' + s[2:8]
            return s
        else:
            i = int(s[:2]) + 12
            s = str(i) + s[2:8]
            return (s)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
