class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        result = 1
        pairs.sort(key = lambda x: x[1])
        x = pairs[0][1]
        for i in range(1, len(pairs)):
            if pairs[i][0] > x:
                result += 1
                x = pairs[i][1]
        return result