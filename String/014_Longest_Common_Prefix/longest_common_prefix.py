class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
		if strs == []:
			return ''
		for i in range(1, len(strs)):
			l1 = len(strs[0])
			l2 = len(strs[i])
			if l1 <= l2:
				l = l1
			else:
				l = l2
			if l == 0:
				return ''
			strs[0] = strs[0][0:l]
			for j in range(l):
				if strs[0][j] != strs[i][j]:
					strs[0] = strs[0][0:j]
					break
		return strs[0]
