class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        list1 = [str(i) for i in nums]
        c=0
        for i in nums:
            if i==0:
                c+=1
        if c==len(nums):
            return "0"
        for i in range(len(list1)):
            index=i
            for j in range(i,len(list1)):
                temp_i = int(list1[index]+list1[j])
                temp_j = int(list1[j]+list1[index])
                if temp_i<temp_j:
                    index=j
            list1[index],list1[i]=list1[i],list1[index]
        return "".join(list1)

        