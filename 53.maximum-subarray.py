#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max = -float('inf')
        for i in nums:
            sum += i
            if sum > max: max = sum
            if sum < 0: sum = 0
        return max
# @lc code=end

