import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
asci = ""
for i in message:
    asci += "0"*(7-len(bin(ord(i))[2:]))+bin(ord(i))[2:]
answer = ""
currentBitType = asci[0]
currentBlock = ""

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for i in asci:
    if i == currentBitType:
        currentBlock = currentBlock + "0"
        
    else:
        if currentBitType == "1":
            answer = answer + "0 " + currentBlock + " "
            
        else:
            answer = answer + "00 " + currentBlock + " "
            
            
        currentBitType = i
        currentBlock = "0"

if currentBitType == "1":
    answer = answer + "0 " + currentBlock
    
else:
    answer = answer + "00 " + currentBlock
        
print(answer)