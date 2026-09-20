# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-infinity"), float("infinity"))    
    
    def dfs(self, root, min, max):
        if not root:
            return True
        
        if root.val <= min or root.val >= max:
            return False
        
        return self.dfs(root.left, min, root.val) and self.dfs(root.right, root.val, max)
        