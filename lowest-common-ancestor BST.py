# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        
        #BST: every node on the left is smaller on the node on the right for the root
        
        # Base case:
    
        if not root:
            return False
        
        # Scenario where if root is greater than both nodes - max returns the largest element
        
        elif root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
  
        # Scenario where if root is less than both nodes - min returns lowest element
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)        
        
        # Scenario where if the root node value is the same/equal as p or q 
        # or p and q are in split/seperate trees
        
        else:
            return root
  
    # Time Complexity O(h) where h = tree height
    # Links:
        # https://www.youtube.com/watch?v=TIoCCStdiFo
        
        