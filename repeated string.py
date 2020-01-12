#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
    # number of a's that originally exist * number of times it repeats + remainder (because he knows if there is a remainder one it doesnt matter) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
