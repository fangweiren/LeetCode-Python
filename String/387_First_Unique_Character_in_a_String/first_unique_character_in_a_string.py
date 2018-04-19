class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for i in s:
            if i in letters.keys():
                letters[i] = letters[i] + 1
            else:
                letters[i] = 1
        for ind in range(len(s)):
            if letters[s[ind]] == 1:
                return ind
        return -1
