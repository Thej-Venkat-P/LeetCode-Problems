# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        root = ListNode()
        temp = root
        carry = 0
        while l1 or l2 or carry:
            value_sum = 0

            value_sum += l1.val if l1 else 0
            l1 = l1.next if l1 else None

            value_sum += l2.val if l2 else 0
            l2 = l2.next if l2 else None

            value_sum += carry

            temp.next = ListNode(value_sum % 10)
            temp = temp.next
            carry = value_sum // 10

        return root.next
