class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sum= 0
        count=0
        for i in range(len(costs)):
            if sum + costs[i]<=coins:
                sum+=costs[i]
                count+=1
            else:
                break
        return count