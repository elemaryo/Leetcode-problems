# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maximumSum(self, root: TreeNode) -> int:
        # base case
        if not root:
            # answer for empty tree
            return 0

        else:
            left = maximumSum(root.left)
            right = maximumSum(root.right)
            result = root.val + max(left, right)

        return result

# Time Complexity: O(N) - visit each node
# Space Complexity: O(h) - height of the tree
