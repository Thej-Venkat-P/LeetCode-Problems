# url: https://leetcode.com/problems/sum-root-to-leaf-numbers/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(node, top):
            if not node:
                return 
            top = top*10 + node.val
            if not node.right and not node.left:
                self.sum += top
                return
            dfs(node.left, top)
            dfs(node.right, top)
        dfs(root, 0)
        return self.sum