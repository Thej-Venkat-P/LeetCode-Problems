# url: https://leetcode.com/problems/evaluate-boolean-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def eval(node):
            if not node.left:
                return node.val == 1
            elif node.val == 2:
                return eval(node.left) or eval(node.right)
            else:
                return eval(node.left) and eval(node.right)
        
        return eval(root)