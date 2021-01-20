class Solution:
    def calculate(self, s: str) -> int:
        # return int(eval(s))
        if len(s) == 0:
            return 0
        op = "+"
        current = 0
        stack = []
        # s.strip(" ")
        for i in range(len(s)):
            if s[i].isdigit():
                # 10 gets printed as 1 and then 0
                current = current * 10 + int(s[i])
            # once you reach the last digit, you dont complete the operation
            # check if you are on the last value
            if s[i].isdigit() != True and s[i] != " " or i == len(s)-1:
                if op == "*":
                    stack.append(int(stack.pop()*current))
                    # stack[-1]*=current
                elif op == "/":
                    # stack[-1]/=current
                    stack.append(int(stack.pop()/current))
                elif op == "+":
                    stack.append(current)
                elif op == "-":
                    stack.append(-current)

                current = 0
                op = s[i]

        return sum(stack)

# Time Complexity - O(N) we visit every number in the list
# Space Complexity - O(N) stack space needed for every number and operator

# Video: https://www.youtube.com/watch?v=2EErQ25kKE8&ab_channel=AnishMalla
#        https://www.youtube.com/watch?v=GR8Z1zaQzz0&ab_channel=AlgorithmsMadeEasy
