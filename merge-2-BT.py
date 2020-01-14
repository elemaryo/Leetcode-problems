# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # Similar to the swapping of tree nodes, always traverse left and right seperately
        # Time Complexity: O(m) - traverse the height of both trees fully at m nodes
        # Space Complexity: O(m) - call stack will be same as number of elements
        # Video:
            # https://www.youtube.com/watch?v=p3vVYNngyxs
        
        # Base case: if one of the nodes in one of the tree is empty, return the other one
        
        if t1 is None:
            return t2
        
        if t2 is None:
            return t1
        
        # Sum up the values of the node from one tree to the other and return as one tree
        t1.val = t1.val + t2.val
        
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1
        