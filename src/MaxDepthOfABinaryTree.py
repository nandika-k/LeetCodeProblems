# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depthCalculator(root, 0)
    def depthCalculator(self, root, depth) -> int:
        if root is None:
            return depth
        return max(self.depthCalculator(root.left, depth+1), self.depthCalculator(root.right, depth+1))
