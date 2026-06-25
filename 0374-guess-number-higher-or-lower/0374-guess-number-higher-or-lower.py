class Solution(object):
    def guessNumber(self, n):
        left=0
        right=n
        while left<=right:
            mid=(left+right)//2
            g=guess(mid)
            if g==0:return mid
            elif g==1:left=mid+1
            elif g==-1:right=mid-1
        return -1