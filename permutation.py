class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def dfs(nums, arr, i, result):
            if len(arr) == len(nums):
                result.append([a for a in arr])
                return

            for k in range(0, len(arr) + 1):
                # k = loop for index, # i = index
                # push number into set
                nextLevelArr = arr[0:k] + [nums[i]] + arr[k:]
                dfs(nums, nextLevelArr, i + 1, result)

        dfs(nums, [nums[0]], 1, self.result)
        return self.result


# Time Complexity: O(n!)
# Space Complexity: O(n) no extra space but result array
# Videos: https://www.youtube.com/watch?v=KukNnoN-SoY&ab_channel=TimeComplexityInfinity
# https://www.youtube.com/watch?v=foBqt8E94mI&ab_channel=AnishMallaAnishMalla
