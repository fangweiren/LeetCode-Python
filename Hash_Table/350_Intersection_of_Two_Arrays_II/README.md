### 题意
Given two arrays, write a function to compute their intersection.  
给定两个数组，写一个方法来计算它们的交集。

Example:
```
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
```
Note:
- Each element in the result should appear as many times as it shows in both arrays.
- 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
- The result can be in any order.
- 我们可以不考虑输出结果的顺序。

Follow up:

- What if the given array is already sorted? How would you optimize your algorithm?
- 如果给定的数组已经排好序呢？你将如何优化你的算法？
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
- 如果 nums2 的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？

### 思路一
遍历 nums1 中的每个元素，并在 nums2 中查找该元素是否出现，若出现且结果列表 res 中没有，则加入 res 中，同时删除 nums2 中的该元素。
```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)
                nums2.remove(num)
        return res
```
### 思路二
用字典 result 存储 nums1 中 num 到 出现次数的映射，然后遍历 nums2，若出现在字典 result 中则将其加入到结果列表 res 中，同时将该数的次数减一。
```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        result = {}
        for num in nums1:
            if num not in result:
                result[num] = 1
            else:
                result[num] += 1
        for num in nums2:
            if num in result and result[num] > 0:
                res.append(num)
                result[num] -= 1
        return res
```
### 思路三
先将两个数组排序，再维持两个指针分别遍历两个数组，寻找共同的元素。
```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res
```
[LeetCode 350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/description/)
