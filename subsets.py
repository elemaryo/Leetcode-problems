class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        # self.subset = []

        if len(nums) == 0:
            return self.results

        def generateSubset(index, results, subset, nums):
            if index >= len(nums):
                results.append([a for a in subset])
                return

            # general case
            subset.append(nums[index])  # path stack append

            # call left child
            generateSubset(index+1, results, subset, nums)

            # combination tree requires pop here
            subset.pop()

            # call right child
            generateSubset(index+1, results, subset, nums)

            # for i in range(index, len(nums)):
            #     subset.append(nums[i])
            #     self.generateSubset(index+1, results, subset, nums)
            #     subset.pop()

        generateSubset(0, self.results, [], nums)
        return self.results


# Time Complexity: O(2^n) - n is number of digits
# Space Complexity: O(h) - h is height of tree
# Videos: https://www.youtube.com/watch?v=LdtQAYdYLcE&ab_channel=KevinNaughtonJr.
# https://www.youtube.com/watch?v=LiuEfq37hqc&ab_channel=SuboptimalEngineer
# https://www.youtube.com/watch?v=XovjRfHumDU&ab_channel=NideeshTerapalli
