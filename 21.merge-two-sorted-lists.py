#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode(-1)
        head = p
        while l1 and l2:
            if l1.val <= l2.val:
                p.next, l1 = l1, l1.next
            else:
                p.next, l2 = l2, l2.next
            p = p.next
        
        if l1: p.next = l1
        else: p.next = l2
        
        return head.next
        
# @lc code=end

