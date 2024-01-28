class Solution(object):
    def countPairs(self, nums, k):
        map = defaultdict(list)
        for i in range(len(nums)):
            map[nums[i]].append(i)
        sum = 0
        for i in map.values():
            for j in range(len(i)):
                for b in range(j+1,len(i)):
                    if i[j]*i[b]%k==0:
                        sum+=1
        return sum


            
        