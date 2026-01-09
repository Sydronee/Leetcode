# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None
            
            lDep, lNode = dfs(node.left)
            rDep, rNode = dfs(node.right)

            if lDep==rDep:
                return lDep+1, node
            elif lDep>rDep:
                return lDep+1, lNode
            else:
                return rDep+1, rNode
            
        return dfs(root)[1] 
