# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
  
        # Use two pointers, one at head and the other two steps and if it passes it then its a cycle
    
        # Time Complexity: O(n) - Loop through the entire linked list
        # Space Complexity: O(1) - No extra space is needed
    
        # If its a single node or no node, there is no cycle
        if head is None or head.next is None:
            return False

        previous = head
        current = head.next
        
        # Since your options are either cycle or not, loop over the cycle option
        
        while previous != current:
            # if there is no cycle 1 -> 2 - > NULL
            if current is None or current.next is None:
                return False
            
            # Accelerate current two steps ahead and they will meet up
            current = current.next.next
            previous = previous.next
        
        return True
        