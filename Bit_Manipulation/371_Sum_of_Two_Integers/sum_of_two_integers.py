class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max       ('0b1111111111111111111111111111111')
        MAX = 0x7FFFFFFF
        # 32 bits interger min     ('0b10000000000000000000000000000000')
        MIN = 0x80000000
        # mask to get last 32 bits ('0b11111111111111111111111111111111')
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            carry = a & b
            a = (a ^ b) & mask
            b = (carry << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
