class Solution(object):
    def isValid(self, s):
        a=[]
        b='{(['
        for i in s:
            if i in b:
                a.append(i)
            else:
                if  (not a) or (i==']' and a[-1]!='[')   or (i==')' and a[-1]!='(') or  (i=='}' and a[-1]!='{'):
                    return False
                else:
                    a.pop()
        return not a 