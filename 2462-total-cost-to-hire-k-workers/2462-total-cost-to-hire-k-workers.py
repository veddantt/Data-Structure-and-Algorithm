class Solution(object):
    def totalCost(self, costs, k, candidates):
        import heapq
        q = []
        i = candidates-1
        j = len(costs)-candidates
        if i<j:
            for k1 in range(i+1):
                q.append((costs[k1], k1))
            for k2 in range(j, len(costs)):
                q.append((costs[k2], k2))
            heapq.heapify(q)
        else:
            q = [(c, i) for i,c in enumerate(costs)]
            heapq.heapify(q)
        
        out = 0
        for t in range(k):
            o = heapq.heappop(q)
            out+=o[0]
            if j-i>1:
               if o[1]<=i:
                 i+=1
                 heapq.heappush(q, (costs[i], i))
               else:
                 j-=1
                 heapq.heappush(q, (costs[j], j))
        return out