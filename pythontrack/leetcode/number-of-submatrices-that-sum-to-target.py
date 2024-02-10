class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
       column=len(matrix[0])+1
       row=len(matrix)+1
##declare 2d to matrix that wil contain prefix sum
       prefix=[]
       for i in range(row):
           temp=[0]*column
           prefix.append(temp)
       total=0
       for i in range(1,row):
           for j in range(1,column):
               current_sum=prefix[i][j-1]+prefix[i-1][j]+matrix[i-1][j-1]-prefix[i-1][j-1]
               prefix[i][j]=current_sum
               for r in range(i-1,-1,-1):
                   for c in range(j-1,-1,-1):
                       temp_sum=current_sum-(prefix[r][j]+prefix[i][c])+prefix[r][c]
                       if temp_sum==target:
                           total+=1
       return total
        