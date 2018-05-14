class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict1 = {}
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        for patt, word in zip(pattern, words):
            if patt not in dict1:
                if word in dict1.values():
                    return False
                dict1[patt] = word
            else:
                if dict1[patt] == word:
                    pass
                else:
                    return False
        return True
