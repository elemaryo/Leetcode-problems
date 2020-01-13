class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        ans = ""
        
        for key, val in roman.items():
            while(num - key >= 0):
                ans += val
                num = num - key
            
        return ans




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
        
    