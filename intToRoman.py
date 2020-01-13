class Solution:
    #basically keep subtracting the number with values above 0 and add the key
    def intToRoman(self, num: int) -> str:
        roman = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        ans = ""
        
        for key, val in roman.items():
            while(num - key >= 0):
                ans += val
                num = num - key
            
        return ans

# ret = ""
        
#         while num >= 1000:
#             ret +=  'M'
#             num -= 1000
            
#         if num >= 900:
#             ret+= 'CM'
#             num-= 900
        
#         if num >= 500:
#             ret+= 'D'
#             num -= 500
            
#         if num >= 400:
#             ret+= 'CD'
#             num-= 400
        
#         while (num >= 100):
#             ret+= 'C'
#             num -= 100
        
#         if num >= 90:
#             ret+= 'XC'
#             num-= 90
            
#         if num >= 50:
#             ret+= 'L'
#             num-= 50
            
#         if num >= 40:
#             ret+= 'XL'
#             num-= 40
        
#         while (num >= 10):
#             ret+= 'X'
#             num -= 10
            
#         if num >= 9:
#             ret+= 'IX'
#             num -= 9
        
#         if num >= 5:
#             ret+= 'V'
#             num -= 5
            
#         if num >= 4:
#             ret+= 'IV'
#             num-= 4
        
#         while num >= 1:
#             ret+= 'I'
#             num -=1
        
#         return ret

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         romanNumber = {
#             1: 'I',
#             5: 'V',
#             10: 'X',
#             50: 'L',
#             100: 'C',
#             500: 'D',
#             1000: 'M'
#         }
        
#         dividends = [1000, 100, 10, 1]      
        
#         output = ""
#         for dividend in dividends:
#             unit = int(num/dividend)
            
#             if unit < 1: continue
           
#             if unit in [4, 9]:
#                 n = (unit * dividend) + dividend
#                 output += romanNumber[dividend] + romanNumber[n]
#             elif unit < 4:
#                 output += romanNumber[dividend] * unit
#             elif unit >= 5:
#                 n = unit%5
#                 output += romanNumber[(5*dividend)] + romanNumber[dividend]*n



#             num -= dividend*unit
            
#         return output



# class Solution:
    
#     def getDigitNumber(self, num: int) -> int:        
#         count = 0
#         while num > 0:
#             num = int(num / 10)
#             count+=1
        
#         return count  
    
#     def getFirstDigit(self, num: int) -> int:
#         while num >= 10:  
#             num = int(num / 10)
            
#         return num
    
    
#     def intToRoman(self, num: int) -> str:
        
#         self.num = num
        
#         roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        
#         ans = ""
        
#         length = self.getDigitNumber(num)
        
#         i = 1
        
#         while num > 0:
            
#             integer = num
#             remainder = int(num % (10**(length-i)))
            
#             if integer > 10:
#                 integer = integer - remainder
                
#             key = list(roman.keys())
                    
#             while integer not in key:

#                 if self.getFirstDigit(integer) == 4:
#                     ans = ans + roman[(integer/4)] + roman[integer + (integer/4)]
#                     break

#                 elif self.getFirstDigit(integer) == 9:
#                     ans = ans + roman[(integer/9)] + roman[integer + (integer/9)]
#                     break

#                 elif integer - max(key) < 0:
#                     key.pop()

#                 else:
#                     integer = integer - max(key)
#                     ans = ans + roman[max(key)]

#             if integer in key:
#                 ans = ans + roman[integer]
            
#             num = num - (self.getFirstDigit(num)*10**(length-i))
#             i+=1
           
#         return ans
        
    
