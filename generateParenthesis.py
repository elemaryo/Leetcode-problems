class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.path = []  # call stack

        if n == 0:
            return self.result

        self.leftn = n
        self.rightn = n

        def dfs(result, path, n, leftn, rightn):
            # invalid base case
            if leftn < 0 or rightn < 0:
                return
            # valid base case
            if leftn == 0 and rightn == 0:
                result.append("".join(path))
                return

            path.append("(")
            # call left paranthesis
            dfs(result, path, n, leftn-1, rightn)
            path.pop()

            # call right paranthesis
            # leftn = 2, rightn = 3 -> yes
            if rightn > leftn:
                path.append(")")
                dfs(result, path, n, leftn, rightn-1)
                path.pop()

        dfs(self.result, self.path, n, self.leftn, self.rightn)
        return self.result

 # Time Complexity: O(2^n) - where n is the number of input in that case parenthesis
 # Space Complexity: O(n * 2) - O(n) for call stack of brackets
 # Videos: https://www.youtube.com/watch?v=sz1qaKt0KGQ

 # combination time : o(total * n * 2 +1)
