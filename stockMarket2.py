import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

maxProfit = 0
delta = 0
n = int(input())
for i in input().split():
    v = int(i)
    
    if v > maxProfit:
      maxProfit = v
    
    if (v < maxProfit) and (maxProfit - v > delta):
      delta = maxProfit - v

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

answer = -(delta)   

print(answer)