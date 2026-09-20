# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        #self.dfs(root, 0, res)
        self.bfs(root, res)
        return res

    def dfs(self, root, level, res):
        if not root:
            return
        
        if len(res) <= level:
            res.append([])
        
        res[level].append(root.val)

        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)


    def bfs(self, root, res):

        q = collections.deque()

        q.append(root)

        while q:
            level = []
            n = len(q)

            for i in range(n):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)
