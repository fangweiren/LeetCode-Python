class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for num in nums:
            if val != num:
                nums[index] = num
                index += 1
        return index
