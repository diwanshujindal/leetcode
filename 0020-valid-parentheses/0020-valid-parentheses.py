class Solution(object):
    def isValid(self, s):
        d={'}':'{',']':'[',')':'('}
        temp=[]
        for i in s:
            if i in d:
                if temp and temp[-1]==d[i]:
                    temp.pop()
                else:
                    return False
            else:
                temp.append(i)
        return len(temp)==0