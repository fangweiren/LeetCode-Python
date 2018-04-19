class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        letters = {}
        for i in magazine:
            letters[i] = letters[i] + 1 if i in letters else 1
        for i in ransomNote:
            if i not in letters:
                return False
            letters[i] -= 1
            if letters[i] < 0:
                return False
        return True
