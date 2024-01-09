class Solution(object):
    def findAnagrams(self, s, p):
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        list1 = [] 
        if len(p)>len(s):
            return []
        for i in range(len(p)):
            dict1[p[i]]+=1
        for i in range(len(p)):
            dict2[s[i]]+=1
        ch = True
        for i in dict1:
            if not i in dict2 or dict1[i]!=dict2[i]:
                ch=False
        if ch:
            list1.append(0)
        for i in range(len(p),len(s)):
            dict2[s[i]]+=1
            dict2[s[i-len(p)]]-=1
            if dict2[s[i-len(p)]]<=0:
                dict2.pop(s[i-len(p)])
            ch = True
            for k in dict1:
                if not k in dict2 or dict1[k]!=dict2[k]:
                    ch=False
            if ch:
                list1.append(i-len(p)+1)
        return list1
        
            