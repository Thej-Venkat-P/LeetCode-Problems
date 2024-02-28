# url: https://leetcode.com/problems/find-bottom-left-tree-value/


from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        left = root
        next_queue = deque()

        while queue or next_queue:
            if queue:
                elem = queue.popleft()
                if elem.left:
                    next_queue.append(elem.left)
                if elem.right:
                    next_queue.append(elem.right)
            elif next_queue:
                queue = next_queue
                left = queue[0]
                next_queue = deque()

        return left.val


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = [root.val, 0]

        def dfs(node, depth):
            if not node:
                return
            if depth > ans[1]:
                ans[1] = depth
                ans[0] = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return ans[0]
