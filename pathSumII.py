# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, pathsum: int) -> List[List[int]]:
        self.path = []  # log stack
        self.result = []

        def dfs(root, path, pathsum):
            if not root:
                return
            self.path.append(root.val)
            if not root.left and not root.right:  # leaf node
                if sum(self.path) == pathsum:
                    self.result.append([a for a in self.path])

            else:
                dfs(root.left, self.path, pathsum)
                dfs(root.right, self.path, pathsum)

            self.path.pop()

        dfs(root, path, pathsum)

        return self.result
