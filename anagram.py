import math
import os
import random
import re
import sys


def anagram(s, t):
    Soccurances = {}
    Toccurances = {}

    for i in range(len(s)):
        if s[i] in Soccurances:
            Soccurances[s[i]] += 1
        else:
            Soccurances[s[i]] = 1

    for i in range(len(t)):
        if t[i] in Toccurances:
            Toccurances[t[i]] += 1
        else:
            Toccurances[t[i]] = 1

    isAnagram = True
    for letter in Soccurances:  # O(n)
        # O(1)
        if letter not in Toccurances or Soccurances[letter] != Toccurances[letter]:
            isAnagram = False
            break
        if not isAnagram:
            print("false")
            continue
    for letter in Toccurances:  # O(n)
        # O(1)
        if letter not in Soccurances or Toccurances[letter] != Soccurances[letter]:
            isAnagram = False
            break
    if isAnagram:
        print("true")
    else:
        print("false")


anagram("anagram", "nagaram")
