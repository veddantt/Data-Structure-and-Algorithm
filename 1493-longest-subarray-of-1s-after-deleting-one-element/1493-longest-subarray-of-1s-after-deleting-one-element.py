class Solution:
    def longestSubarray(self, nums):
        left = {}
        right = {}
        cnt = 0
        ones = 0

        # Calculate left consecutive ones before each 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                ones += 1
            else:
                left[i] = cnt
                cnt = 0

        # Edge cases
        if ones == 0:
            return 0  # No 1s
        if ones == len(nums):
            return len(nums) - 1  # All 1s

        cnt = 0

        # Calculate right consecutive ones after each 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 1:
                cnt += 1
            else:
                right[i] = cnt
                cnt = 0

        # Calculate max combined length
        maxi = cnt
        for i in range(len(nums)):
            if nums[i] == 0:
                left_count = left.get(i, 0)
                right_count = right.get(i, 0)
                maxi = max(maxi, left_count + right_count)

        return maxi