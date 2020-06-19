#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
import collections, sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # 初始化字母表
        table = collections.Counter(t)
        
        # 初始化 Sliding Window
        begin = 0
        end = 0
        counter = len(t)
        cur_len = sys.maxsize
        ans = ''

        # Start Sliding Window
        while end < len(s):
            endchar = s[end]

            # 在字母表中找到對應的字母
            if table[endchar]:
                table[endchar] -= 1
                if table[endchar] == 0:
                    counter -= 1
            end += 1

            # 如果新 Window 比之前都要小
            while counter == 0:
                if end - begin < cur_len:
                    cur_len = end - begin
                    ans = s[begin:end]

                # 如果 s 開頭的字元 不在字母表中: 去掉它
                startchar = s[begin]

                if startchar in table:
                    table[startchar] += 1
                    if table[startchar] > 0: counter += 1
            
                begin += 1

        return ans
        
# @lc code=end

