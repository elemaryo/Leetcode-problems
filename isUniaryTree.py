# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # check if the left side is the null or if the left is true and the current value is true
        left = not root.left or root.val == root.left.val and self.isUnivalTree(
            root.left)
        # check if the right side is the null or if the right is true and the current value is true
        right = not root.right or root.val == root.right.val and self.isUnivalTree(
            root.right)
        return right and left

    # Time Complexity O(n)
    # Space Complexity O(h) where h = tree height

    # Links:
        # https://www.youtube.com/watch?v=BkUEFJZpZRw

# def univalued(root)->bool:
#     if not root:
#         return True
#     if root and not root.left and not root.right:
#         return True

#     l = univalued(root.left)#T
#     r = univalued(root.right)#T
#     flag = True
#     if root.left and not root.right:
#         flag = (flag and root.left.val == root.val)

#     if root.right and not root.left:
#         flag = (flag and root.right.val == root.val)

#     return l and r and flag
