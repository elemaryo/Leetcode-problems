import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
for i in range(h):
    row = input()
    result = ""
    for j in t:
        if ord(j) >= 97:
            index = (ord(j) - 97) * l
            result += row[index:index + l]
        elif ord(j) >= 65:
            index = (ord(j) - 65) * l
            result += row[index:index + l]
        else:
            index = (ord(j) - 65 + 27) * l
            result += row[index:index + l]
            
    
    print(result)