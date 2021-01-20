class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        newString = list(s)

        while i < j:
            if newString[i].isalpha() and newString[j].isalpha():
                newString[i], newString[j] = newString[j], newString[i]
                i += 1
                j -= 1

            elif not newString[i].isalpha():
                i += 1

            # elif not newString[j].isalpha():
            #     j-=1
            else:
                j -= 1

        return "".join(newString)

# Time Complexity - O(n) look through every character
# Space Complexity - O(n) creating a list version of the string
