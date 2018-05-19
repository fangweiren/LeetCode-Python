### 题意
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).  
二进制手表顶部有 4 个 LED 代表小时 (0-11)，底部的 6 个 LED 代表分钟 (0-59)。

Each LED represents a zero or one, with the least significant bit on the right.  
每个 LED 代表一个 0 或 1，最低位在右侧。

![401. Binary Watch](https://github.com/fangweiren/LeetCode-Python/blob/master/screenshots/Binary_clock_samui_moon.jpg)

For example, the above binary watch reads "3:25".  
例如，上面的二进制手表读取 “3:25”。

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.  
给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

Example:
```
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
```
Note:
- The order of output does not matter.
- 输出的顺序没有要求。
- The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
- 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
- The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
- 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。

### 思路
枚举小时 h 和分钟 m，然后判断二进制 1 的个数是否等于 num。

```python
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    res.append('%d:%02d' % (h, m))
        return res


# *****************************************************************************
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # hh_summary, mm_summary = self.get_summary()
        hh_summary = {
            0: [0],
            1: [1, 2, 4, 8],
            2: [3, 5, 6, 9, 10],
            3: [7, 11],
        }
        mm_summary = {
            0: [0],
            1: [1, 2, 4, 8, 16, 32],
            2: [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48],
            3: [7, 11, 13, 14, 19, 21, 22, 25, 26, 28, 35, 37, 38, 41, 42, 44,
                49, 50, 52, 56],
            4: [15, 23, 27, 29, 30, 39, 43, 45, 46, 51, 53, 54, 57, 58],
            5: [31, 47, 55, 59],
        }

        valid_time = []
        for hh in range(num + 1):
            mm = num - hh
            valid_hh = hh_summary.get(hh, [])
            valid_mm = mm_summary.get(mm, [])
            for h in valid_hh:
                for m in valid_mm:
                    valid_time.append('{0}:{1:02d}'.format(h, m))
        return valid_time

    # def get_summary(self):
    #     hh_summary = self._get_summary(11)
    #     mm_summary = self._get_summary(59)
    #     return hh_summary, mm_summary

    # def _get_summary(self, num):
    #     summary = {}
    #     for n in range(num + 1):
    #         bit = self.get_bit(n)
    #         summary[bit] = summary.get(bit, []) + [n]
    #     return summary

    # def get_bit(self, n):
    #     bit = 0
    #     while n > 0:
    #         bit += n & 1
    #         n >>= 1
    #     return bit
```
[LeetCode 401. Binary Watch](https://leetcode.com/problems/binary-watch/description/)
