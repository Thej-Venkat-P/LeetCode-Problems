# url: https://leetcode.com/problems/even-odd-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([root])
        asc = True
        while queue:
            curr_len = len(queue)
            prev = None
            for i in range(curr_len):
                node = queue.popleft()
                if asc:
                    if node.val % 2 == 0 or (prev and node.val <= prev.val):
                        return False
                else:
                    if node.val % 2 == 1 or (prev and node.val >= prev.val):
                        return False
                prev = node
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
            asc = not asc
        return True