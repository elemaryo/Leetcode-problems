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

    # Time complexity: o(n) We traverse the list containing nn elements only once. Each look up in the table costs only O(1)O(1) time.
    # Space complexity: o(n) The extra space required depends on the number of items stored in the hash table, which stores at most nn elements.
