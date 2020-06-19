#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        if len(text1) <= len(text2):
            short, long = text1, text2
        else:
            short, long = text2, text1

        # res = ""
        res = 0
        i_short = 0
        i_long = 0
        while short and long:
            word = short[i_short]
            i_long = long.find(word)
            if i_long == -1:
                short = short[1:]
            else:
                # res += word
                res += 1
                short = short[1:]
                long = long[i_long + 1:]
        # return len(res)
        return res
        
# @lc code=end

