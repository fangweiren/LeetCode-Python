class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        count = 1
        while x / count > 10:
            count *= 10
        while x:
            left = x / count
            right = x % 10
            if left != right:
                return False
            x = (x % count) / 10
            count /= 100
        return True
