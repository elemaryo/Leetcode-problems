class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}  # O(n = 7)

        ans = 0

        # loop through each letter before last letter
        for i in range(len(s)-1):  # O(n-1)
            if roman[s[i]] >= roman[s[i+1]]:
                ans += roman[s[i]]
            else:
                ans -= roman[s[i]]

        # add last letter
        ans += roman[s[len(s)-1]]  # O(1)

        return ans
