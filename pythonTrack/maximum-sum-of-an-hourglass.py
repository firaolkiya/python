class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        col=1
        row=1
        total=0
        while col<len(grid[0])-1:
            row=1
            while row<len(grid)-1:
                curent_sum=grid[row-1][col-1]+grid[row-1][col]+grid[row-1][col+1]
                curent_sum+=grid[row][col]
                curent_sum+=grid[row+1][col-1]+grid[row+1][col]+grid[row+1][col+1]
                total=max(curent_sum,total)
                row+=1
            col+=1
        return total
            