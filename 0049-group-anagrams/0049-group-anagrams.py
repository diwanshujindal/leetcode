class Solution(object):
    def groupAnagrams(self, strs):
        d=defaultdict(list)
        for s in strs:
            a=[0]*26
            for c in s:
                a[ord(c)-ord('a')]+=1
            d[tuple(a)].append(s)
        return d.values()
        
        