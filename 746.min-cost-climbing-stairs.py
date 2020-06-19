#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1: return cost[0]
        pre1 = cost[0]
        pre2 = cost[1]
        for i in range(2, len(cost)):
            current = cost[i] + min(pre1, pre2)
            pre1 = pre2
            pre2 = current
        return min(pre1, pre2)
        
# @lc code=end

