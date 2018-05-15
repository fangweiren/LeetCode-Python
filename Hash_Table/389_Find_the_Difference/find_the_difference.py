class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        diff = {}
        for c in s:
            diff[c] = diff[c] + 1 if c in diff else 1
        for c in t:
            if c not in diff:
                return c
            diff[c] -= 1
            if diff[c] < 0:
                return c
