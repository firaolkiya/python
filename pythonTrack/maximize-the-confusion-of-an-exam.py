class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        nums = [0 if i=="F" else 1 for i in answerKey]
        right=0
        left=0
        fliped = 0
        total_one=0
        while right<len(nums):
            if nums[right]==1:
                total_one = max(right+1-left,total_one)
                right+=1
            elif fliped<k:
                fliped+=1
                total_one = max(right+1-left,total_one)
                right+=1
            else:
                while fliped>=k:
                    if nums[left]==0:
                        fliped-=1
                    left+=1
        total = total_one
        nums = [1 if i=="F" else 0 for i in answerKey]
        right=0
        left=0
        fliped = 0
        total_one=0
        while right<len(nums):
            if nums[right]==1:
                total_one = max(right+1-left,total_one)
                right+=1
            elif fliped<k:
                fliped+=1
                total_one = max(right+1-left,total_one)
                right+=1
            else:
                while fliped>=k:
                    if nums[left]==0:
                        fliped-=1
                    left+=1
        print(total,total_one)
        total = max(total_one,total)
        return total

            

          

        