class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        for i in t:
            dict2[i] = dict2.get(i, 0) + 1
        return dict1 == dict2
