# url: https://leetcode.com/problems/remove-nodes-from-linked-list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rem(node):
            if node.next:
                rem(node.next)
                if node.next.val > node.val:
                    node.val = node.next.val
                    node.next = node.next.next
        rem(head)
        return head

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        temp = prev
        head = None

        maxi = -float('inf')
        while temp:
            if temp.val >= maxi:
                maxi = temp.val
                next_node = temp.next
                temp.next = head
                head = temp
                temp = next_node
            else:
                temp = temp.next
        return head