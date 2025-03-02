class Solution(object):
    def calPoints(self, operations):
        record=[]
        n=len(operations)
        for i in operations:
            if i== 'C':
                record.pop()
            elif i=='+':
                record.append(record[-1]+record[-2])
            elif i=='D':
                record.append(2*record[-1])
            else:
                record.append(int(i))
        count=0
        for i in record:
            count+= i
        return count

        