class Solution:
    # When you have a matrix problem where you are comparing values against adjacent values
    # it is a graph problem.
    # BFS: level by level
    # DFS: going deep into the graph
    def numIslands(self, grid):
        if not grid:
            return 0

        # increase count if we find an island
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        # Check if we are at the ends, or if we are not at a 1
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        # setting current value to # to mark it as visited
        grid[i][j] = '#'
        # visit its neighbours to look for 1s
        self.dfs(grid, i+1, j)  # down
        self.dfs(grid, i-1, j)  # up
        self.dfs(grid, i, j+1)  # right
        self.dfs(grid, i, j-1)  # left

    # Time Complexity: O(M*N) - Iterate through every element in the matrix for rows and columns
    # Space Complexity: O(M*N) - Recursion call stack space for rows and columns
    # Videos: https://www.youtube.com/watch?v=NTNMN_UwQRA&list=WL&index=23&ab_channel=BrennanFradelis-DataStructuresandAlgorithms
    #         https://www.youtube.com/watch?v=U6-X_QOwPcs&ab_channel=NickWhite
    #           https: // www.youtube.com/watch?v = o8S2bO3pmO4 & ab_channel = KevinNaughtonJr.
