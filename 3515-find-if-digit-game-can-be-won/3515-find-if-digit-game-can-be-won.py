class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a=0
        for i in nums:
            if i>=10:
                a+=i
            else:
                a-=i
        if a==0:
            return False
        else:
            return True