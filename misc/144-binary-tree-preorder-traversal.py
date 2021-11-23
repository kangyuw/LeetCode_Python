#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            cursor = stack.pop()
            if cursor:
                stack.append(cursor.right)
                stack.append(cursor.left)
                res.append(cursor.val)
        return res
        
# @lc code=end

