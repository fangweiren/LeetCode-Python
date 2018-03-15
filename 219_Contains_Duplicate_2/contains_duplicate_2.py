class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d1 = {}
        for i, v in enumerate(nums):
            if v in d1 and i - d1[v] <= k:
                return True
            d1[v] = i
        return False
