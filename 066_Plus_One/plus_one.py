class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 1
        for i in range(len(digits)-1 ,-1, -1):
            if digits[i] + num == 10:
                digits[i] = 0
                num = 1
            else:
                digits[i] = digits[i] + num
                num = 0
				break
        if num == 1:
            digits.insert(0,1)
        return digits
