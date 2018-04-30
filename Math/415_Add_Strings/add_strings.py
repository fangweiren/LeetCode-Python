class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        digits1 = list(num1)
        digits2 = list(num2)
        
        sum1 = 0
        sum2 = 0
        for i in digits1:
            sum1 *= 10
            sum1 += int(i)
            
        for i in digits2:
            sum2 *= 10
            sum2 += int(i)

        return str(sum1 + sum2) 
