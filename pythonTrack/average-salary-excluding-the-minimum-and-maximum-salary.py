class Solution(object):
    def average(self, salary):
       salary.sort()
       sum=0.0
       for i in range(1,len(salary)-1):
           sum+=salary[i]
       sum/=(len(salary)-2)
       return sum
        