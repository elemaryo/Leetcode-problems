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
        
    # Search the left subtree and the right subtree till you find p and q then return the root node
        
    # Base cases        
        # Scenario where If the tree reached the end of a branch/ no root, return False
        if not root:
            return False
        
        # Scenario where If your root is equal to your p or q node value, will always be the            lowest common ancestor
        if root.val == p.val or root.val == q.val:
            return root
        
        # Left Recursion
        
        left = self.lowestCommonAncestor(root.left, p, q)
        
        # Right Recursion
        
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Scenario where If one side is null and the other is not
        
        if not left:
            return right
        
        if not right:
            return left
        
        # If the recursion scales back up and returns both p and q, it returns that root as         LCA
        
        return root
        
    # Time Complexity O(n)
    # Space Complexity O(h) where h = tree height
    
    # Links:
        # https://www.youtube.com/watch?v=13m9ZCB8gjw
        # https://www.youtube.com/watch?v=py3R23aAPCA
            
        