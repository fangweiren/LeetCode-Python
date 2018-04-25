class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top1 = top2 = top3 = float('-inf')
        for num in nums:
            if num not in (top1, top2, top3):
                if num > top1:
                    top1, num = num, top1
                if num > top2:
                    top2, num = num, top2
                if num > top3:
                    top3, num = num, top3
        print top1, top2, top3
        if top3 == float('-inf'):
            return top1
        return top3
