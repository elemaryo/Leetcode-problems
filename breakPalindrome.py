class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
         # only need to look at the first half since its a palindrome
         # 'a' forms the most lexiclogically smallest palindrome
        for i in range(len(palindrome)//2):
            # replace the first character that isn't a to break palindrome in most optimal way
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
        # corner case - all 'a' i.e aaa replace last element with b
        return palindrome[:i-1] + "b" if len(palindrome) > 1 else ""
