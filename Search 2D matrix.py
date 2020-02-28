class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """ 
        j = 0
        i = len(matrix) - 1
        while i >=0 and j < len(matrix[0]):
            print (i,j)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                j+=1
            else:
                i-=1
        return Falses