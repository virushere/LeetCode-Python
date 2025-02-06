# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Edge case for empty tree

        queue = deque([(root, 1)])  # (node, depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if it's a leaf node
            if not node.left and not node.right:
                return depth
            
            # Otherwise, add the children to the queue with depth + 1
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))