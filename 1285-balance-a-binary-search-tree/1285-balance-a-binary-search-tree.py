# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # 1. Collect all nodes in sorted order using Inorder Traversal
        sorted_nodes = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_nodes.append(node)
            inorder(node.right)
            
        inorder(root)
        
        # 2. Helper function to build a balanced BST from the sorted list
        def build_tree(left, right):
            if left > right:
                return None
            
            # Use the middle element as the root to ensure height balance
            mid = (left + right) // 2
            node = sorted_nodes[mid]
            
            # Recursively construct the left and right subtrees
            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)
            
            return node
            
        return build_tree(0, len(sorted_nodes) - 1)