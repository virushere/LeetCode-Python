# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # # Iterative way to solve this problem
        # ## Maintain a stack to populate 2 values 1 current node and the targetsum - current value 
        # ## if targetsum - root value == 0 and it doesn't has child nodes then return True else all other cases will be False
        # stack = [( root , targetSum - root.val) ]
                
        # while stack:
        #     node, current_sum = stack.pop()

        #     if not node.left and not node.right and current_sum == 0:
        #         return True
            
        #     if node.right:
        #         stack.append((node.right, current_sum - node.right.val))

        #     if node.left:
        #         stack.append((node.left, current_sum - node.left.val))
        
        # return False

        ## Recursively solving the problem

        if not root.left and not root.right:
            return targetSum == root.val

        return (self.hasPathSum(root.left, targetSum - root.val) or  
                self.hasPathSum(root.right, targetSum - root.val))