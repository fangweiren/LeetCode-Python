class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = {}
        res = []
        for num in nums1:
            if num not in result:
                result[num] = 1
        for num in nums2:
            if num in result:
                res.append(num)
                result.pop(num)
        return res
