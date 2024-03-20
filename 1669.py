# url: https://leetcode.com/problems/merge-in-between-linked-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        for i in range(a - 1):
            temp = temp.next
        temp1 = temp
        for i in range(b - a + 1):
            temp = temp.next
        temp2 = temp.next
        temp.next = None
        temp = None
        temp1.next = list2
        while temp1.next:
            temp1 = temp1.next
        temp1.next = temp2
        return list1