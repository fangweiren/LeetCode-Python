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
