class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        if len(nums) <= 1:
            return result

        for c in range(len(nums)):
            if c > 0 and nums[c] == nums[c-1]:
                continue
                # remove duplicates at c
            newTarget = 0 - nums[c]
            # a pair of numbers in arr[k+1:] that add up to newTarget
            a = c + 1
            b = len(nums) - 1
            while a < b:
                if nums[a] + nums[b] > newTarget:
                    b -= 1
                elif nums[a] + nums[b] < newTarget:
                    a += 1
                else:
                    result.append([nums[c], nums[a], nums[b]])
                    a += 1
                    while nums[a] == nums[a-1] and a < b:
                        a += 1
                        # remove duplicates at a

#         for c in range(len(nums)):
#             newTarget = 0 - nums[c]
#             # a pair of numbers in arr[k+1:] that add up to newTarget
#             a = c + 1
#             b = len(nums) - 1
#             while a < b:
#                 if nums[a] + nums[b] == newTarget:
#                     result.append([nums[a],nums[b],nums[c]])
#                     a+=1
#                     b-=1

#                 elif nums[a] + nums[b] > newTarget:
#                     b-=1

#                 else:
#                     a+=1

        return result

# Time Complexity: O(n^2) - looping through array twice
# Videos: https://www.youtube.com/watch?v=6qgC-dqKElA&ab_channel=thecodingworld
