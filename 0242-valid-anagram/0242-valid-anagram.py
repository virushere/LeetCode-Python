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