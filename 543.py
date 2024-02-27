# url: https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = [0]
        def find_d(node):
            if not node:
                return 0
            left = find_d(node.left)
            right = find_d(node.right)
            d[0] = max(d[0], left + right)
            return max(left, right) + 1
        find_d(root)
        return d[0]