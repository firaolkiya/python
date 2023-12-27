class Solution(object):
    def freqAlphabets(self, s):
        ##my algorhithm i is that starting from 1 index and check if next char is #.
# if # add equivalent char of s[i-1:i+1] else add index i-1

        string_len = len(s)
        output = ""
        current_index = 1
        while current_index<string_len:
            if current_index==string_len-1 or s[current_index+1]!="#":
                equivalent_int = int(s[current_index-1])
                output+=chr(96+equivalent_int)
                current_index+=1
            else:
                equivalent_int = int(s[current_index-1:current_index+1])
                output+=chr(96+equivalent_int)
                current_index+=3
        if not s[string_len-1]=="#":
            equivalent_int = int(s[string_len-1])
            output+=chr(equivalent_int+96)
        return (output)

            


        