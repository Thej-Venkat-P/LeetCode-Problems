# url: https://leetcode.com/problems/distribute-coins-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dist(node, parent=None):
            if not node:
                return 0
            moves = dist(node.left, node) + dist(node.right, node)
            extra = node.val - 1
            if parent:
                parent.val += extra
            moves += abs(extra)
            return moves
        return dist(root)