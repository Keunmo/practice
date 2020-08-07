# https://leetcode.com/problems/sort-list/

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        vallist = []
        while head:
            vallist.append(head.val)
            head = head.next
        vallist.sort()
        head = ListNode(vallist[0])
        res = head
        for i in vallist[1:]:
            head.next = ListNode(i)
            head = head.next
        return res