# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ## METHOD 1 doing it iteratively 
        ## We do it using post order as we go till the depth of left child node 
        ## look for the root node each time makes the run time better.

        # stack = [] # to process child nodes
        # height = {} # to record height of nodes
        # visited = set() # to track if node is seen or not
        
        # while stack or root:
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         node = stack[-1] # Peek at the last node
        #         if node.right and node.right not in visited:
        #             root = node.right
        #         else:
        #             stack.pop()
        #             left_height = height.get(node.left, 0)
        #             right_height = height.get(node.right, 0)
                
        #             # check balance conditions
        #             if abs(left_height - right_height) > 1:
        #                 return False
                    
        #             height[node] = 1 + max(left_height,right_height)
        #             visited.add(node)
        # return True

    ## Method 2 recursive way
        return self.checkIfBalanced(root) != -1

    def checkIfBalanced(self, node: Optional[TreeNode]) -> int:
        if not node: 
            return 0 #Base case if empty root then return 0

        #Recursively get height of left and right subtrees
        left_height = self.checkIfBalanced(node.left)
        right_height = self.checkIfBalanced(node.right)

        # if left or right subtree is unbalanced then return -1 for False
        if left_height == -1 or right_height == -1:
            return -1
        
        # If the height difference is greater than 1, return -1 (not balanced)
        if abs(left_height - right_height) > 1:
            return -1

        # Otherwise return height of the current node
        return 1 + max(left_height, right_height)