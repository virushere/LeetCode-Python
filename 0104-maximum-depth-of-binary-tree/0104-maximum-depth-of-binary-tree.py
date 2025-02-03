# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            maxLeft = self.maxDepth(root.left)
            maxRight = self.maxDepth(root.right)
            return 1 + max(maxLeft, maxRight)