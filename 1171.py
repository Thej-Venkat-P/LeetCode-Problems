# url: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        temp = dummy.next
        prefix_sums = {0:dummy}
        curr_sum = 0
        while temp:
            val = temp.val
            curr_sum += val
            if curr_sum not in prefix_sums:
                prefix_sums[curr_sum] = temp
            else:
                first_occ = prefix_sums[curr_sum]
                curr_occ = first_occ.next
                occ_sum = curr_sum
                while curr_occ != temp:
                    occ_sum += curr_occ.val
                    del prefix_sums[occ_sum]
                    curr_occ = curr_occ.next
                first_occ.next = temp.next
            temp = temp.next
        return dummy.next
    

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prefix_sums = {0:dummy}
        curr_sum = 0
        while head:
            curr_sum += head.val
            prefix_sums[curr_sum] = head
            head = head.next
        temp = dummy
        curr_sum = 0
        while temp:
            curr_sum += temp.val
            temp.next = prefix_sums[curr_sum].next
            temp = temp.next
        return dummy.next