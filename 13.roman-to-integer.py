#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        dict_norm = {'M': 1000, 'D': 500, 'C': 100,
                     'L': 50, 'X': 10, 'V': 5, 'I': 1}
        s = s.replace('CM', 'DCCCC').replace('CD', 'CCCC').replace('XC', 'LXXXX').replace('XL', 'XXXX').replace('IX', 'VIIII').replace('IV', 'IIII')
        
        res = 0
        for cha in s:
            res += dict_norm[cha]
        return res

# @lc code=end
