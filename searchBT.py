# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def search(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        else:
            left = self.searchBST(root.left, val)
            right = self.searchBST(root.right, val)

        return root.val == val or left or right


# Time Complexity: O(N) - visit each node
# Space Complexity: O(h) - height of the tree
