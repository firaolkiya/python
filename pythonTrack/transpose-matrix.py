class Solution(object):
    def transpose(self, matrix):
        mat = []
        for i in range(len(matrix[0])):
            lis=[]
            for j in range(len(matrix)):
                lis.append(matrix[j][i])
            mat.append(lis)
        return mat
