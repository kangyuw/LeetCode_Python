#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def dfs(self, grid, y, x):
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] != '1':
            return

        grid[y][x] = '*'
        self.dfs(grid, y+1, x)
        self.dfs(grid, y-1, x)
        self.dfs(grid, y, x+1)
        self.dfs(grid, y, x-1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res
        
# @lc code=end

