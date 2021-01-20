# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # check if its a null tree
        if not root:
            return True

        def isSymmetric(left: TreeNode, right: TreeNode):
            if (not left and not right):
                return True
            if (not left or not right):
                return False

            # if (left.val != right.val):
            #     return False

            else:
                # check left child to the right child in value and if the left subtree right child is the same as right subtree left child and if the left left is the same as the right subtree right child
                return left.val == right.val and isSymmetric(left.right, right.left) and isSymmetric(left.left, right.right)

        # since you have root, check left and right
        return isSymmetric(root.left, root.right)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Videos: https://www.youtube.com/watch?v=K7LyJTWr2yA
