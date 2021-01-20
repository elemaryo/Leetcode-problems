class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        newString = s.lower()

        i = 0
        j = len(s) - 1

        while i <= j:
            if not newString[i].isalnum():
                i += 1
                continue

            if not newString[j].isalnum():
                j -= 1
                continue

            if newString[i] != newString[j]:
                return False

            else:
                i += 1
                j -= 1

        return True
