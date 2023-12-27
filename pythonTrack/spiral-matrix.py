class Solution(object):
    def spiralOrder(self, matrix):
        xstart=0
        ystart=0
        yend = len(matrix)
        xend=len(matrix[0])
        count=0;
        total=yend*xend
        list1 = []
        while(count<total):
            for i in range(xstart,xend):
                count+=1
                if(matrix[ystart][i]!=200):
                    list1.append(matrix[ystart][i])
                    matrix[ystart][i]=200
            ystart+=1
            for i in range(ystart,yend):
                count+=1
                if matrix[i][xend-1]!=200:
                    list1.append(matrix[i][xend-1])
                    matrix[i][xend-1]=200
            xend-=1
            for i in range(xend-1,xstart-1,-1):
                count+=1
                if matrix[yend-1][i]!=200:
                    list1.append(matrix[yend-1][i])
                    matrix[yend-1][i]=200
            yend-=1
            for i in range(yend-1,ystart-1,-1):
                count+=1
                if matrix[i][xstart]!=200:
                    list1.append(matrix[i][xstart])
                    matrix[i][xstart]
            xstart+=1
        return list1



