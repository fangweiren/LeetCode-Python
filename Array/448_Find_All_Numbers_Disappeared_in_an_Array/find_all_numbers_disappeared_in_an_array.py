class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        return [ind + 1 for ind, val in enumerate(nums) if val > 0]
