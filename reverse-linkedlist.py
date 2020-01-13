# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursive:
            # Time complexity - O(n) - Interate over each element in linked list
            # Space complexity - O(n) - Recursive call stack           
        # Base case or if there is one node or just a NULL
            # head.next = False = 1 -> NULL, one item 
            # not head = NULL no reverse
#         if not head or head.next = False:
#             return head
        
#         newhead = self.reverseList(head.next)
#         head.next.next = head # the current head tells the next head to point towards it
#                                 # apparently after null, next.next points back to the node                                      before
#         head.next = None        # so the linkedlist is not cyclical
        
#         return newhead

        
        # iterative - use two pointers and increment 
            # Time complexity - O(n) - Interate over each element in linked list
            # Space complexity - O(1)
        
        previous = None
        current = head
        temp = None
        
        
        while current != None:
            temp = current.next # save next node
            current.next = previous # reverse pointer
            previous = current # advance previous
            current = temp     # advance current

            
        return previous # Automatically going to become new head at the end
        # x -> 1 -> 2 -> 3 -> 4 x
        # x <- 1 -> 2 -> 3 -> 4 x
        # x 1 -> 2 -> 3 -> 4 x
        # x 1 <- 2 -> 3 -> 4 x
        
        # Videos:
            # https://www.youtube.com/watch?v=O0By4Zq0OFc
            # https://www.youtube.com/watch?v=MRe3UsRadKw
            
            