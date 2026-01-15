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

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     anagram_map = {}
        
    #     for word in strs:
    #         sorted_word = ''.join(sorted(word))
            
    #         if sorted_word in anagram_map:
    #             anagram_map[sorted_word].append(word)
    #         else:
    #             anagram_map[sorted_word] = [word]
        
    #     return list(anagram_map.values())        