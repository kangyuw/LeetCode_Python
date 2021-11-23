#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution():
    def isValidBST(self, root):
        if not root: return True
    
        stack = []
        prev = TreeNode(None)

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if prev.val != None and prev.val >= root.val: return False;
            prev = root
            root = root.right

    
        return True
        
# @lc code=end

