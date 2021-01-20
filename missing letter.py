import math
import os
import random
import re
import sys

def missing(s,t):
    ans = ""

    for letter in s: #O(n)
            if letter not in t: #O(1)
                ans += letter

    for letter in ans: #O(n)
            print(letter)

missing("abcde", "abce")