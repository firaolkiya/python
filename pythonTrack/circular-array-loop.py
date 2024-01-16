class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            rotated= 0
            index=i
            while rotated<3:
                if (nums[i]<0 and nums[index]>0) or (nums[i]>0 and nums[index]<0):
                    break
                index+=nums[index]
                if index==i and abs(nums[i])%len(nums)!=0:
                    print(i)
                    return True
                elif index>=len(nums):
                    rotated+=1
                    index=index%len(nums)
                elif index<0:
                    temp=abs(index)
                    if temp<=len(nums):
                        index+=len(nums)
                    else:
                        temp%=len(nums)
                        index=len(nums)-temp
                    rotated+=1
                if index==i and abs(nums[i])%len(nums)!=0:
                    print(index)
                    return True
                   
                
        return False
                

        