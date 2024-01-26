class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
       map1={}
       total=sum(nums)
       prefix=0
       if total%p==0:
           return 0
       leng=len(nums)
       print(total)
       for i in range(len(nums)):
           prefix+=nums[i]
           right_mod=(total-prefix)%p
           if p-right_mod in map1:
               leng=min(leng,i-map1[p-right_mod])
           if right_mod%p==0:
               leng=min(leng,i+1)
           if prefix%p==0:
               map1[p]=i
           else:
                map1[prefix%p]=i
       print(map1)
       return leng if leng!=len(nums) else -1


           