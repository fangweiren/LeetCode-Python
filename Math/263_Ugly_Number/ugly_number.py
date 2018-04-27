class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while True:
            if num <= 0:
                return False
            if num == 1:
                return True
            elif num % 2 == 0:
                num /= 2
            elif num % 5 == 0:
                num /= 5
            elif num % 3 == 0:
                num /= 3
            else:
                return False
