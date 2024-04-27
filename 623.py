# url: https://leetcode.com/problems/add-one-row-to-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def new_node(left=None, right=None):
            return TreeNode(val, left=left, right=right)
        dummy = new_node()
        dummy.left = root
        curr_depth = 0
        dq = collections.deque([(dummy, 0)])
        while dq:
            curr_node, curr_depth = dq.popleft()
            if curr_depth < depth - 1:
                if curr_node.left:
                    dq.append((curr_node.left, curr_depth + 1))
                if curr_node.right:
                    dq.append((curr_node.right, curr_depth + 1))
            elif curr_depth == depth - 1:
                prev_right = curr_node.right
                prev_left = curr_node.left
                curr_node.left = new_node(left=prev_left)
                curr_node.right = new_node(right=prev_right)
        return dummy.left

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def new_node(left=None, right=None):
            return TreeNode(val, left=left, right=right)
        if depth == 1:
            return TreeNode(val, root)
        def dfs(node, curr_depth):
            if not node:
                return
            if curr_depth != depth:
                dfs(node.left, curr_depth + 1)
                dfs(node.right, curr_depth + 1)
            else:
                curr_node = node
                prev_right = curr_node.right
                prev_left = curr_node.left
                curr_node.left = new_node(left=prev_left)
                curr_node.right = new_node(right=prev_right)
        dfs(root, 2)
        return root