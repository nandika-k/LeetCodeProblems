# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightNodes = []
        nodes = collections.deque([root])

        while nodes:
            rightmost = None
            levelLen = len(nodes)

            for i in range(levelLen):
                node = nodes.popleft()

                if node:
                    rightmost = node
                    nodes.append(node.left)
                    nodes.append(node.right)
            if rightmost:
                rightNodes.append(rightmost.val)
        return rightNodes