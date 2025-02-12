class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        ans=nums
        for i in range(n):
            ans.append(nums[i])
        return ans