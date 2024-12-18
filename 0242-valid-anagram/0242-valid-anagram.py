class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_string_s = ''.join(sorted(s))
        sorted_string_t = ''.join(sorted(t))
        if sorted_string_s == sorted_string_t:
            return True
        else:
            return False