class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        list_size=len(points)

        total_time = 0
        for i in range(list_size-1):
            xdistance = abs(points[i+1][0]-points[i][0])
            ydistance = abs(points[i+1][1]-points[i][1])
            max_distance = max(xdistance,ydistance)
            total_time+=max_distance
        return (total_time)