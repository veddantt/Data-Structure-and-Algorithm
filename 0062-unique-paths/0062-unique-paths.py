class Solution(object):
    def uniquePaths(self, m, n):
        dp = [1] * n

        for _ in range(1, m):
            for col in range(1, n):
                dp[col] += dp[col - 1]

        return dp[-1]