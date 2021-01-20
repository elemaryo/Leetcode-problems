# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def cloneTreeDFS(self, root: TreeNode):
        if not root:
            return None

        else:
            copy = TreeNode(root.val)
            copy.left = cloneTreeDFS(root.left)
            copy.right = cloneTreeDFS(root.right)

        return copy

    # Time Complexity O(n)
    # Space Complexity O(h) where h = tree height
