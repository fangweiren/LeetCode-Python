### 题意
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.  
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

Grid cells are connected horizontally/vertically (not diagonally).  
网格中的格子水平和垂直方向相连（对角线方向不相连）。

The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).  
整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).  
岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。

One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.  
格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

Example:
```
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
解释: 它的周长是下面图片中的 16 个黄色的边：
![](https://leetcode-cn.com/static/images/problemset/island.png)
```

### 思路
如果是陆地，则周长 +4 ；如果上面也是陆地，说明重复计数了，周长 -2 ；如果左边也是陆地，同样周长 -2 。
```python
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        length = len(grid[0]) if height else 0
        side = 0
        for h in range(height):
            for l in range(length):
                if grid[h][l] == 1:
                    side += 4
                    
                    if h>0 and grid[h-1][l]:
                        side -= 2
                    if l>0 and grid[h][l-1]:
                        side -= 2
        return side
```
[LeetCode 463. Island Perimeter](https://leetcode.com/problems/island-perimeter/description/)
