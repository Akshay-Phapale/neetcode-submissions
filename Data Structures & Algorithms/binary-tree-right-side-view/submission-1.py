# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, depth, res):
        if not root:
            return
        if len(res) == depth:
            res.append(root.val)
        self.dfs(root.right, 1+depth, res)
        self.dfs(root.left, 1+depth, res)