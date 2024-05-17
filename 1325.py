# url: https://leetcode.com/problems/delete-leaves-with-a-given-value/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        node = root
        if not node:
            return None
        node.left = self.removeLeafNodes(node.left, target)
        node.right = self.removeLeafNodes(node.right, target)
        if not node.left and not node.right and node.val == target:
            return None
        return node