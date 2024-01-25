class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row=len(matrix)+1
        col=len(matrix[0])+1
        self.mat=[]
        for i in range(row):
            self.mat.append([0]*col)
        for i in range(1,row):
            for j in range(1,col):
                pre_sum=self.mat[i-1][j]+self.mat[i][j-1]+matrix[i-1][j-1]-self.mat[i-1][j-1]
                self.mat[i][j]=pre_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_=self.mat[row2+1][col2+1]-self.mat[row1][col2+1]-self.mat[row2+1][col1]+self.mat[row1][col1]
        return sum_
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)