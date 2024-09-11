class Solution(object):
    def searchInsert(self, nums, target):
        a=0
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums=sorted(nums)
            return nums.index(target)