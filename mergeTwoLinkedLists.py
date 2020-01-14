# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Time Complexity - O(m+n) - traversing both linked lists lengths
        # Space Complexity - O(1) - no extra space used
        # Video:
            # https://www.youtube.com/watch?v=GfRQvf7MB3k
        
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        current = ListNode(None)
        head = current
        
        while (l1 is not None) and (l2 is not None): # short circuits if one is empty
            if (l1.val <= l2.val):
                current.next = l1
                l1 = l1.next
                current = current.next
                # l1.next = self.mergeTwoLists(l1.next, l2)
                # return l1

            elif (l1.val >= l2.val):
                current.next = l2
                l2 = l2.next
                current = current.next
                #l2.next = self.mergeTwoLists(l1, l2.next)
                # return l2
            
            
        # if you reach the end of one of the linked list since they arent the same size
        if (l1 is None):
            current.next = l2
        
        elif (l2 is None):
            current.next = l1
            
        return head.next
        
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         resultArr = []
#         arr1 = self.to_list(l1)
#         arr2 = self.to_list(l2)
        
#         resultArr = sorted(arr1 + arr2)
        
#         return self.to_link(resultArr)
        
        
#     def to_link(self, array: list) -> ListNode:
#         head = ListNode(None)
#         current = head
        
#         for e in array:
#             current.next = ListNode(e)
#             current = current.next
        
#         return head.next
    
#     def to_list(self, l: ListNode) -> list:
#         array = []
#         current = l
        
#         while current != None:
#             array.append(current.val)
#             current = current.next
        
#         return array
        