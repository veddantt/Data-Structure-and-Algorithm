class Solution(object):
    def maxProfit(self, prices, fee):
        not_hold = 0
        hold = -prices[0]
        for p in prices[1:]:
            hold = max(hold, not_hold-p)
            not_hold = max(p+hold-fee, not_hold)
        return not_hold
        