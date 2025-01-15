class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0
        for current_num in nums_set:
            # first check if its start of sequence
            if current_num - 1 not in nums_set:
                current_streak = 1
                while current_num + 1 in nums_set:
                    current_num += 1    
                    current_streak += 1
                
                longest_streak = max(longest_streak,current_streak)
        return longest_streak