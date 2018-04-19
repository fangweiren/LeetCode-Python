class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        convert = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        len_s = len(s)
        for i in range(len_s - 1):
            current = convert[s[i]]
            next = convert[s[i+1]]
            if current >= next:
                sum += current
            else:
                sum -= current
        return sum + convert[s[-1]]
