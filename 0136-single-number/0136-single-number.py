class Solution(object):
    def singleNumber(self, nums):
        n = len(nums)
        c = 0
        for i in range(n):
            c = c ^ nums[i]
        return c