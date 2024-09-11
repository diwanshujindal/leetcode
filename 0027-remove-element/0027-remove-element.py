class Solution(object):
    def removeElement(self, nums, val):
        new = [i for i in nums if i != val]
        nums[:] = new
        return len(nums)
       
       