#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        pre1 = 1
        pre2 = 2
        res = 0
        for i in range(n-2):
            res = pre1 + pre2
            pre1 = pre2
            pre2 = res
        return res
        
# @lc code=end

