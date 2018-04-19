class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
            if dict[num] > len(nums) / 2:
                return num


#方法二：先对数组进行排序，因为多数元素一定存在，且个数超过总个数的一半，那么排序后最中间的那个元素一定是多数元素。
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]
