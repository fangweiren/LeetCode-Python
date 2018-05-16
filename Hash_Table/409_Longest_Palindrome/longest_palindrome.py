class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        res = 0
        for c in s:
            d[c] = d[c] + 1 if c in d else 1
        for times in d.values():
            if times % 2 == 0:
               res += times
            else:
                res += times - 1
        return res+1 if res < len(s) else res
