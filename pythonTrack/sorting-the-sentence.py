class Solution(object):
    def sortSentence(self, s):
        list1 = list(s.split(" "))
        list2 = [""]*len(list1)
        for i in list1:
            num = i[len(i)-1]
            k = i[:len(i)-1]
            num = int(num)
            list2[num-1]=k
        return " ".join(list2)
        

        