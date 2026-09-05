# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root, 0)
        return self.count
    
    def dfs(self, node, height):
        if not node:
            return 0
        
        height += 1

        self.count = max(self.count, height)

        self.dfs(node.left, height)
        self.dfs(node.right, height)
        

        