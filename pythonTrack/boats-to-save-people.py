class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        count=0
        left=0
        right=len(people)-1
        while left<=right:
            if people[left]+people[right]<=limit:
                count+=1
                left+=1
                right-=1
            else:
                count+=1
                right-=1
        return count

        