#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dict_brk = {'(': ')', '[': ']', '{': '}'}
        stk = []
        while s:
            cha, s = s[0], s[1:]
            if cha in dict_brk.keys():
                stk.append(cha)
            else:
                if not stk or cha != dict_brk[stk.pop()]:
                    return False
        if stk: return False
        return True
# @lc code=end

