# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            # no depth
            return 0

        else:
            left = maxDepth(root.left)
            right = maxDepth(root.right)

            # handle returns max of each tree + root node
            result = max(left, right) + 1

        return result

# Time Complexity O(n) - visit each node in the tree
# Space Complexity O(h) where h = tree height
