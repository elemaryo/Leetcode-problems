import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
minimumTemp = float("inf") 
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    if abs(t) - 0 < abs(minimumTemp) or t == -minimumTemp and t > 0:
        minimumTemp = t
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

if n == 0:
    minimumTemp = 0

print(minimumTemp)