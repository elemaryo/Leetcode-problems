# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        # Go down to the end and return each node and swap it, it takes the whole branch
        # Time Complexity: O(n) - visit each node
        # Space Complexity: O(d) - Call stack is equal to the height of the tree
        
        # Base case: reach the last node
        if root is None:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
#         tempNode = TreeNode(None)
#         tempNode = root.left
#         root.left = root.right
#         root.right = tempNode 
        
#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)
        
        return root