# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head != None and head.val == val:
            head = head.next
        if head != None:
            cur = head
            prev = cur
            cur = cur.next
            while cur != None:
                if cur.val == val:
                    cur = cur.next
                    prev.next = cur
                    continue
                prev.next = cur
                cur = cur.next
                prev = prev.next
        return head