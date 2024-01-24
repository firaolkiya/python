class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left=0
        right=len(nums)-1
        mid=0
        while mid<=right:
            if nums[mid]==0:
                nums[mid],nums[left]=nums[left],nums[mid]
                left+=1     
            elif nums[mid]==2:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
            else:
                mid+=1
            if left>mid:
                mid+=1
            

        