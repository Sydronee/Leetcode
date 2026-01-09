# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None
            
            lDep, lNode = dfs(node.left)
            rDep, rNode = dfs(node.right)

            if lDep==rDep:
                return lDep+1, node

            if lDep>rDep:
                return lDep+1, lNode
            
            return rDep+1, rNode
            
        return dfs(root)[1] 
