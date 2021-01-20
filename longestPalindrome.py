class Solution:
    def longestPalindrome(self, s: str) -> int:
        # longest palindrome involves even numbers of letters and one
        # unique character i.e racecar
        characterCount = {}
        result = 0
        # get character counts in string
        for i in range(len(s)):
            if s[i] in characterCount:
                characterCount[s[i]] += 1

            else:
                characterCount[s[i]] = 1

        for i in characterCount:
            # add character count that is even
            # note if you have 'aaa' it will do 3/2 = 1 and add 2 a's
            result += characterCount[i] // 2 * 2
            # add special character only if we are even
            if result % 2 == 0 and characterCount[i] % 2 == 1:
                result += 1

        return result

# Time Complexity: O(N), loop through each letter
# Space Complexity: O(N), store count
# Videos: https://www.youtube.com/watch?v=a_3XDW9P47E&ab_channel=NickWhite
