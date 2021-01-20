# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.path = []  # log stack
        self.result = []
        self.num = 0

        def dfs(root, path):
            if not root:
                return
            self.path.append(root.val)
            # add string or do the current*10+root.val
            # path call stack base case to leaf node
            if not root.left and not root.right:
                for i in range(len(self.path)):
                    self.num = self.num * 10 + self.path[i]

                self.result.append(self.num)

            else:
                dfs(root.left, self.path)
                dfs(root.right, self.path)

            self.path.pop()
            self.num = 0

        dfs(root, self.path)
        return sum(self.result)
