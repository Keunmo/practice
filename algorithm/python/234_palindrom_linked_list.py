# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums=[]
        while head != None:
            nums.append(head.val)
            head = head.next
        while len(nums) > 1:
            if nums[0] == nums[-1]:
                nums.remove(nums[0])
                if not nums:
                    return True
                nums.remove(nums[-1])
            else:
                break
        if len(nums) <= 1:
            return True
        return False
            
            
            
