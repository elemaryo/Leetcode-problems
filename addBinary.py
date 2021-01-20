class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def decimalToBinary(number):
            result = ""
            if number == 0:
                result = str(0) + result
            while number != 0:
                remainder = number % 2  # gives the exact remainder
                number = number // 2  # reduce the number
                result = str(remainder) + result

            return result

        def binaryToDecimal(num):
            numD = 0
            i = 0
            while len(num) > 0:
                # gets right digit
                numD += (2**i) * (int(num) % 10)
                i += 1
                num = num[:len(num)-1]

            return numD

        ans = binaryToDecimal(a) + binaryToDecimal(b)
        return decimalToBinary(ans)
