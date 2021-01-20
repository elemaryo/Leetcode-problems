class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.path = []
        self.result = []

        def dfs(candidates, target, path, result, index):
            # invalid case
            if target < 0:
                return
            # base case
            if target == 0:
                result.append([a for a in path])
                return
            # invalid case
            if index >= len(candidates):
                return

            else:
                # general case
                path.append(candidates[index])

                # call left child -- accept nums[i]
                dfs(candidates, target-candidates[index], path, result, index)

                path.pop()

                # call right child -- reject nums[i]
                dfs(candidates, target, path, result, index+1)

        dfs(candidates, target, self.path, self.result, 0)
        return self.result

# Time Complexity: O(2^n) - n is the number of candidates
# Space Complexity: O(h) - height of the tree
