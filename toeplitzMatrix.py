class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                # check the one thats ahead against behind so your index isnt behind
                if row > 0 and col > 0 and matrix[row][col] != matrix[row-1][col-1]:
                    return False

        return True

# Time Complexity - O(M * N) visit each row and column
# Space Complexity - O(1)
# Videos: https://www.youtube.com/watch?v=1jI0h9r-q0M
