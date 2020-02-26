import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
a = []
for i in range(n):
    pi = int(input())
    a.append(pi)
    
a.sort()
d = abs(a[0] - a[1])

for i in range(len(a)-2):
    if abs(a[i+1] - a[i+2]) < d:
        d = abs(a[i+1] - a[i+2])
        

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(d)