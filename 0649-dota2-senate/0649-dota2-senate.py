class Solution(object):
    def predictPartyVictory(self, senate):
        queue_r=[]
        queue_d=[]

        for index, s in enumerate(senate):
            if s=="R": queue_r.append(index)
            if s=="D": queue_d.append(index)
            index+=1

        while (queue_r and queue_d):
            voter_r=queue_r.pop(0)
            voter_d=queue_d.pop(0)

            queue_r.append(voter_r+len(senate)) if voter_r < voter_d else queue_d.append(voter_d+len(senate))

        return "Radiant" if queue_r else "Dire"