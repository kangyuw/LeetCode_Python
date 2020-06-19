#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        for i in range(1, days[-1] + 1):
            if i not in costs: dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + costs[0],
                            dp[max(i-7,0)] + costs[1],
                            dp[max(i-30,0)] + costs[2])
            print(dp)
        return dp[-1]
        
# @lc code=end

