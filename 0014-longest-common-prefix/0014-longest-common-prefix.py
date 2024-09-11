class Solution(object):
    def longestCommonPrefix(self, strs):
        s0=strs[0]
        d=''
        for i in range(1,len(strs)):
            s1=strs[i]
            flag=True
            for j in range(len(s0)):
                if flag==True and j<len(s1) and s0[j]==s1[j]:
                    d+=s0[j]
                else:
                    flag=False
            s0=d
            d=''
        return s0
        