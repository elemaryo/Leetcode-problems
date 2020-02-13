# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        list.sort(nums)
        x = 1
        
        for i in range(len(nums)):
            if nums[i] < 0:
                continue
            # if we find a smaller number no need to continue, cause the array is sorted
            if x < nums[i]:
                return x
            
            x = nums[i] + 1
            
        return x
        

# def solution(A):
#     # write your code in Python 3.6
#     maximumNumber = 0
    
#     for i in range(len(A)):
#         maximumNumber = max(maximumNumber,A[i])
      
    
#     # if minimumNumber < 0:
#     if maximumNumber < 0:
#         return 1
    
#     elif (maximumNumber - 1) in A:
#         return int(maximumNumber + 1)
        
#     else: 
#         return int(maximumNumber - 1)