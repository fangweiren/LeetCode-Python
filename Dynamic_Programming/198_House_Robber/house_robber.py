class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        else:
            nums[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
            return nums[-1]
																																		            
