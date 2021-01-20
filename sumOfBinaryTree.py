# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfTree(self, root: TreeNode):
        if not root:
            # answer for empty tree
            return 0

        else:
            # general case
            left = self.sumOfTree(root.left)
            right = self.sumOfTree(root.right)
            # handle for root and left and right
            result = root.val + left + right

        return result

    # Time Complexity O(n)
    # Space Complexity O(h) where h = tree height
