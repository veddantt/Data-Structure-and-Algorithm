class Solution(object):
    def rob(self, nums):
        
        p1,p2 = 0,0
        for num in nums:
            t = p1
            p1 = max(num + p2,p1)
            p2 = t
        return p1