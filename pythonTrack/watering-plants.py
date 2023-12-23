class Solution(object):
    def wateringPlants(self, plants, capacity):
        sum = 0
        cap =capacity
        for i in range(len(plants)):
            sum+=1
            if plants[i]>cap:
                sum+=2*(i)
                cap=capacity
            cap-=plants[i]

        return sum