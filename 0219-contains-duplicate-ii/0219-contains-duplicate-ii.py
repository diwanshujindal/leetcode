class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d={}
        n=len(nums)
        for i in range(n):
            if nums[i] in d:
                if abs(d[nums[i]]-i)<=k:
                    return True
            
            d[nums[i]]=i
        return False
        
        