# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
            
    def isValidBST(self, root: TreeNode) -> bool:
        
        # Traverse recursively left and right sub tree
        # if one fails, return false
        
        # Time Complexity: O(n) - you run on every node
        # Space Complexity: O(h) - call stack will be at the height of the tree
        # Video:
            # https://www.youtube.com/watch?v=U2PV7-jca2o
        
        
        # Initialize min and max as infinities as starter
        return self.helper(root,float('-inf'), float('inf') )
        
        
    def helper(self, root: TreeNode, minimum: int, maximum: int) -> bool:
            
        # Base case for Null nodes
    
        if root is None:
            return True
        
        # Base case for checking left and right node key values with the minimum/maximum value before
        
        if root.val <= minimum or root.val >= maximum:
            return False
        
         # Preorder traversal - left side then right side
        left = self.helper(root.left, minimum, root.val)
        right = self.helper(root.right, root.val, maximum)
        
        
        return left and right
    
    
    #OLD thinking
    
#             if (root.left is None) or ((root.val > root.left.val) and (root.left.val < minimum.val)):
#             minimum = root
#             left = self.isValidBST(root.left)
        
#         else:
#             return False
            
#         if (root.right is None) or ((root.val < root.right.val) and (root.right.val > maximum.val)):
#             maximum = root
#             right = self.isValidBST(root.right)
              
#         else:
#             return False
        
#         return (left and right)
        
    

        
                