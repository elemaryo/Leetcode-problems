class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        if len(digits) == 0:
            return result

        def dfs(path, digits, result):
            if len(digits) == 0:
                result.append("".join(path))
                return

            else:
                for i in range(len(phone[digits[0]])):
                    path.append(phone[digits[0]][i])
                    dfs(path, digits[1:], result)
                    path.pop()

        dfs([], digits, result)
        return result

# Time Complexity: O(3^N * 4^M) where N is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and M is the number of digits in the input that maps to 4 letters (e.g. 7, 9), and N+M is the total number digits in the input.
# Space Complexity: O(3^N * 4^M)
# Videos: https://www.youtube.com/watch?v=a-sMgZ7HGW0&ab_channel=BackToBackSWE
