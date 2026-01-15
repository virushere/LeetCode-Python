class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: strs = ["eat","tea","tan","ate","nat","bat"]
        # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        # Initialize a defaultdict with lists
        result = defaultdict(list)  
        
        # Iterate over each string
        for s in strs:
            count = [0] * 26  # Create a frequency count array for characters a-z
            for c in s:
                count[ord(c) - ord("a")] += 1  # Update frequency for each character
            result[tuple(count)].append(s)  # Use the frequency tuple as a key
            
        # Convert dict_values to a list
        return list(result.values())

# from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_map = defaultdict(list)
#         for word in strs:
#             sorted_str = "".join(sorted(word))
#             anagram_map[sorted_str].append(word)
#         return list(anagram_map.values())     