class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstr = [x for x in s.lower() if x.isalnum()]
        return newstr == newstr[::-1]
