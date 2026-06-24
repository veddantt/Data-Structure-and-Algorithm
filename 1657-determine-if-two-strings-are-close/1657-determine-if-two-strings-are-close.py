class Solution(object):
    def closeStrings(self, word1, word2):

        uw1=list(set(word1))
        uw2=list(set(word2))
        if sorted(uw1)!=sorted(uw2):
            return False
        else:
            c1=[]
            c2=[]
            for i in uw1:
                x=word1.count(i)
                c1.append(x)
            for i in uw2:
                x=word2.count(i)
                c2.append(x)
            if sorted(c1)==sorted(c2):
                return True
            else:
                return False
        