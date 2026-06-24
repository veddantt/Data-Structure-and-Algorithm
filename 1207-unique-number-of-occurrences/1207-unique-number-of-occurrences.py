class Solution(object):
    def uniqueOccurrences(self, nums):
          a=Counter(nums)
          b=set()
          for element in a.values():
            if element in b:
             return False
            else:
              b.add(element)
          return True
        