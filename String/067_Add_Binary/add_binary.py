class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '':
            return b
        if b == '':
            return a
        if a[-1] == '1' and b[-1] == '1':
            self.addBinary(self.addBinary(a[-1], b[-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            self.addBinary(a[-1], b[-1]) + '0'
        else:
            self.addBinary(a[-1], b[-1]) + '1'
