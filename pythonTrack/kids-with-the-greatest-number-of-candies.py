class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ma = max(candies)
        boolean = []
        for i in candies:
            boolean.append((i+extraCandies>=ma))
        return boolean
        