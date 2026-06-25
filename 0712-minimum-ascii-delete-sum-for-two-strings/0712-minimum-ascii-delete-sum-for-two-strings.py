class Solution(object):
    def lcs(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = ord(s1[i-1]) + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

    def minimumDeleteSum(self, s1, s2):
        tot = 0
        for ch in s1:
            tot += ord(ch)
        for ch in s2:
            tot += ord(ch)

        return tot - 2 * self.lcs(s1, s2)