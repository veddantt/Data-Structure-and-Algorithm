class Solution(object):
    def countBits(self, n):
     nexto = 2
     t = 0
     c = [0]*(n+1)

     for i in range(1, n+1):
        if i == nexto:
            nexto *= 2
            t = 0
        c[i] = c[t] + 1
        t += 1
     return c