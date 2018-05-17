### 题意
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).  
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).  
找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

Example:
```
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
```

### 思路
对于每个点，创建一个哈希映射并计算具有相同距离的所有点。 如果对于点 i，则有距离为 d 的 k 个点，与其相对应的回飞镖的数量是 `k *（k-1）`。继续添加这些来获得最终结果。

```python
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0     
        for i in points:
            d = {}
            for j in points:
                dist = (i[0]-j[0])**2 + (i[1]-j[1])**2
                print dist
                d[dist] = d.get(dist, 0) + 1
                
            for n in d:
                res += d[n] * (d[n]-1)
                print '-'*10
                print res
        return res
```
[LeetCode 447. Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/description/)
