#https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = []
        while head:
            reverse.insert(0, head.val)
            head = head.next
        for i in reverse:
            node = ListNode()
            node.val = i
            if head == None:
                head = node
            else:
                tail = head
                while tail.next != None:
                    tail = tail.next
                tail. next = node
        return head