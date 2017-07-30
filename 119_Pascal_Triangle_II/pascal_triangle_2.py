class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1,rowIndex + 1):
            res = [1] + [res[x] + res[x-1] for x in range(1, i)] + [1]
        return res
