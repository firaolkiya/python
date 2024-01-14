class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        first=0
        second=0
        output = []
        while first<len(firstList) and second<len(secondList):
            if firstList[first][0]>=secondList[second][0]:
                if firstList[first][0]>secondList[second][1]:
                    second+=1
                elif firstList[first][1]<=secondList[second][1]:
                    output.append([firstList[first][0],firstList[first][1]])
                    first+=1
                else:
                    output.append([firstList[first][0],secondList[second][1]])
                    second+=1
            else:
                if secondList[second][0]>firstList[first][1]:
                    first+=1
                elif secondList[second][1]<=firstList[first][1]:
                    output.append([secondList[second][0],secondList[second][1]])
                    second+=1
                else:
                    output.append([secondList[second][0],firstList[first][1]])
                    first+=1
        return output








       