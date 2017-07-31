class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for i in range(0,len(numbers)):
            sub = target - numbers[i]
            if sub in result.keys():
                return [result[sub]+1,i+1]
            else:
                result[numbers[i]] = i
