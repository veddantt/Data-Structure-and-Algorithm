class Solution(object):
    def mergeAlternately(self, word1, word2):
        r = ''
        i = 0
        while i < min(len(word1),len(word2)):
            r += word1[i] + word2[i] 
            i +=1
        if len(word1)>len(word2):
            r += word1[i:]
        elif len(word2)>len(word1):
            r += word2[i:]
        
        return r