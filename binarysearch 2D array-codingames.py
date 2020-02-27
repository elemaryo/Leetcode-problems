import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

top = 0;
bot = h - 1; # because if H = 10, then array is 0..9
left = 0;
right = w - 1; # because if W = 10, then array is 0..9

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if bomb_dir == "U":
        bot = y0 - 1
    
    if bomb_dir == "UR":
        bot = y0 - 1
        left = x0 + 1
        
    if bomb_dir == "R":
        left = x0 + 1
    
    if bomb_dir == "DR":
        left = x0 + 1
        top = y0 + 1
        
        
    if bomb_dir == "D":
        top = y0 + 1
    
    if bomb_dir == "DL":
        top = y0 + 1
        right = x0 - 1

    if bomb_dir == "L":
        right = x0 - 1
            
    if bomb_dir == "UL":
        bot = y0 - 1
        right = x0 - 1
                
    x0 = (right + left)/2 
    y0 = (top + bot)/2

    # the location of the next window Batman should jump to.
    print(str(int(x0)) + " " + str(int(y0)))

    #Videos:
    #https://www.youtube.com/watch?v=4R9PyTvcWE0
    #https://www.youtube.com/watch?v=LzUKpADnmNM

    # O(n) = Log (N*M)