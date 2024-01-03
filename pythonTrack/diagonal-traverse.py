class Solution(object):
    def findDiagonalOrder(self, mat):
        list1 = []
        xstart=0
        ystart = 0
        xend=0
        yend=0
        count=0
        while count<len(mat)*len(mat[0]):
            i=xstart
            j=yend
            while(i<=xend and j<=yend):
                list1.append(mat[j][i])
                i+=1
                j-=1
                count+=1
            if xend<len(mat[0])-1:
                xend+=1
            else:
                ystart+=1
            if yend<len(mat)-1:
                yend+=1
            else:
                xstart+=1
            i=xend
            j=ystart
            
            while i>=xstart and j<=yend:
                list1.append(mat[j][i])
                i-=1
                j+=1
                count+=1
            if yend<len(mat)-1:
                yend+=1
            else:
                xstart+=1
            if xend<len(mat[0])-1:
                xend+=1
            else:
                ystart+=1
        return list1







        