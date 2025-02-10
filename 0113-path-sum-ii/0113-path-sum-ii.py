# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node, curr_path, remaining_sum):
            if not node:
                return

            # Add current node to the path
            curr_path.append(node.val)
            
            if not node.left and not node.right and remaining_sum == node.val:
                result.append(list(curr_path))

            #recursivelt iterate left and right
            dfs(node.right, curr_path, remaining_sum - node.val)
            dfs(node.left, curr_path, remaining_sum - node.val)
            
            # Backtrack: Remove last node before returning
            curr_path.pop()

        dfs(root, [], targetSum)
        return result
