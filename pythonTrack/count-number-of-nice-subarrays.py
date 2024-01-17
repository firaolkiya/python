class Solution(object):
    def numberOfSubarrays(self, nums, k):
        left=1
        right=0
        total_count=0
        list1 = [i for i in range(len(nums))if nums[i]%2!=0]
        list1=[-1]+list1
        list1.append(len(nums))
        odd_counter=0
        while right<len(nums):
            if odd_counter<k and nums[right]%2!=0:
                odd_counter+=1
                if odd_counter==k:
                    even_left=list1[left]-list1[left-1]
                    even_right=list1[left+k]-right
                    print(even_left,even_right)
                    right=list1[left+k-1]
                    left+=1
                    total_count+=(even_left*even_right)
                    odd_counter-=1
            right+=1
        return total_count


                
            
        return total_count    

                


