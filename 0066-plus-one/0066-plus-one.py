class Solution(object):
    def plusOne(self, digits):
        a=''
        result=[]
        for i in digits:
            a+=str(i)
        num=str(int(a)+1)
        for i in num:
            result.append(int(i))
        return result

        