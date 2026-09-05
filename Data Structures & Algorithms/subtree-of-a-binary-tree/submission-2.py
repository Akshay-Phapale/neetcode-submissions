# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False
        
        def check(root, subTree):
            if not root and not subTree:
                return True
            if not root and subTree:
                return False
            if root and not subTree:
                return False
            if root.val != subTree.val:
                return False
            
            return check(root.left, subTree.left) and check(root.right, subTree.right)

        flag = False
        def dfs(root):
            nonlocal flag
            if not root:
                return
            
            if root.val == subRoot.val and check(root, subRoot):
                flag = True
                return
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return flag

            

