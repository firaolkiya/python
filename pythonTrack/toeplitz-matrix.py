class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if not matrix[i][j]==matrix[i-1][j-1]:
                    return False


        return True
                