# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        # base case that assumes the diameter = 1 and does not pass through root
        self.ans = 1

        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            # update the diameter between either the original or the addition of the left
            # and right subtree plus the node
            self.ans = max(self.ans, L+R+1)
            # take the largest sub tree and add 1
            return max(L, R) + 1

        depth(root)
         # n nodes = n-1 paths
        return self.ans - 1

    # Video: https://www.youtube.com/watch?v=ey7DYc9OANo
    
    # Time Complexity - O(N) we visit every node once
    # Space Complexity - O(N) the size of our callstack depends on the depth of the search
        
    # diameter of binary tree is the longest height of the left subtree + the longest height of the right subtree
    # plus 1 for the root node of that tree