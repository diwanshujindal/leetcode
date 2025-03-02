class Solution(object):
    def topKFrequent(self, nums, k):
        #get the dictionary for the frequency of each num
        frequency={}
        for i in nums:
            frequency[i]=frequency.get(i,0)+1 #if the frequency exist then get that else 0 then add 1 
        l=[]
        result=[]
        for i in range(len(nums)+1):
            l.append([])
        for num,count in frequency.items():
            l[count].append(num)
        for i in range(len(l)-1,-1,-1):
            for j in l[i]:
                result.append(j)
                if len(result)==k:
                    return result
        return result
        