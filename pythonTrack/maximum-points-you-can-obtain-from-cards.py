class Solution(object):
    def maxScore(self, cardPoints, k):
        left_start=0
        left_end=k-1
        right_start=len(cardPoints)-k
        right_end=len(cardPoints)-1
        sum_left_window=sum(cardPoints[:left_end+1])
        sum_right_window=sum(cardPoints[right_start:])
        max_sum=0
        #iterate at most k elements will added to total sum
        count=0
        while count<k:
            if sum_left_window>sum_right_window:
                max_sum+=cardPoints[left_start]
                sum_left_window-=cardPoints[left_start]
                sum_right_window-=cardPoints[right_start]
                left_start+=1
                right_start+=1
            elif sum_right_window>sum_left_window:
                max_sum+=cardPoints[right_end]
                sum_left_window-=cardPoints[left_end]
                sum_right_window-=cardPoints[right_end]
                left_end-=1
                right_end-=1
            elif cardPoints[left_start]>cardPoints[right_end]:
                max_sum+=cardPoints[left_start]
                sum_left_window-=cardPoints[left_start]
                sum_right_window-=cardPoints[right_start]
                left_start+=1
                right_start+=1
            else:
                max_sum+=cardPoints[right_end]
                sum_left_window-=cardPoints[left_end]
                sum_right_window-=cardPoints[right_end]
                left_end-=1
                right_end-=1
            count+=1
        return max_sum

