class Solution(object):
    def diagonalSum(self, mat):
        sum=0
        for i in range(len(mat)):
            sum+=mat[i][i]
        co = 0
        for i in range(len(mat)-1,-1,-1):
            if co == i:
                co+=1
                continue
            sum+=mat[co][i]
            co+=1
        return sum
            
        