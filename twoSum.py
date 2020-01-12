class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}
        
        for index in range(len(nums)):
            currentValue = nums[index]
            neededValue = target - currentValue
            
            if neededValue in dictionary:
                return [dictionary[neededValue], index]
            
            else:
                dictionary[currentValue] = index
        