class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_num = len(nums)
        if len_num == 0:
            return 0
        if len_num == 1:
            return 1
        sum = 0
        for i in range(1,len_num):
            if nums[i-1] != nums[i]:
                sum += 1
                nums[sum] = nums[i]
        return sum + 1
