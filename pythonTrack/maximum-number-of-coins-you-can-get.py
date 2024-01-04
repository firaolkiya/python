class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left=0
        right=len(piles)-1
        count=0
        while(right>left+1):
            count+=piles[right-1]
            right-=2
            left+=1
        return count

        
        