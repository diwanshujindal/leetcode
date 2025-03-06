class Solution(object):
    def thirdMax(self, nums):
        if(len(set(nums))<3):
            return max(nums)
        x = max(nums)
        nums.remove(max(nums))
        while(max(nums) == x):
            nums.remove(max(nums))
        y = max(nums)
        nums.remove(max(nums))
        while(max(nums)==y):
            nums.remove(max(nums))
        return max(nums)
        