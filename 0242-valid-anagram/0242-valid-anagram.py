class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        sorted_string_s = ''.join(sorted(s))
        sorted_string_t = ''.join(sorted(t))
        if sorted_string_s != sorted_string_t:
            return False
        else:
            return True
## Time: O(n log n) — sorting
## Space: O(n) — storing sorted strings

# # Solution 2
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # Time: O(n), Space: O(1)
#         # Edge case: different lengths can't be anagrams
#         if len(s) != len(t):
#             return False
        
#         # Build frequency map for characters in s
#         # Time: O(n) - iterate through all characters
#         # Space: O(1) - at most 26 lowercase letters
#         hashmap = {}
#         for char in s:
#             if char in hashmap:
#                 hashmap[char] = hashmap[char] + 1
#             else:
#                 hashmap[char] = 1
        
#         # Decrement counts for each character in t
#         # If any character in t doesn't exist in s, return False
#         # Time: O(n) - iterate through all characters
#         # Space: O(1) - no additional space (using same hashmap)
#         for char in t:
#             if char in hashmap:
#                 hashmap[char] = hashmap[char] - 1
#             else:
#                 return False
        
#         # If we made it here, all characters matched with correct frequencies
#         # Overall: Time O(n), Space O(1)
#         return True
