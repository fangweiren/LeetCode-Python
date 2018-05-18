class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        for word in words:
            for row in rows:
                if set(word.lower()) <= row:
                    res.append(word)
        return res
