# url: https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        res = ListNode(0)
        res.next = head
        slow = fast = res
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        second = self.reverseTwo(slow.next)
        slow.next = None

        first = res.next
        while second:
            fn, sn = first.next, second.next
            first.next, second.next = second, fn
            first, second = fn, sn

        return res.next


    def reverseTwo(self, node):
        prev = None
        curr = node
        while curr:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp
        return prev