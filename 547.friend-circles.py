#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [False]*len(M)
        stack = []
        res = 0

        for i in range(len(M)):
            if not visited[i]:
                res += 1
                stack.append(i)
        
                while stack:
                    cursor = stack.pop()
                    visited[cursor] = True
                    for j in range(len(M[cursor])):
                        if not visited[j] and M[cursor][j]:
                            stack.append(j)
        return res
        
# @lc code=end

