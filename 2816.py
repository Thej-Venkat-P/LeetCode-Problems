# url: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        temp = dummy

        while temp.next:
            temp.val = (temp.val * 2 + (temp.next.val > 4)) % 10
            temp = temp.next
        temp.val = (temp.val * 2) % 10
        
        if dummy.val == 0:
            return head
        return dummy