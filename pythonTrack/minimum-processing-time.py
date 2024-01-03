class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        totalTime=0
        count=0
        for i in range(len(tasks)):
            if i==0:
                totalTime=tasks[i]+processorTime[count//4]
            else:
                totalTime=max(totalTime,tasks[i]+processorTime[count//4])
            count+=1
        return  totalTime