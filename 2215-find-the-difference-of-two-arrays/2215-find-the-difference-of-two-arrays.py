class Solution(object):
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        nums1Def = [n for n in set1 if n not in set2]
        nums2Def = [n for n in set2 if n not in set1]

        return [nums1Def, nums2Def]