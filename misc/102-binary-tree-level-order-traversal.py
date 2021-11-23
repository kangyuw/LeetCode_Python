#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        level_res = []
        bfs = deque()
        marker = TreeNode(float("-inf"))

        bfs.append(root)
        bfs.append(marker)

        while(bfs):
            current = bfs.popleft()

            if(current):
                if(current.val == float("-inf")): # 碰到 marker 了
                    res.append(level_res)
                    level_res = []
                    if(bfs): bfs.append(marker)
                else:
                    level_res.append(current.val)
                    bfs.append(current.left)
                    bfs.append(current.right)
                    
        res.pop()
        return res
        
# @lc code=end

